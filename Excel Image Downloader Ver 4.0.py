import tkinter
import csv
import urllib
import urllib.request as ur
from urllib.error import URLError, HTTPError
from tkinter import filedialog


window = tkinter.Tk()

window.title('Excel Image Downloader By Alpha Technologies')

window.geometry("766x640")

window.configure(background="Black")

window.wm_iconbitmap('bb.ico')

photo = tkinter.PhotoImage(file="atech.gif")

w = tkinter.Label(window, image=photo).grid(row = 0,column=0, padx=2, pady=2,ipadx=4, ipady=4,columnspan=4)


lb1 = tkinter.Label(window, text = 'Excel File Name', bg="#a1dbcd").grid(row=16,column=0,ipadx=3, ipady=3,padx=2, pady=2)
#en1 = tkinter.Entry(window)
#en1.grid(row=17,column=0)
lb2 = tkinter.Label(window, text = 'Image Column 1', bg="#a1dbcd").grid(row=16,column=1,ipadx=3, ipady=3,padx=2, pady=2)
en2 = tkinter.Entry(window)
en2.grid(row=17,column=1)
lb3 = tkinter.Label(window, text = 'Image Column 2', bg="#a1dbcd").grid(row=16,column=2,ipadx=3, ipady=3,padx=2, pady=2)
en3 = tkinter.Entry(window)
en3.grid(row=17,column=2)
lb4 = tkinter.Label(window, text = 'Image Column 3', bg="#a1dbcd").grid(row=16,column=3,ipadx=3, ipady=3,padx=2, pady=2)
en4 = tkinter.Entry(window)
en4.grid(row=17,column=3)



def extract_rows(sheet_data):
    lst = []
    for row in sheet_data:
        lst.append(row)
    return lst

def main():
    workbook = filename[:-4]
    col1 = int(en2.get())
    col2 = int(en3.get())
    col3 = int(en4.get())
    rfile = open(workbook + '.csv', 'r')
    csv_read = csv.reader(rfile)
    wfile = open(workbook + '_new' + '.csv', 'w', newline='')
    csv_write = csv.writer(wfile)
    lst_of_rows = extract_rows(csv_read)
    lst_of_rows[0][col1] = ""
    lst_of_rows[0][col2] = ""
    lst_of_rows[0][col3] = ""
    csv_write.writerow(lst_of_rows[0])
    write_data(lst_of_rows[1:], csv_write, col1,col2,col3)
    rfile.close()
    wfile.close()
    print("Your New spreadsheet is ready under the name " + workbook + "_new.csv")

def write_data(lor, wrt, c1, c2, c3):
    #print(lor[1])
    prefix = 0
    for rw in lor:
        prefix += 1
        lou = list(set([rw[c1], rw[c2], rw[c3]]))
        new_values = image_downloader(rw, lou, prefix)
        rw[7] = new_values[0]
        rw[8] = new_values[1]
        rw[c1] = ""
        rw[c2] = ""
        rw[c3] = ""
        wrt.writerow(rw)
    
def get_extension(s):
    #indx = s.rfind(".")
    #if indx == -1:
        #print("No extension for " + s)
        #ext = ".EXTENTION"
    #else:
        #ext = s[indx: indx + 4]
    #if ext == ".jpe":
        #ext = ".jpeg"
    #return ext
    ext = s.info()['Content-Type']
    ext = ext[ext.find('/') + 1:]
    if len(ext) > 4:
        x= '.' + ext[:ext.find(';')]
    else:
        x= '.' + ext
    print(x)    
    return x

def image_downloader(my_row, lst_of_url, main):
    sub = 0
    img_lst = []
    for u in lst_of_url:
        print(u)
        if u != "":
            sub += 1
            try:
                user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
                headers= {'User-Agent':user_agent,} 
                r = ur.Request(u, None, headers)                
                img = ur.urlopen(r)
            except urllib.error.URLError:
                print(my_row[4] + " ==> " + 'URL Not Working: ' + u)
            else:
                rename = str(main) + '-' + str(sub) + get_extension(img)
                f = open(rename,'wb')
                f.write(img.read())
                f.close()
                img_lst.append(rename)
    top_picture = ''
    for i in img_lst:
        print(i)
        top_picture = top_picture + "; " + i
    if img_lst != []:
        return [top_picture[2:], img_lst[0]]
    else:
        return ["",""]

#filename =''

def f():
    global filename
    filename = filedialog.askopenfilename(initialdir = "E:/Images",title = "Choose your file",filetypes = (("CSV files","*.csv"),("all files","*.*")))

btn1 = tkinter.Button(window, text="Browse your csv", command= lambda: f() , fg= "#a1dbcd", bg= "#383a39").grid(row=17,column=0,columnspan=1,ipadx=14, ipady=1,padx=8, pady=6)    
btn2 = tkinter.Button(window, text="Start downloading", command= lambda: main() , fg= "#a1dbcd", bg= "#383a39").grid(row=18,column=1,columnspan=2,ipadx=13, ipady=3,padx=12, pady=12)


window.mainloop()