import re
pattern = re.compile(r'(?:<genre>)(?P<genre>.*?)(?:</genre>)',re.DOTALL)
with open('books.xml','r') as fin:
    with open('result.txt','w') as fout:
        str = fin.read()
        matches = re.findall(pattern,str)
        for match in matches:
            fout.write(match + '\n')
