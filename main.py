from tl.gpt_tl import createResponse
from tl.gcv_ovr import detect_txt

image_path = "./img/image.jpg"

img_txt = detect_txt(image_path)

response = createResponse(img_txt)

print('-----------------------------------------TRANSLATED TEXT--------------------------------------------------')
print(response["message"])

print('---------------------------------------TOKEN COST---------------------------------------------------------')
print(response["in_tokens"])
print(response["out_tokens"])

print('-----------------------------------------TOTAL COST---------------------------------------------------------')
print(response["cost"])