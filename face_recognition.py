from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from datetime import datetime
import cv2
import os


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=(
            "times new roman", 35, "bold"), bg="white", fg="darkblue")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # First Image
        img_top = Image.open("College_images\\f7.jpg")
        img_top = img_top.resize((650, 700))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        f_lbl1 = Label(self.root, image=self.photoimg_top)
        f_lbl1.place(x=0, y=55, width=650, height=700)

        # Second Image
        img_bottom = Image.open("College_images\\f2.jpg")
        img_bottom = img_bottom.resize((950, 700))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        f_lbl2 = Label(self.root, image=self.photoimg_bottom)
        f_lbl2.place(x=650, y=55, width=950, height=700)

        # Button
        b1_1 = Button(f_lbl2, text="FACE RECOGNITION", command=self.face_recog,
                      cursor="hand2", font=("times new roman", 12, "bold"), bg="red", fg="white")
        b1_1.place(x=360, y=620, width=200, height=40)

    # Attendance Function
    def mark_attendance(self, i, r, n, d):
        with open("Ankits.csv", "r+", newline="\n") as f:
            myDataList = f.readlines()
            name_list = [line.strip().split(",")[0] for line in myDataList]

            if n not in name_list:
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{n},{i},{r},{d},{dtString},{d1},Present")

    # Face Recognition Logic
    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100 * (1 - predict / 300)))

                try:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="Ankit@3421", database="face_recognizer")
                    my_cursor = conn.cursor()

                    my_cursor.execute(
                        "SELECT Name, Student_id, Roll, Dep FROM student WHERE Student_id=%s", (str(id),))
                    result = my_cursor.fetchone()

                    if result:
                        n, i, r, d = result

                        if confidence > 85:
                            cv2.putText(
                                img, f"Roll:{r}", (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(
                                img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(
                                img, f"StudentId:{i}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            cv2.putText(
                                img, f"Dep:{d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 2)
                            self.mark_attendance(i, r, n, d)
                        else:
                            cv2.rectangle(
                                img, (x, y), (x+w, y+h), (0, 0, 255), 2)
                            cv2.putText(
                                img, "Unknown Face", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                        coord = [x, y, w, h]
                    else:
                        print(f"No student found with ID: {id}")
                except Exception as e:
                    print("Database error:", e)
                # finally:
                #     conn.close()

            return coord

        def recognizer(img, clf, faceCascade):
            self.coord = draw_boundary(
                img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier(
            "C://Users//asus//AppData//Roaming//Python//Python311//site-packages//cv2//data//haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            img = recognizer(img, clf, faceCascade)
            cv2.imshow("Welcome To Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Enter key
                break

        video_cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
