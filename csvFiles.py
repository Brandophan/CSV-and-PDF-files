import csv
#open the file
data = open('example.csv',encoding ='utf-8')
#csv.reader
csv_data = csv.reader(data)
#reformat it into a python object list of lists
data_lines = list(csv_data)

#should get UnicodeDecodeError , need encoding = 'utf-8'
print(data_lines[0])
print(len(data_lines))
for line in data_lines[:5]: 
    print(line)
#can grab the email
print(data_lines[10][3])

#grab all the emails 

all_emails = []
for line in data_lines[1:15]: 
    all_emails.append(line[3])
    
print(all_emails)

full_names = []
for line in data_lines[1:]: 
    full_names.append(line[1]+' '+line[2])
    
print(full_names)

file_to_output = open('to_save_file.csv',mode='w',newline='')
csv_writer = csv.writer(file_to_output,delimiter=',')
#delimiter is another word for what is the seperator, what is seperating one word from another 


csv_writer.writerow(['a','b','c'])
csv_writer.writerows([['1','2','3'],['4','5','6']])

file_to_output.close()

f= open('to_save_file.csv',mode='a',newline='')

csv_writer = csv.writer(f)
csv_writer.writerow(['1','2','3'])
f.close()