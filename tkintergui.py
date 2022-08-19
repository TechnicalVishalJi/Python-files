import tkinter as tk

#Creating screen
root = tk.Tk()

#size of the screen
#Can only be used when every element is shown with .pack()
"""
root.geometry("160x90")  #(width, height)
root.minsize(160,90)
root.maxsize(320,180)
"""

#Placing text on the screen
text1 = tk.Label(root, text = "Text1")
#text1.pack()

#Placing text on the screen in row and column
text2 = tk.Label(root, text = "Text2")
text3 = tk.Label(root, text = "Text3")
space = tk.Label(root, text="      ").grid(row=2, column=2)

text1.grid(row=0, column=0)
text2.grid(row=1, column=1)
#space.grid(row=2, column=2)
text3.grid(row=3, column=3)

root.mainloop()
