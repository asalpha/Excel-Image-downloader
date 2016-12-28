import tkinter


window = tkinter.Tk()

window.title('Excel Image Downloader By Alpha Technologies')

window.geometry("766x630")

window.configure(background="Black")

window.wm_iconbitmap('bb.ico')

photo = tkinter.PhotoImage(file="atech.gif")

w = tkinter.Label(window, image=photo).grid(row = 0,column=0, padx=2, pady=2,ipadx=4, ipady=4,columnspan=4)


lb1 = tkinter.Label(window, text = 'Excel File Name', bg="#a1dbcd").grid(row=16,column=0,ipadx=3, ipady=3,padx=2, pady=2)
en1 = tkinter.Entry(window)
en1.grid(row=17,column=0)
lb2 = tkinter.Label(window, text = 'Image 1 row no.', bg="#a1dbcd").grid(row=16,column=1,ipadx=3, ipady=3,padx=2, pady=2)
en2 = tkinter.Entry(window)
en2.grid(row=17,column=1)
lb3 = tkinter.Label(window, text = 'Image 2 row no.', bg="#a1dbcd").grid(row=16,column=2,ipadx=3, ipady=3,padx=2, pady=2)
en3 = tkinter.Entry(window)
en3.grid(row=17,column=2)
lb4 = tkinter.Label(window, text = 'Image 3 row no.', bg="#a1dbcd").grid(row=16,column=3,ipadx=3, ipady=3,padx=2, pady=2)
en4 = tkinter.Entry(window)
en4.grid(row=17,column=3)


def work():
    a = en1.get()
    b = en2.get()
    c = en3.get()
    d = en4.get()   
    main
    

    
btn2 = tkinter.Button(window, text="Click here", command= lambda: work() , fg= "#a1dbcd", bg= "#383a39").grid(row=18,column=1,columnspan=2,ipadx=13, ipady=3,padx=12, pady=12)


window.mainloop()