
import tkinter as tk

root = tk.Tk()
root.geometry('200x300')
root.title('i am your assistent')
root.configure(bg="#e8e8e8")

e1 = tk.Text(root)
e1.place(x=10,y=35,height=50,width=180)

l1 = tk.Label(root,text='Output: ', bg="#e8e8e8")
l1.place(x=10,y=5)

e2 = tk.Text(root)
e2.place(x=10,y=150,height=30,width=180)

l2 = tk.Label(root,text='You said: ', bg="#e8e8e8")
l2.place(x=10,y=120)

root.mainloop()

