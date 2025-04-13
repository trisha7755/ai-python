from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

from array import array
import os
from PIL import Image
import sys
import time

'''
Authenticate
Authenticates your credentials and creates a client.
'''
#subscription_key = os.environ['7BH2pfeXXXXXXXXXXXXXXXXXXXXXXXXXXXX']
subscription_key = os.environ.get('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXgr', 'default_value')
#endpoint = os.environ['https://aemailabgen.cognitiveservices.azure.com/']
endpoint = "https://aemailab.cognitiveservices.azure.com/"
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))
'''
END - Authenticate
'''

'''
OCR: Read File using the Read API, extract text - remote
This example will extract text in an image, then print results, line by line.
This API call can also extract handwriting style text (not shown).
'''
print("===== Read File - remote =====")
# Get an image with text
read_image_url = "https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png"

# Call API with URL and raw response (allows you to get the operation location)
read_response = computervision_client.read(read_image_url,  raw=True)

# Get the operation location (URL with an ID at the end) from the response
read_operation_location = read_response.headers["Operation-Location"]
# Grab the ID from the URL
operation_id = read_operation_location.split("/")[-1]

# Call the "GET" API and wait for it to retrieve the results 
while True:
    read_result = computervision_client.get_read_result(operation_id)
    if read_result.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# Print the detected text, line by line
if read_result.status == OperationStatusCodes.succeeded:
    for text_result in read_result.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print(line.bounding_box)
print()
'''
END - Read File - remote
'''

print("End of Computer Vision quickstart.")




+++++++++++++++++++++++
Env Setup Code
++++++++++++++++++++++

    sudo su -
     apt-get update
    2  mkdir application
    3  cd application/
    4  ls -l
    5  pip install --upgrade azure-cognitiveservices-vision-computervision
    6  apt install python3-pip
    7  pip install --upgrade azure-cognitiveservices-vision-computervision
    8  apt install python3-venv -y
    9  python3 -m venv myenv
   10  source myenv/bin/activate
   11  pip install --upgrade pip
   12  pip install --upgrade azure-cognitiveservices-vision-computervision
   13  pip install pillow
   14  code app.py
   15  nano app.py
   16  ls -l
   17  cd myenv/
   18  ls -l
   19  cd ..
   20  ls -l
   21  python app.py
