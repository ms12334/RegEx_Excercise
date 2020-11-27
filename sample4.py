import re
with open('books.xml','r') as fin:
    with open('books_updated.xml','w') as fout:
        str = fin.read()
        str = re.sub('(?s)<genre>(?P<genre>.*?)</genre>','\g<genre> - updated',str)
        fout.write(str)

