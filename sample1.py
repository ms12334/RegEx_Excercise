import re
pattern = re.compile(r'(?:<publisher>)(?P<pub>.*?)(?:</publisher>)')
with open('books.xml','r') as fin:
    with open('result.txt','w') as fout:
        str = fin.read()
        matches = re.findall(pattern,str)
        for match in matches:
            fout.write(match + '\n')
