from tl.gpt_tl import createResponse
from tl.gcv_ovr import detect_txt
from gui.get_from_window import capture_window

#image_path = "./img/image.jpg"
img = capture_window("mGBA - 0.10.3")
print(f"Type of screenshot: {type(img)}")
img.save
# img_txt = detect_txt(image_path)
img_txt = detect_txt(saved=False, screenshot=img)

response = createResponse(img_txt)

print('-----------------------------------------TRANSLATED TEXT--------------------------------------------------')
print(response["message"])

print('---------------------------------------TOKEN COST---------------------------------------------------------')
print(response["in_tokens"])
print(response["out_tokens"])

print('-----------------------------------------TOTAL COST---------------------------------------------------------')
print(response["cost"])