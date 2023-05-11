from PyPDF2 import PdfReader

#note: when printing Hebrew words, they will appear backwards. 
#Leave them like this

def get_words(file_name): 
    """
    Converts a PDF Document into an ordered list of Hebrew
    words that are found on the page.
    """
    reader = PdfReader(file_name)
    total_list = []
    for page in reader.pages:
        lines = [line for line in page.extract_text().split('\n')] #list of string lines
        for line in lines:
            for word in line.split(' '): #
                if len(word) > 0:
                    total_list.append(word)
    return total_list

def find_all(word_list, target_word, exact_match = True):
    """
    Finds all instances of a word in the word_list. Exact_match 
    determines if we're searching for an exact copy or a word 
    that contains this target_word. 
    """
    all_instances = []
    for index, word in enumerate(word_list):
        if exact_match and word == target_word:
            all_instances.append((index, word))
        elif (not exact_match) and target_word in word:
            all_instances.append((index, word))
    return all_instances

#Defining Language Stuff
english = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
Hebrew_Alphabet = "אבבּגדהוזחטיככלמנסעפצקרשתןםךףץ"

def is_english(word):
    for letter in word:
        if letter in english: 
            return True
    return False

def get_all_citations():
    """
    Gets all of the citations from the 
    All_Citations.rtf file. Returns a set
    of Hebrew words
    """
    all_citations = set()

    with open('All_Citations.rtf', 'r') as file:
        large_doc_citation = file.read()

    for line in large_doc_citation.split('\n'):
        #print(line, line.find('–'))
        dash = line.find('–')
        if dash == -1:
            dash = line.find('-')
        if dash >= 0:
            abbrev = line[0:dash]
            if not is_english(abbrev):
                abbrev = abbrev.strip()
                all_citations.add(abbrev)
        else:
            print(line)

    #Adding English citations (in reverse b/c English ir processed backwards)
    all_citations.add("Supp") 
    all_citations.add("P.G")
    return all_citations

def get_all_locations(file_name):
    word_list = get_words(file_name)
    all_citations = get_all_citations()
    print("here")
    for cit in all_citations:
        show_citation = cit[::-1]
        all_instances = find_all(word_list, cit, False)
        if len(all_instances) > 0:
            print(show_citation, all_instances)
    return

get_all_locations("sample_blank.pdf")