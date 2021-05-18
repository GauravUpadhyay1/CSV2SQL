import mysql.connector
import csv
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import os


class Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("CSV2SQL Converter")
        self.root.geometry("600x400+300+100")
        self.root.config(bg="black")

        self.filename = StringVar()

        label_heading = Label(self.root, text="CSV2SQL Converter",
                              fg="white", bg="black", bd=5, relief=RAISED, font=("times new roman", 20, "bold"))
        label_heading.place(x=0, y=2, width=276)

        labelframeleft = LabelFrame(
            self.root, text="How to Use", font=("times new roman", 13, "bold"), padx=2, fg="white", bd=4, bg='black', relief=RAISED)
        labelframeleft.place(x=5, y=50, width=270, height=342)

        # labels and texts for instruction

        labelframeright = LabelFrame(
            self.root, bg="black", fg="white", bd=4, padx=2, relief=RAISED)
        labelframeright.place(x=280, y=2, width=318, height=389)

        label_heading_right = Label(
            labelframeright, text="Enter the details of your sql table", font=("times new roman", 13, "bold"), bg="black", fg="white", bd=4, padx=2, relief=RAISED)
        label_heading_right.place(x=1, y=0)

        label_filename = Label(
            labelframeright, text="Enter the file name", font=("times new roman", 15, "bold"), bg="black", fg="white", bd=4, padx=3, relief=RAISED)
        label_filename.place(x=45, y=60)

        self.label_filename_entry = ttk.Entry(
            labelframeright, width=30, textvariable=self.filename)
        self.label_filename_entry.place(x=43, y=160)

        btn_convert = Button(labelframeright, text="Convert", font=(
            "times new roman", 20, "bold"), relief=RAISED, bd=3, bg="Red", fg="black", command=self.add_data)
        btn_convert.place(x=71, y=250)

        # label instructions

        label_ins1 = Label(labelframeleft, text="1- Put the CSV file into the data folder.",
                           font=("times new roman", 12, "bold"), bg="black", fg="white")
        label_ins1.place(x=2, y=5)

        label_ins2 = Label(labelframeleft, text="2- Create a database and a table.",
                           font=("times new roman", 12, "bold"), bg="black", fg="white")
        label_ins2.place(x=2, y=50)

        label_ins3 = Label(labelframeleft, text="3- Enter the correct filename.",
                           font=("times new roman", 12, "bold"), bg="black", fg="white")
        label_ins3.place(x=2, y=95)

        label_ins4 = Label(labelframeleft, text="4- Click the convert button.",
                           font=("times new roman", 12, "bold"), bg="black", fg="white")
        label_ins4.place(x=2, y=140)

        label_ins5 = Label(labelframeleft, text="5- Open the database and check",
                           font=("times new roman", 12, "bold"), bg="black", fg="white")
        label_ins5.place(x=2, y=185)

        label_ins6 = Label(labelframeleft, text="THANK YOU FOR USING",
                           font=("times new roman", 15, "italic"), bg="black", fg="white", bd=5, relief=RAISED)
        label_ins6.place(x=8, y=250)

    def add_data(self):
        if self.filename.get() == "":
            messagebox.showerror("Error", "Enter a valid file name")

        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", user="root", password="gaurav4u7", database="csvtosql")
            # conn = mysql.connector.connect(
            #     host="localhost", username="root", password="gaurav4u7", database="csvtosql")

                with open(os.path.join(f"E:\Python\Projects\CSVTOSQL/{self.filename.get()}")) as csv_file:
                    csvfile = csv.reader(csv_file, delimiter=',')

                    all_values = []

                    for row in csvfile:
                        value = (row[0], row[1], row[2], row[3], row[4])
                        all_values.append(value)

                query = "insert into iris values (%s,%s,%s,%s,%s) "

                mycursor = conn.cursor()
                mycursor.executemany(query, all_values)
                conn.commit()
                messagebox.showinfo(
                    "Success", "Data has been successfully inserted")

            except Exception as es:
                messagebox.showwarning(
                    "warning", f"something went wront:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Converter(root)
    root.mainloop()
