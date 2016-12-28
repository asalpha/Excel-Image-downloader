Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> f
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f
NameError: name 'f' is not defined
>>> import csv
import urllib

def get_list():
    file = open('test.csv')
    csv_file = csv.reader(file)
    prod = ''
    img = []
    new_sheet = []
    for row in csv_file:
        if row[5] == prod:
            img.append(row[8])
        else:
            new_sheet.append([prod, img])
            prod = row[5]
            img = []
            img.append(row[8])
        if row[0] == '':
            return (new_sheet)

def downloader():
    url = 'http://www.snowbee.co.uk/_webedit/cached-images/1776-1789-0-300-high'
    #urllib.urlretrieve(url, 'abc.jpg')
    f = open('00002.jpg','w')
    f.write(urllib.urlopen(url).read())
    f.close()
    
