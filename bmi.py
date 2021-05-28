from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0,'end')
    height_tf.delete(0,'end')
    weight_tf.delete(0,'end')

def calculate_bmi():
    kg = int(weight_tf.get())
    m = int(height_tf.get())/100
    bmi = kg/(m*m)
    bmi = round(bmi, 1)
    bmi_index(bmi)

def bmi_index(bmi):
    if (bmi < 14.99):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Very Severely Underweight'.format(bmi))
    elif (bmi > 15) and (bmi < 15.99):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Severely Underweight'.format(bmi))
    elif (bmi > 16) and (bmi < 18.49):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Underweight'.format(bmi))
    elif (bmi > 18.5) and (bmi < 24.99):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Healthy'.format(bmi))
    elif (bmi > 25) and (bmi < 29.99):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Overweight'.format(bmi))
    elif (bmi > 30) and (bmi < 34.99):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Moderately Obese'.format(bmi))
    elif (bmi > 35) and (bmi < 39.99):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Severely Obese'.format(bmi))
    elif (bmi > 40):
        messagebox.showinfo('BMI_CALCULATOR', 'BMI = {} \n Your results show that you are Verey Severely or Morbidly Obese'.format(bmi))
    else:
        messagebox.showerror('BMI_CALCULATOR', 'OOPS something went wrong!!')

window = Tk()
window.title('BMI CALCULATOR')
window.geometry('380x400')
window.config(bg='#49A')

var = IntVar()

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)


age_lb = Label(
    frame,
    text="Enter Age (2 up to 120)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Select Gender'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text = 'Male',
    variable = var,
    value = 1
)
male_rb.pack(side=RIGHT)

female_rb = Radiobutton(
    frame2,
    text = 'Female',
    variable = var,
    value = 2
)
female_rb.pack(side=LEFT)

height_lb = Label(
    frame,
    text="Enter Height (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Enter Weight (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Calculate',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Reset',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Exit',
    command=lambda:ws.destroy()
)
exit_btn.pack(side=RIGHT)

window.mainloop()
