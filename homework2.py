import tkinter as tk
screen = tk.Tk()
screen.geometry("500x500")

label = tk.Label(screen, text = "Email", background = "blue")
label.place(x=150, y=20)

entry = tk.Entry(screen, width=20)
entry.place(x= 200, y=16)

label2 = tk.Label(screen, text= "Password", background = "blue")
label2.place(x=125, y=50)

entry2 = tk.Entry(screen, width=20)
entry2.place(x=200, y=47)

label3 = tk.Label(screen, text = "What food would you like?", background = "blue")
label3.place(x=125,y=80)

drop_down_option = tk.StringVar(screen)
food = ["burger", "pizza", "salad", "pasta"]
drop_down_option.set("Choose option")
drop_down = tk.OptionMenu(screen, drop_down_option,*food)
drop_down.place(x=300,y=79)

def click():
    email = entry.get()
    option = drop_down_option.get()
    print(option)
    print(email)

button = tk.Button(screen, text= "Submit", background = "purple", command=click)
button.place(x=200,y=100)





screen.mainloop()