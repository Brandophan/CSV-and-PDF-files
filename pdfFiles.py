import PyPDF2

# Open the PDF file
with open('Working_Business_Proposal.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    print(len(pdf_reader.pages))
    # Extract text from each page
    # for page_num in range(len(reader.pages)):
    #     page = reader.pages[page_num]
    #     text = page.extract_text()
    #     print(f"Page {page_num + 1}:\n{text}\n")
    page_one = pdf_reader.pages[0]
    page_one_text = page_one.extract_text()
    print(page_one_text)
    
# Open the original PDF file
with open('Working_Business_Proposal.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)  # Use PdfReader instead of PdfFileReader
    first_page = pdf_reader.pages[0]  # Get the first page

    # Create a PdfWriter object to write the new PDF
    pdf_writer = PyPDF2.PdfWriter()  # Use PdfWriter instead of PdfFileWriter
    pdf_writer.add_page(first_page)  # Add the first page to the writer

    # Open the output PDF file
    with open('Some_BrandNew_Doc.pdf', 'wb') as pdf_output:
        pdf_writer.write(pdf_output)  # Write the content to the new file

# No need to manually close pdf_output; it's handled by the with statement

# Open the PDF file
with open('Working_Business_Proposal.pdf', 'rb') as pdf_file:
    pdf_text = []
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    
    # Loop through all pages and extract text
    for num in range(len(pdf_reader.pages)):  # Use len(pdf_reader.pages)
        page = pdf_reader.pages[num]
        pdf_text.append(page.extract_text())
    
    # Print text from the second page (index 1)
    print(pdf_text[1])  # This will print the text from the second page