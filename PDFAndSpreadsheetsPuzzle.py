import csv
import re
import PyPDF2

# Task One: Grab the Google Drive Link from .csv File
data_file_path = '/Volumes/Extreme SSD/The complete python bootcamp from zero to hero in python/WorkingwithPDFAndSpreadsheetCSV/Excercise_Files/find_the_link.csv'
with open(data_file_path, encoding="utf-8") as data:
    csv_data = csv.reader(data)
    data_lines = list(csv_data)
    
    # Initialize an empty string for the link
    link_str = ''
    
    # Concatenate the diagonal elements
    for row_num in range(len(data_lines)):
        link_str += data_lines[row_num][row_num]
    
    print("Google Drive Link:", link_str)

# Task Two: Extract Phone Number from PDF
pdf_file_path = '/Volumes/Extreme SSD/The complete python bootcamp from zero to hero in python/WorkingwithPDFAndSpreadsheetCSV/Excercise_Files/Find_the_Phone_Number.pdf'
with open(pdf_file_path, 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Initialize a variable to store all text
    all_text = ''
    
    # Extract text from each page
    for n in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[n]
        page_text = page.extract_text()
        all_text += ' ' + page_text
    
    # Print the entire text (optional)
    # print(all_text)
    
    # Define a regex pattern to find phone numbers (various formats)
    phone_pattern = r'\d{3}.\d{3}.\d{4}'
    
    # Find all matching phone numbers
    # phone_numbers = re.findall(phone_pattern, all_text)
    #or 
    for match in re.finditer(phone_pattern,all_text): 
        print(match)
    #print(all_text[41790:42919+20])
    
    # Print all found phone numbers
    # print("Phone Numbers Found:")
    # for number in phone_numbers:
    #     print(number)
