# [html2text]

html2text is a Python script that converts a page of HTML into clean, easy-to-read plain ASCII text. Better yet, that ASCII also happens to be valid Makdown (a text-to-HTML format).

This code is based on Aaron Swartz's html2text.py, which you can find at https://github.com/aaronsw/html2text. Aaron Swartz is a great programmer, and I admire him a lot.

The input is a root dictionary. You need to modify it in the code in this version. The program will recursively find all index.html in the given root dictionary. Then by using Aaron Swartz's html2text.py, I get the plain text and store it in index.txt which has same location with index.html.

One important thing to mention: if you haven't got package chardet installed, you'd better get one. It's easy to install by using pip:

    pip install chardet

Test file is in dictionary test

TODO:
I've found some `UnicodeDecodeError` in practical use. In this version I just ignore the error.
