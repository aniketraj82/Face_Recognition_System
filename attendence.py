from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import os
import csv

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.var_atten_id = StringVar()
        self.var_atten_roll = StringVar()
        self.var_atten_name = StringVar()
        self.var_atten_dep = StringVar()
        self.var_atten_time = StringVar()
        self.var_atten_date = StringVar()
        self.var_atten_attendance = StringVar()

        # Top Images
        img_top = Image.open("College_images\\f11.jpg").resize((800, 200))
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(
            x=0, y=0, width=800, height=200)

        img_bottom = Image.open("College_images\\f11.jpg").resize((800, 200))
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(
            x=800, y=0, width=800, height=200)

        # Background Image
        img3 = Image.open("College_images\\bg_pic.jpg").resize((1530, 710))
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE MANAGEMENT", font=(
            "times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2)
        main_frame.place(x=5, y=55, width=1480, height=600)

        # Left Frame
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Attendance Details",
                                font=("times new roman", 15, "bold"), bg="white", fg="black")
        Left_frame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("College_images\\f10.jpg").resize((720, 130))
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        Label(Left_frame, image=self.photoimg_left).place(
            x=5, y=0, width=720, height=130)

        left_inside_frame = Frame(Left_frame, relief=RIDGE, bg="white", bd=2)
        left_inside_frame.place(x=0, y=135, width=720, height=300)

        # Labels and Entries
        fields = [("AttendaceId:", self.var_atten_id), ("Roll:", self.var_atten_roll),
                  ("Name:", self.var_atten_name), ("Department:", self.var_atten_dep),
                  ("Date:", self.var_atten_date), ("Time:", self.var_atten_time)]
        positions = [(0, 0), (0, 2), (1, 0), (1, 2), (2, 0), (2, 2)]

        for (label, var), (row, col) in zip(fields, positions):
            Label(left_inside_frame, text=label, font=("times new roman", 12, "bold"),
                  bg="white").grid(row=row, column=col, padx=10, pady=5, sticky=W)
            ttk.Entry(left_inside_frame, textvariable=var, font=("times new roman", 12,
                      "bold"), width=17).grid(row=row, column=col+1, padx=10, pady=5, sticky=W)

        # Attendance Status
        Label(left_inside_frame, text="Attendance Status:", font=("times new roman",
              12, "bold"), bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        atten_combo = ttk.Combobox(left_inside_frame, textvariable=self.var_atten_attendance,
                                   font=("times new roman", 12, "bold"), state="readonly", width=15)
        atten_combo["values"] = ("Status", "Present", "Absent")
        atten_combo.current(0)
        atten_combo.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Buttons
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=170, width=715, height=35)

        Button(btn_frame, text="Import CSV", command=self.importCsv, font=("times new roman", 12, "bold"),
               width=17, bg="blue", fg="white").grid(row=0, column=0)

        Button(btn_frame, text="Export CSV", command=self.exportCsv, font=("times new roman", 12, "bold"),
               width=17, bg="blue", fg="white").grid(row=0, column=1)

        Button(btn_frame, text="Reset", command=self.reset_data, font=("times new roman", 12, "bold"),
               width=17, bg="blue", fg="white").grid(row=0, column=2)

        # Right Frame
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Attendance Records",
                                 font=("times new roman", 15, "bold"), bg="white", fg="black")
        Right_frame.place(x=750, y=10, width=720, height=580)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=700, height=455)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns=(
            "id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        headers = [("id", "Attendance ID"), ("roll", "Roll No"), ("name", "Name"),
                   ("department", "Department"), ("time", "Time"), ("date", "Date"),
                   ("attendance", "Status")]

        for col, text in headers:
            self.AttendanceReportTable.heading(col, text=text)
            self.AttendanceReportTable.column(col, width=100)

            self.AttendanceReportTable["show"] = "headings"
            self.AttendanceReportTable.pack(fill=BOTH, expand=1)
            self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    def fetchData(self, rows):
        self.AttendanceReportTable.delete(
            *self.AttendanceReportTable.get_children())
        for row in rows:
            self.AttendanceReportTable.insert("", END, values=row)

    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV",
                                         filetypes=[("CSV files", "*.csv")], parent=self.root)
        if fln:
            with open(fln) as myfile:
                csvread = csv.reader(myfile)
                for row in csvread:
                    mydata.append(row)
            self.fetchData(mydata)

    def exportCsv(self):
        try:
            if not mydata:
                messagebox.showerror(
                    "Error", "No data to export", parent=self.root)
                return
            fln = filedialog.asksaveasfilename(defaultextension=".csv", initialdir=os.getcwd(),
                                               title="Save CSV", filetypes=[("CSV files", "*.csv")], parent=self.root)
            if fln:
                with open(fln, mode="w", newline="") as myfile:
                    csvwriter = csv.writer(myfile)
                    for row in mydata:
                        csvwriter.writerow(row)
                messagebox.showinfo(
                    "Success", f"Data exported successfully to {os.path.basename(fln)}", parent=self.root)
        except Exception as e:
            messagebox.showerror(
                "Error", f"Error due to: {str(e)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        row = content['values']
        if row:
            self.var_atten_id.set(row[0])
            self.var_atten_roll.set(row[1])
            self.var_atten_name.set(row[2])
            self.var_atten_dep.set(row[3])
            self.var_atten_time.set(row[4])
            self.var_atten_date.set(row[5])
            self.var_atten_attendance.set(row[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
