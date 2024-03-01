# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 15:43:27 2023

@author: shrik
"""

# 📌🐍 ----------------------------------------------------------------------

from PyPDF2 import  PdfFileReader

from PyPDF2 import PdfReader

reader = PdfReader('C:/1-python/Python NLP/python_tutorial.pdf')
print(len(reader.pages))

page = reader.pages[10]

print(page)