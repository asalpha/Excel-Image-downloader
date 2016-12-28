import csv
import urllib
import urllib.request as ur
from urllib.error import URLError, HTTPError

def extract_rows(sheet_data):
    lst = []
    for row in sheet_data:
        lst.append(row)
    return lst

def main(workbook,col1,col2,col3):
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
    indx = s.rfind(".")
    if indx == -1:
        print("No extension for " + s)
        ext = ".EXTENTION"
    else:
        ext = s[indx: indx + 4]
    if ext == ".jpe":
        ext = ".jpeg"
    return ext

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
                rename = str(main) + '-' + str(sub) + get_extension(u)
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
