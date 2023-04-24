from PyPDF2 import PdfReader

#Getting The Actual Text



def format_text(file_name): #returns a bunch of fixed (reverse Hebrew reversal) pages
    reader = PdfReader(file_name)
   # number_of_pages = len(reader.pages)
    for page in reader.pages:
        total_list = []
        lines = [line[::-1] for line in temp]
        yield [word[::-1] for word in page.extract_text().split(' ')]
   # number_of_pages = len(reader.pages)
   # page = reader.pages[14]
  #  text = page.extract_text()

full_text = format_text("sample_blank.pdf")
print("here!")
for p in full_text:
    print(p)
    break
#print(number_of_pages)
#print("Page", page)
#temp = text.split('\n')
#lines = [line[::-1] for line in temp]
#full_text = ""
#for line in lines:
#    full_text += line

##print(full_text)

#Defining Language Stuff
Aleph = "א"
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
#print('\n' in text)
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
    dash = line.find('–') 
    if dash >= 0:
        abbrev = line[0:dash]
        if not is_english(abbrev):
            abbrev = abbrev[::-1].strip()
            all_citations.add(abbrev)

#Adding English citations (in reverse b/c English ir processed backwards)
all_citations.add("ppuS") 
all_citations.add("G.P")

#print(all_citations)


def get_all_locations(all_pages):
    #Scanning the Text Document

    for num, page in enumerate(all_pages):
        text = page.extract_text()
        for cit in all_citations:
            if cit in text:
                print("here", num+1, cit)
                loc = text.find(cit)
                print(text[loc-5:loc+5])

        break
    return

#get_all_locations()