import tkinter


window = tkinter.Tk()

window.title('Excel Image Downloader By Alpha Technologies')

window.geometry("766x630")

window.configure(background="Black")

window.wm_iconbitmap('bb.ico')

photo = tkinter.PhotoImage(file="atech.gif")

w = tkinter.Label(window, image=photo).grid(row = 0,column=0, padx=2, pady=2,ipadx=4, ipady=4,columnspan=4)
#w.pack(side=tkinter.TOP, padx=5)

#lbl = tkinter.Label(window, text = "Enter your Excel Filename")
#f_name = tkinter.Entry(window)
#lbl.pack(side= tkinter.TOP)
#f_name.pack()



#f_name = tkinter.Entry(window)

lbl2 = tkinter.Label(window, text = "Password", bg="#a1dbcd")

ent2 = tkinter.Entry(window)

#lbl2.pack(side=tkinter.RIGHT)
#ent2.pack(side=tkinter.RIGHT)

r = 0
l = ['a','b','c','d']


lb1 = tkinter.Label(window, text = 'Excel File Name', bg="#a1dbcd").grid(row=16,column=0,ipadx=3, ipady=3,padx=2, pady=2)
en1 = tkinter.Entry(window).grid(row=17,column=0)
lb2 = tkinter.Label(window, text = 'Image 1 row no.', bg="#a1dbcd").grid(row=16,column=1,ipadx=3, ipady=3,padx=2, pady=2)
en2 = tkinter.Entry(window).grid(row=17,column=1)
lb3 = tkinter.Label(window, text = 'Image 2 row no.', bg="#a1dbcd").grid(row=16,column=2,ipadx=3, ipady=3,padx=2, pady=2)
en3 = tkinter.Entry(window).grid(row=17,column=2)
lb4 = tkinter.Label(window, text = 'Image 3 row no.', bg="#a1dbcd").grid(row=16,column=3,ipadx=3, ipady=3,padx=2, pady=2)
en4 = tkinter.Entry(window).grid(row=17,column=3)

def callback():
    lbl3.configure(text=ent)
    
#lbl3 = tkinter.Label(window, text="Nothing Happened Yet")
#lbl3.pack()
presses = 0

def addclick():
    global presses
    presses += 1
    lbl4.configure(text= ent.get())
    
def userinput():
    inp = input("enter value")
    print(ent2)
lbl4 = tkinter.Label(window, text= "Enter your stuff here", fg= "#a1dbcd", bg= "#383a39")
#lbl4.pack(side=tkinter.BOTTOM)
    
    
btn2 = tkinter.Button(window, text="Click here",  command= addclick, fg= "#a1dbcd", bg= "#383a39")






#btn2.pack()
window.mainloop()