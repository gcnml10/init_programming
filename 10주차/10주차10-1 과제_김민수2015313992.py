from PIL import Image
from PIL import ImageFont, ImageDraw

# 1. Load profile photo image, student id card templete image, font file

photoImage = Image.open('./week10_01_image_and_font/week10_image_and_font/myeonglyun.png')
cardTemplete = Image.open('./week10_01_image_and_font/week10_image_and_font/student_id_card_empty.jpg')
#28,62 / 124,124

# 2. Resize profile photo image
photoImage_s = photoImage.resize((124,124))

# 3. Set the coordinate and merge profile photo to student id card templete with the coordinate
xy = (28,62)
cardTemplete.paste(photoImage_s, xy)

# 4. Put student name, major name into student id card templete using loaded font
draw = ImageDraw.Draw(cardTemplete)
font = ImageFont.truetype('NanumSquareRoundR.ttf', 20)
draw.rectangle([(175,125),(288,156)],fill='#ffffff')
draw.text((175,80), "김명륜\n경영학과\n", (0,0,0), font=font)
font = ImageFont.truetype('NanumSquareRoundR.ttf', 10)
draw.text((175,125), "ID No.2015313992\n2020.11.15", (0,0,0), font=font)
id_card = cardTemplete
# 5. Print the completed student id card
def display(card):
    card.show()
display(id_card)