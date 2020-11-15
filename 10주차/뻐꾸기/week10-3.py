import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 500, height = 300)

def click(event):
    print("Click Location: ", event.x, event.y)
    r, g, b = img.getpixel((event.x, event.y))
    print("R:%d, G:%d, B:%d" % (r,g,b))

cv.bind("<Button-1>", click)
cv.pack()

img = Image.open("cat.jpg")
img_tk = ImageTk.PhotoImage(img)
cv.create_image(250, 250, image=img_tk)

root.mainloop()