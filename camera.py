import cv2

cam = cv2.VideoCapture(0)

cv2.namedWindow("Python Webcam Screenshot App")

img_counter = 0
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab fame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k % 256 == 27:
        print("Escape hit, closing the app")
        break
    elif k % 256 == 32:
        img_name = "data/Opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("Taken photo")
        img_counter += 1

    # if self.txtuser.get() == "" or self.txtpass.get() == "":
    #         messagebox.showerror("Error", "All field required")
    #     elif:
    #         self.txtuser.get() == "Kapu" or self.txtpass.get() == "ashu":
    #         messagebox.showinfo("Success", "Welcome to Subharti Unversity")

    #     else:
    #         messagebox.showerror("Ivalid", "Invalid username and password")


cam.release()

cam.destroyAllvindows()
