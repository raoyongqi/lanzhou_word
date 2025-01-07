from PIL import Image

# 打开原始图片
image = Image.open('Untitled.png')

# 调整图片大小为 295x413 像素
image_resized = image.resize((295, 413))

# 保存调整后的图片
image_resized.save('output.jpg')
