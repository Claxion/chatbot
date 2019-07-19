import csv

#4. dictwriter
with open('student.csv','w', encoding='utf-8', newline =' ') as f:
    fieldnames = ['name','major']
    writer = csv.DictWriter(f, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'name':'john', 'major':'cs'})
    writer.writerow({'name':'jaeseok', 'major':'math'})