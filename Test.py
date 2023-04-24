from PyPDF2 import PdfReader

reader = PdfReader("sample.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[1]
text = page.extract_text()

print(number_of_pages)
print(page)
print(text)