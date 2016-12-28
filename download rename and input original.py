import csv
import urllib
import urllib.request as ur


def fun(workbook):
    ifile = open(workbook + '.csv', 'r')
    csv_file = csv.reader(ifile)
    file = open(workbook + '_new' + '.csv', 'w')
    csv_new = csv.writer(file)
    main = 0
    sub = 0
    cell = []
    q = 'g'
    for row in csv_file:
        main = main + 1
        sub = 0
        loi = row[8].split('; ')
        if cell != []:
            write_value = make_str(cell)
            row[7] = write_value[0]
            row[8] = write_value[1]
            csv_new.writerow(row)        
        cell = []
        for x in loi:
            if x == '':
                ifile.close()            
                file.close()
                return None
            else:
                sub = sub + 1
                rename = str(main) + '-' + str(sub) + '.jpg'
                f = open(rename,'wb')
                f.write(ur.urlopen(x).read())
                f.close()
                cell.append(rename)
                
    ifile.close()            
    file.close()
    return None

def make_str(los):
    if los == []:
        return ['Top Picture(s)', 'Model Picture']
    first = los[0]
    last = ''
    for s in los:
        last = last + s + '; '
    return [first, last[:-2]]