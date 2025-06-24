from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_ilb = Label(self.root, text="DEVELOPER", font=(
            "times new roman", 35, "bold"), bg="white", fg="Green")
        title_ilb.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("College_images\\f12.jpg")
        img_top = img_top.resize((1530, 720))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # corrected: use photoimg_top
        f_lbl2 = Label(self.root, image=self.photoimg_top)
        f_lbl2.place(x=0, y=55, width=1530, height=720)

        main_frame = Frame(f_lbl2, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1 = Image.open("College_images\\f2.jpg")
        img_top1 = img_top.resize((200, 200))
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        # corrected: use photoimg_top
        f_lbl2 = Label(main_frame, image=self.photoimg_top1)
        f_lbl2.place(x=300, y=0, width=200, height=200)

        # Developer info
        title_ilb1 = Label(main_frame, text="Hii my name, Ankit !", font=(
            "times new roman", 20, "bold"), bg="white", fg="Green")
        title_ilb1.place(x=0, y=5)

        title_ilb1 = Label(main_frame, text="I am software developer With fast-moving technology and stiff competition, it’s crucial to possess your engineering team’s insights which will help you stay ahead. The usage of a development metrics dashboard will provide useful insights into the strengths and weaknesses of your team.", font=(
            "times new roman", 20, "bold"), bg="white", fg="Green")
        title_ilb1.place(x=0, y=40)

        img_top2 = Image.open("College_images\\f4.jpg")
        img_top2 = img_top2.resize((500, 300))
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        # corrected: use photoimg_top
        f_lbl2 = Label(main_frame, image=self.photoimg_top2)
        f_lbl2.place(x=0, y=200, width=500, height=300)


if __name__ == "__main__":
    root = Tk()
    obj = developer(root)
    root.mainloop()
