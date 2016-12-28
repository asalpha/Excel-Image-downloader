import csv
import urllib
import urllib.request as ur

def get_list():
    file = open('test1.csv')
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
    new_sheet.append([prod, img])
    print(len(new_sheet) - 2)
    return new_sheet[2:]

def downloader():
    lol = get_list()
    main = 0
    for x in lol:
        sub = 1
        main = main + 1
        for y in x[1]:
            f = open(str(main) + '-' + str(sub) + '.jpg','wb')
            f.write(ur.urlopen(y).read())
            f.close()
            sub = sub + 1
    
