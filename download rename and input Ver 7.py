import csv
import urllib
import urllib.request as ur
from urllib.error import URLError, HTTPError

def fun(workbook):
    ifile = open(workbook + '.csv', 'r')
    csv_file = csv.reader(ifile)
    file = open(workbook + '_new' + '.csv', 'w', newline='')
    csv_new = csv.writer(file)
    main = 0
    sub = 0
    cell = []
    q = 'g'
    for row in csv_file:
        if row[8] == 'Model Picture':
            csv_new.writerow(row)
        else:
            main = main + 1
            sub = 0
            loi = row[8].split('; ')
            if cell != []:
                write_value = make_str(cell)
                past[7] = write_value[0]
                past[8] = write_value[1]
                csv_new.writerow(past)        
            cell = []
            past = row
            for x in loi:
                if x == '':
                    write_value = make_str(cell)
                    row[7] = write_value[0]
                    row[8] = write_value[1]
                    csv_new.writerow(row)                    
                    ifile.close()            
                    file.close()
                    return "ITS DONE 111"
                else:
                    try:
                        img = ur.urlopen(x)
                    except urllib.error.URLError:
                        print('URL Not Working: ' + x)
                    else:
                        sub = sub + 1
                        rename = str(main) + '-' + str(sub) + x[(len(x) - 4):]
                        f = open(rename,'wb')
                        f.write(img.read())
                        f.close()
                        cell.append(rename) 
    write_value = make_str(cell)
    row[7] = write_value[0]
    row[8] = write_value[1]
    csv_new.writerow(row) 
    ifile.close()            
    file.close()
    return "ITS DONE 222"

def make_str(los):
    first = los[0]
    last = ''
    for s in los:
        last = last + s + '; '
    return [first, last[:-2]]