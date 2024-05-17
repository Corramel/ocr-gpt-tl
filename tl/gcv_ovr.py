#This works when I use _my_ credentials, 
#but I want to impersonate a service account so I can transfer the file instead of having to rely on my own credentials that she most certainly does not have.

import base64
from io import BytesIO
import json

from PIL import Image as image_reader

from google.cloud import vision
#from google.protobuf.json_format import MessageToJson

def detect_txt(path):
    client = vision.ImageAnnotatorClient() 
    with image_reader.open(path) as f:
        file = f
        file_arr = BytesIO()
        file.save(file_arr, format='png')
        file_arr = file_arr.getvalue()

    image = vision.Image(content=file_arr)


    response = client.text_detection(image=image,
                                      image_context={"language_hints":["ja"]})
    texts = response.text_annotations
    print("-----------------------IMAGE TEXT OUTPUT-----------------------")
    output = texts[0].description
    print(output)
    # print(main_description)
    # for text in texts:
    #     # print(f'\n "{text.description}"')
    #     output += text.description
    #     # vertices = [
    #     #     f"({vertex.x},{vertex.y})" for vertex in text.bounding_poly.vertices
    #     # ]

    #     #print("bounds: {}".format(",".join(vertices)))

    if response.error.message:
        raise Exception(
            "{}\nFor more info on error messages, check: "
            "https://cloud.google.com/apis/design/errors".format(response.error.message)
        )
    
    return output

