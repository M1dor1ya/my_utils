from tkinter import *
import tkinter.filedialog
import tkinter.messagebox
# 导入tkinter模块的所有内容
from PIL import Image
from pic_anal import label


path = ''


def chose():
    file = tkinter.filedialog.askopenfilename()
    global path
    global image

    path = file
    image = Image.open(path)
    return 1
    # path = '' or abs_path


def show(image):
    if image:
        image.show()
    else:
        tkinter.messagebox.showwarning('警告', message='请先选择文件!')



def detail():
    global path
    global var
    if path != '':
        result = label.anal(path)

        # var.set('name：'+image.format+','+str(image.size[0])+'*'+str(image.size[1])+','+image.mode)
        var.set(result)
    else:
        tkinter.messagebox.showwarning('警告', message='请先选择文件!')


def show_path():
    global var2
    global path
    var2.set('图片路径：' + path)


def roll():
    if path != '':
        global image
        image = image.rotate(45)
        image.show()
    else:
        tkinter.messagebox.showwarning('警告', message='请先选择文件!')


def save():
    if path != '':
        image.save('new_pic.jpg')
    else:
        tkinter.messagebox.showwarning('警告', message='请先选择文件!')

root = Tk()
root.geometry('800x600')
var = StringVar()
var2 = StringVar()
# 创建一个文本Label对象
root.title = '图片处理器'

frm = Frame(root)

frm_R = Frame(frm)

textLabel = Label(frm_R, textvariable=var, justify=LEFT, padx=40)
textLabel.pack(side=TOP, anchor='w')
textLabel = Label(frm_R, textvariable=var2, justify=LEFT, padx=40)
textLabel.pack(side=TOP, pady=50, anchor='w')

frm_R.pack(side=RIGHT)

frm_L = Frame(frm)
chose_but = Button(frm_L, text="请选择图片", command=chose, padx=30)
chose_but.pack(side=TOP, padx=10, pady=40, anchor='w')
confirm_but = Button(frm_L, text="显示图片", command=lambda: show(image=image), padx=30)
confirm_but.pack(side=TOP, padx=10, anchor='w')
grey_but = Button(frm_L, text="识别", command=detail, padx=30)
grey_but.pack(side=TOP, padx=10, pady=40, anchor='w')
# but1 = Button(frm_L, text="显示图片路径", command=show_path, padx=30)
# but1.pack(side=TOP, padx=10, anchor='w')
# but2 = Button(frm_L, text="旋转图片", command=roll, padx=30)
# but2.pack(side=TOP, padx=10, pady=40, anchor='w')
# but3 = Button(frm_L, text="显示图片参数", command=detail, padx=30)
# but3.pack(side=TOP, padx=10, anchor='w')
# but4 = Button(frm_L, text="保存图片", command=save, padx=30)
# but4.pack(side=TOP, padx=10, pady=40, anchor='w')

frm_L.pack(side=LEFT, padx=50)
frm.pack()

root.mainloop()


