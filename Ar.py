from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import cv2
import os
import numpy as np


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_ilb = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_ilb.place(x=0, y=0, width=1530, height=45)

        # first image
        img_top = Image.open("College_images\\f7.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        # corrected: use photoimg_top
        f_lbl2 = Label(self.root, image=self.photoimg_top)
        f_lbl2.place(x=0, y=55, width=650, height=700)

        # second image
        img_bottom = Image.open("College_images\\f2.jpg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        # corrected: use photoimg_top
        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl2, text="FACE RECOGNITION", command=self.face_recog, cursor="hand2", font=(
            "times new roman", 12, "bold"), bg="red", fg="white")
        b1_1.place(x=360, y=620, width=200, height=40)

    # ======Attendace=======
    def mark_attendance(self, i, r, n, d):
        with open("Ankits.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.strip().split(",")[0] for line in myDataList]

            if n not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{i},{r},{d},{dtString},{d1},Present")

    # ::::::::::face recognition:::::::::::

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(
                    host="localhost", username="root", password="Ankit@3421", database="face_recognizer")
                my_cursor = conn.cursor()

                my_cursor.execute(
                    "select Name from student where Student_id="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute(
                    "select Student_id from student where Student_id="+str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                my_cursor.execute(
                    "select Roll from student where Student_id="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute(
                    "select Dep from student where Student_id="+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 68:
                    cv2.putText(
                        img, f"Student Id:{i}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 25), 2)
                    cv2.putText(
                        img, f"Enroll No:{r}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 25), 2)
                    cv2.putText(
                        img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 25), 2)
                    cv2.putText(
                        img, f"Department:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 25), 2)
                    self.mark_attendance(n, i, r, d)

                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y-5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.75, (255, 255, 255), 2)

                coord = [x, y, w, h]
            return coord

        def recognizer(img, clf, faceCascade):
            self.coord = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            self.ret, img = video_cap.read()
            img = recognizer(img, clf, faceCascade)
            cv2.imshow("Welcome To face Recognition", img)

            if cv2.waitKey(1) == 13:
                break
        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
