import re
pattern = re.compile(r'<book title="(?P<title>.*?)">.*?<author>(?P<author>.*?)</author>.*?<firstPrint>(?P<printed>.*?)</firstPrint>',re.DOTALL)
with open('books.xml','r') as fin:
    with open('result.txt','w') as fout:
        str = fin.read()
        matches = re.findall(pattern,str)
        for match in matches:
            fout.write('Title: ' + match[0] + ' Author: '+ match[1] + ' Published: ' + match[2] +'\n')

