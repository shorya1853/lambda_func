# Lambda function to check if file is CSV file using python_magic


## Using aws APIgatway `event["binary"]` which return binary file and store in lambda function /tmp/ folder, `detect_file_type()` check if file is CSV and save it in S3 bucket

**Layers for Lambda Function**

  **Magic layer**
  > install python_magic using `pip install python_magic -t . `zip it using zip or compress and add it as layer
> 
  **Libmagic**
  > Download ```file-libs-5.39-7.amzn2023.0.2.x86_64.rpm``` from [here](https://amazonlinux.pkgs.org/2023/amazonlinux-x86_64/file-libs-5.39-7.amzn2023.0.2.x86_64.rpm.html)
> 
  **Magic file**
  > add magic file as layer, from above downloaded file /usr/share/misc zip it and add. using magic.mgc file in lambda function [by adding location of layer]() in `magic.Magic()`
  
  ### Happing coding :sunglasses:	
