from PyPDF2 import PdfReader

#Getting The Actual Text
reader = PdfReader("sample_blank2.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[5]
text = page.extract_text()

print(number_of_pages)
#print("Page", page)
temp = text.split('\n')
lines = [line[::-1] for line in temp]
for line in lines:
    print(line)


#Defining Language Stuff
Aleph = "א"
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
print('\n' in text)
Hebrew_Alphabet = {"א"}

def is_english(word):
    for letter in word:
        if letter in english: 
            return True
    return False

#Getting all the citations
all_citations = set()
with open('All_Citations.rtf', 'r') as file:
    large_doc_citation = file.read()
    
for line in large_doc_citation.split('\n'):
    space_index = line.find(' ') 
    if space_index >= 0:
        abbrev = line[0:space_index]
        if not is_english(abbrev):
            abbrev = abbrev[::-1]
            all_citations.add(abbrev)
#Adding English citations 
all_citations.add("Supp")
all_citations.add("P.G")


