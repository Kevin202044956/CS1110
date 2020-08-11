import urllib.request
from string import punctuation

print('Type text; enter a blank line to end.')
phrase = urllib.request.urlopen('http://cs1110.cs.virginia.edu/files/words.txt')
data_list = []
for line in phrase:
    decoded_line = line.strip().decode('utf-8')
    cells = decoded_line.strip()
    data_list.append(cells)

while True:
    context = input()
    if context == '':
        break
    context_phrase = context.split()
    for phrase in context_phrase:
        phrase = phrase.strip(punctuation)
        new_phrase = phrase.lower()
        if phrase not in data_list and new_phrase not in data_list:
            print("  MISSPELLED:", phrase)