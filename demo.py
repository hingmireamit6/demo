from tkinter import *

# Create main window
root = Tk()
root.title("Student Grade Calculator")
root.geometry("300x350")

# Function to calculate total, percentage and grade
def calculate():
    m1 = int(sub1.get())
    m2 = int(sub2.get())
    m3 = int(sub3.get())

    total = m1 + m2 + m3
    percentage = total / 3

    if percentage >= 75:
        grade = "A"
    elif percentage >= 60:
        grade = "B"
    elif percentage >= 50:
        grade = "C"
    else:
        grade = "Fail"

    lbl_total.config(text="Total Marks: " + str(total))
    lbl_percentage.config(text="Percentage: " + str(percentage))
    lbl_grade.config(text="Grade: " + grade)

# Labels and Entry boxes
Label(root, text="Subject 1 Marks").pack()
sub1 = Entry(root)
sub1.pack()

Label(root, text="Subject 2 Marks").pack()
sub2 = Entry(root)
sub2.pack()

Label(root, text="Subject 3 Marks").pack()
sub3 = Entry(root)
sub3.pack()

# Button
Button(root, text="Calculate", command=calculate).pack(pady=10)

# Result labels
lbl_total = Label(root, text="Total Marks:")
lbl_total.pack()

lbl_percentage = Label(root, text="Percentage:")
lbl_percentage.pack()

lbl_grade = Label(root, text="Grade:")
lbl_grade.pack()

# Run window
root.mainloop()