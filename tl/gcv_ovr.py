import os

import base64 #potentially for later use when building GUI

from io import BytesIO
import json

from PIL import Image as image_reader

from google.cloud import vision

from google.auth import impersonated_credentials
from google.oauth2 import service_account

#Need to get path to key
path_to_key = '../api/service_account_key.json'
path_to_key = os.path.join(os.path.dirname(__file__), path_to_key)

key_file = open(path_to_key)
key_obj = json.load(key_file)


target_service_acc = key_obj["client_email"]

target_credentials = impersonated_credentials.Credentials(
    source_credentials=service_account.Credentials.from_service_account_file(path_to_key),
    target_principal=target_service_acc,
    target_scopes=['https://www.googleapis.com/auth/cloud-platform'], 
    lifetime=60
)

def detect_txt(path, language="ja"): #language added just in case of future use...
    client = vision.ImageAnnotatorClient(credentials=target_credentials) 
    with image_reader.open(path) as f:
        file = f
        file_arr = BytesIO()
        file.save(file_arr, format='png')
        file_arr = file_arr.getvalue()

    image = vision.Image(content=file_arr)


    response = client.text_detection(image=image,
                                      image_context={"language_hints":[language]})
    texts = response.text_annotations
    print("-----------------------IMAGE TEXT OUTPUT-----------------------")
    output = texts[0].description
    print(output)

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    
    return output

#Used for testing
#detect_txt(path="C:/Users/Corr/Documents/ShareX/Screenshots/2024-05/firefox_Q3h5qQnriu.png")