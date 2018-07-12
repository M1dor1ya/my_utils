from PIL import Image
image = Image.open("C:\\Users\\admin-x\\Desktop\\JFLA.jpg")
print(type(image.format))
print(image.mode)
print(image.size)
# image.show()  显示图片
# print(image.format, image.size, image.mode)  图片格式  大小
# def cut(left, upper, right, lower):
#     box = (left, upper, right, lower)
#     region = image.crop(box)
# image.thumbnail((128, 128))  缩略图


