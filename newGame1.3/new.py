import glob
import cv2
from tkinter import *
root = Tk()
root.attributes("-fullscreen", True)
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
img1= 'player/100x150/*.png'
img2 = 'player1.png'
addrs = glob.glob(img1)
imz2 = cv2.imread(img2, cv2.IMREAD_UNCHANGED)

c = 0
# print(addrs)
for add in addrs:
    print(add)
    imz = cv2.imread(add, cv2.IMREAD_UNCHANGED)
    # cv2.imshow("data",imz)
    # add = add[:-3] + "jpg"
    # new = 'img' + str(c) + '.jpeg'
    img = cv2.resize(imz, (100, 150), interpolation=cv2.INTER_CUBIC)
    imz[:,:,3] = imz2[:,:,3]
    # print(imz, imz2)
    cv2.imwrite(add, img)
    c+=1
    cv2.waitKey(1)
    cv2.destroyAllWindows()
