from tkinter import *

def display_data():
    n = name.get()
    s = subject.get()
    g = grade.get()
    data_list.append((n, s, g))
    name.set('')
    subject.set('')
    grade.set('')

def show_all_data():
    all_data_window = Toplevel(root)
    all_data_window.title('All Stored Data')
    all_data_window.geometry('300x200')

    for i, data in enumerate(data_list):
        Label(all_data_window, text=f"Entry {i+1}", font=('Arial', 10, 'bold')).pack(pady=5)
        Label(all_data_window, text=f"Name: {data[0]}", font=('Arial', 10)).pack()
        Label(all_data_window, text=f"Subject: {data[1]}", font=('Arial', 10)).pack()
        Label(all_data_window, text=f"Grade: {data[2]}", font=('Arial', 10)).pack()
        Label(all_data_window, text="-"*20, font=('Arial', 10)).pack(pady=5)

root = Tk()
root.title('Grade Page')
root.geometry('500x400')
name = StringVar()
subject = StringVar()
grade = StringVar()


data_list = []
f1 = Frame(root)
f1.pack(pady=10)

name_label = Label(f1, text='Name', font=('Arial', 12))
name_label.pack(side='left', padx=10)

name_entry = Entry(f1, textvariable=name, width=30)
name_entry.pack(side='right')


f2 = Frame(root)
f2.pack(pady=10)

subject_label = Label(f2, text='Subject', font=('Arial', 12))
subject_label.pack(side='left', padx=10)

subject_entry = Entry(f2, textvariable=subject, width=30)
subject_entry.pack(side='right')

f3 = Frame(root)
f3.pack(pady=10)

grade_label = Label(f3, text='Grade', font=('Arial', 12))
grade_label.pack(side='left', padx=10)

grade_entry = Entry(f3, textvariable=grade, width=30)
grade_entry.pack(side='right')

submit_button = Button(root, text='Submit', command=display_data, font=('Arial', 12))
submit_button.pack(pady=20)


bottom_frame = Frame(root)
bottom_frame.pack(side='bottom', fill='x')

bottom_button = Button(bottom_frame, text='Show All Data', bg='white', fg='black', font=('Arial', 12), command=show_all_data)
bottom_button.pack(side='right', padx=10, pady=10)

root.mainloop()
