#pdf merger

import PyPDF2 # install pypdf2 library for pdf operations
files=["1.pdf","2.pdf"]
merger=PyPDF2.PdfMerger()

for pdf in files:
    abc=open(pdf,'rb')
    read=PyPDF2.PdfReader(abc)
    merger.append(read)
abc.close()
merger.write('new.pdf')
