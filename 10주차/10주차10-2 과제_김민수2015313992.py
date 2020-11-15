from PIL import Image
from PIL import ImageFilter

# 도로 이미지 road.png 불러오기
### do not edit here ###
source = Image.open('road.png')
horizon = 300
sx, sy = source.size

# 도로 이미지 road.png와 같은 사이즈의 새로운 이미지 생성
### your code here ###
size = (1308,982)
new_img = Image.new("RGB", size, (0,0,0))

# RGB 값 중 최소값이 0xf0이상이면 분홍색으로 변경 (분홍색 RGB 값 : (0xf0, 0x50, 0x90))
### your code here ###
for y in range(horizon, sy):
    for x in range(sx):
        rgb_i = source.getpixel((x,y))

        if min(rgb_i) > 0xf0:
            new_img.load()[x,y] = (0xf0, 0x50, 0x90)

# ImageFilter 모듈 중 이미지의 edge를 찾아주는 필터를 적용해 최종 결과를 출력
### your code here ###

new_img = new_img.filter(ImageFilter.EDGE_ENHANCE)

# 최종 이미지 결과 출력
### your code here ###
new_img.show()