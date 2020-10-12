import re
pattern = re.compile(r'(?:<publiser>)(?P<pub>.*?)(?:</publisher>)')
with open('books.xml','r') as fin:
    with open('result.txt','w') as fout:
        str = fin.read()
        results = re.findall(pattern,str)
        for result in results:
            fout.write(result + '\n')
