from PyPDF2 import PdfReader

reader = PdfReader("sample_blank2.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[5]
text = page.extract_text()

print(number_of_pages)
#print("Page", page)
temp = text.split('\n')
lines = [line[::-1] for line in temp]
#print(lines[3])

for line in lines:
    print(line)


Aleph = "א"
print('\n' in text)
Hebrew_Alphabet = {"א"}