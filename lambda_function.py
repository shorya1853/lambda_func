import boto3
import base64
import magic

#Check if file is csv 
def detect_file_type(file_path) -> str:
    """
    Lambda function layer location (Magic file)>>>>>>>>>>>>>>>>>>>>>>>/opt/lib/magic.mgc
    """
    #magic_instance = magic.Magic(mime=True, magic_file= "/opt/lib/magic.mgc")
    magic_instance = magic.Magic(mime=True)
    file_type = magic_instance.from_file(file_path)
    """
    Check if file contain "," return text/csv
    """
    if file_type == "text/plain":
        with open(file_path, 'r', errors='replace') as file:
            content = file.read()
            if "," in content:
                return "text/csv"
    return file_type

#Convert file into binary
def csv_to_binary(csv_file_path, binary_file_path):
    try:
        with open(csv_file_path, 'r', errors='replace') as csvfile:
            csv_data = csvfile.read()

        binary_data = csv_data.encode('utf-8')

        with open(csv_file_path, 'wb') as binary_file:
            binary_file.write(binary_data)

        print(f"CSV file '{csv_file_path}' has been converted to binary and saved as '{binary_file_path}'.")
        return csv_file_path
    except Exception as e:
        print(f"Error: {e}")

#Storing file in lambda  /tmp/ 
def write_to_tmp(binarydata)-> bool:
    path = "/tmp/data.csv"
    try:
        with open(path, "w") as file:
            file.write(binarydata)
            file.close()
        print("Wrote in /tmp/data.csv")
        return True
    except Exception as e:
        print(f"messa: {e}")
        return False



def lambda_function(event, content) -> str:
    binarydata = event["binary"]

    decoded_data = base64.b64decode(binarydata)

    s3 = boto3.client("s3")
    try:
        if write_to_tmp(decoded_data):
            res = detect_file_type("/tmp/data.csv")
            if res == 'CSV text':
                #if file is CSV text save it in s3 bucket
                s3.upload_file(decoded_data, "csvconverted123", 'binary.csv')
                return {
            'statusCode': 200,
            'body': "Saved to S3"
            }

            else:
                 return {
            'statusCode': 400,
            'body': f"Please select CSV file!"
            }

        else: 
            return None
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Was not able to upload csv ,' + str(e)
        }








