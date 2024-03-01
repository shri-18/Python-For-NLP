# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:24:16 2023

@author: shrik
"""
# 📌🐍 ----------------------------------------------------------------------
#remove special char
import re

def remove_special_char():
    pattern = '[^+-@?#$!*\s]+'
    return pattern

text = 'welcome ! to the ? new year 2023 **# xxxx'

matches = re.findall(remove_special_char(),text)
matches
for i in range(len(matches)):
    print(matches[i], end=' ')

# 📌🐍 ----------------------------------------------------------------------
#remove numbers
import re
text = '''123 jhsdjhs398r897b239847b73sdfd'''
pattern = '[a-zA-Z.,!?/:;\"\'/s]+'

matche = re.findall(pattern, text)
print(matche)
# 📌🐍 ----------------------------------------------------------------------

import re

text = 'hello i am harry potter'
x = re.split('.,!?/:;\"\'\s ', text)
print(x)

# 📌🐍 ----------------------------------------------------------------------
#remove punctuation mark

import string
import re
def remove_punc(text):
    text = ''.join([c for c in text if c not in string.punctuation])
    return text

x = remove_punc('Articles: @first sentense of some, {important} articles having lot of ~ punctuation and another one;!')
print(x)

# 📌🐍 ----------------------------------------------------------------------
'''------------------------------#stemming---------------------------------'''

import nltk
def get_stem(text):
    stemmer = nltk.porter.PorterStemmer()
    text = ' '.join([stemmer.stem(word) for word in text.split()])
    return text

x = get_stem('we are eating and swimming ; we have eating and swimming; he eats an=nd swimd=s ; he ate and swim')
print(x)

# 📌🐍 ----------------------------------------------------------------------
import re

txt = 'asdf fghj; afdh, fjeh,asdf,foo'
re.split(r'(?:,\;/\s)\s', txt)

pattern = r'(?:,\;/\s)\s'
x = re.findall(pattern, )
print(x)

# 📌🐍 ----------------------------------------------------------------------
filename = 'spam.txt'
filename.endswith('.txt')

# 📌🐍 ----------------------------------------------------------------------
choices = ('http:','ftp:')
url = 'http://wwww.python.org'
url.startswith(choices)
# 📌🐍 ----------------------------------------------------------------------
s = 'ABSIUGSD'
print(s[-7:-2])

print(s[2:7:2])

# 📌🐍 ----------------------------------------------------------------------
url = 'http://www.python.org'
url[:5] == 'http:' or url[:6] == 'https' or url[:4] == 'ftp' 


# 📌🐍 ----------------------------------------------------------------------
from fnmatch import fnmatchcase, fnmatch
names = ['dot1.csv','dot2.csv','config.ini','foo.py']
[name for name in names if fnmatch(name,'dot1.csv')]


# 📌🐍 ----------------------------------------------------------------------
#.match method
import re
text1 = '18/02/2003'

if re.match(r'\d+/\d+/\d+',text1):
    print("Yes")
else:
    print('No')    
# 📌🐍 ----------------------------------------------------------------------

import re
d = re.compile(r'(\d+)/(\d+)/(\d+)')
text1 = '18/02/2003'

if re.match(d, text1):
    print('yes')
else:
    print('no')    
# 📌🐍 ----------------------------------------------------------------------
import re
data = 'yeah, but no, but yeah, but no, but yes'
x = data.replace('yeah', 'yepp')
print(x)
# 📌🐍 ----------------------------------------------------------------------
import re

data = 'python , PyTHon Advance, pythON ,pyth, mixed python'
x = re.findall('python', data, flags= re.IGNORECASE)
print(x)

# 📌🐍 ----------------------------------------------------------------------
import re

data = 'python , PyTHon Advance, pythON ,pyth, mixed python'
x = re.sub('python', 'snake',data, flags=re.IGNORECASE)

print(x)

# 📌🐍 ----------------------------------------------------------------------
import re

def matchcase(word):
    def replace(m):
        text = m.group()
        #print(m)
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace    
data = 'python , PyTHon Advance, pythON ,pyth, mixed python'

text3 = re.sub('python', matchcase('snake'),data, flags=re.IGNORECASE)
print(text3)
# 📌🐍 ----------------------------------------------------------------------

import re
d = re.compile(r'\"(.*)\"')
t = 'computer says no'
x = re.findall(d,t)
x





    