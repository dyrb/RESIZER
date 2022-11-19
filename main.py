from PIL import Image

image = input('Введите название изображения (image.png): ')
extension = image.split(".",1)[1]


image = Image.open(image)

width = int(input('Введите ширину: '))
height = int(input('Введите высоту: '))

final = image.resize((width, height))
final.save(f'{width}_{height}_size.{extension}')
