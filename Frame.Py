import os
from PIL import Image, ImageDraw, ImageFilter

class frame():
    def __init__(self, current_image):
        self.current_image = current_image
        self.img = Image.open(current_image)
        print(self.img.size)
    def edit_edit(self):
        self.img.show()
    def edit_resize(self):
        lop = True
        while lop is True:
            try:
                print("new size Width(%)")
                h = int(input())/100
                print("new size Height(%)")
                p = int(input())/100
            except:
                print("Input must be an interger number!\nOne or more inputs are not")
            else:
                lop = False
        self.img = self.img.resize((int(self.img.size[0]*h),int(self.img.size[1]*p)))
        self.img.show()
    def edit_cut(self):
        self.img.show()
    def edit_filter(self):
        self.img.show()
    def edit_color_mode(self):
        self.img.show()

def salid(nya):
    print("0 to stay 1 to leave 2 to save")
    

print(os.getcwd())
print("select file by typing it")
lop = True
while lop is True:
    try:
        frame_a = frame(f"{os.getcwd()}\{input()}")
    except:
        print("incorrect statement or input")
    else:
        lop = False

print(f"image {frame_a.current_image}")
print("1 edit\n2 resize\n3 cut\n4 filter\n5 color mode\nselect option:")
nya = True
while nya is True:
    p = 0
    lop = True
    while lop is True:
        try:
            p = int(input())
        except:
            print("Input must be an interger number!")
            print("1 edit\n2 resize\n3 cut\n4 filter\n5 color mode\nselect option:")
        else:
            lop = False
    if p == 1:
        frame_a.edit_edit()
    elif p == 2:
        frame_a.edit_resize()
    elif p == 3:
        frame_a.edit_cut()
    elif p == 4:
        frame_a.edit_filter()
    elif p == 5:
        frame_a.edit_color_mode()
    else:
        print(f"{p} is not and option")
    #salid(nya)
    break

