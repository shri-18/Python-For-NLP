# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:20:56 2023

@author: shrik
"""

# 📌🐍 ----------------------------------------------------------------------
import re
text = ''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern = r'\d\d\d\d\d\d\d\d\d\d'

matches = re.findall(pattern,text )

print(matches)

# 📌🐍 ----------------------------------------------------------------------
import re
text = ''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern = r'\d{10}'

matches = re.findall(pattern,text )

print(matches)
# 📌🐍 ----------------------------------------------------------------------

import re
text = ''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern1 = r'\W\d{3}\W-\d{3}-\d{4}'        # \W for special charecter

pattern2 = r'\(\d{3}\)-\d{3}-\d{4}'        #for specific special char
matches1 = re.findall(pattern1,text )
matches2 = re.findall(pattern2,text )
print(matches1)
print(matches2)
#o/p
#['(999)-333-7777']
#['(999)-333-7777']

# 📌🐍 ----------------------------------------------------------------------
#for the both us and indian cell phone num
"\(\d{3}\)-\d{3}-\d{4}|\d{10}"

import re
text = ''' Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion'''

pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches = re.findall(pattern,text )

print(matches)
#o/p
#['9991116666', '(999)-333-7777']

# 📌🐍 ----------------------------------------------------------------------

import re 
text = '''A protracted; legal battle; over a 32-carat;
 Golconda diamond-'''
 
pattern = r'[^;-]'        #  ^ id except operator (except ;-)

matches = re.findall(pattern,text)
print(matches)
'''
output = 
['A', ' ', 'p', 'r', 'o', 't', 'r', 'a', 'c', 't', 'e', 'd', ' ', 'l', 'e', 'g', 'a', 'l', ' ', 'b', 'a', 't', 't', 'l', 'e', ' ', 'o', 'v', 'e', 'r', ' ', 'a', ' ', '3', '2', 'c', 'a', 'r', 'a', 't', '\n', ' ', 'G
'''
# 📌🐍 ----------------------------------------------------------------------

'Note \d[^\n]+'

#for extracting the line strats with 'Note 1'


import re 
text = '''Note 1 – Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.'''
 
pattern = r'Note \d[^\n]+'        
#when u want only one line not next line for that we use [^\n]
matches = re.findall(pattern,text)
print(matches)
#o/p
#['Note 1 – Summary of Significant Accounting Policies']

# 📌🐍 ----------------------------------------------------------------------



import re 
text = '''Note 1 – Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.'''
 
pattern = r'Note \d \W([^\n]+)'        
#when u want only one line not next line for that we use [^\n]
matches = re.findall(pattern,text)
print(matches)
#o/p 
#[' Summary of Significant Accounting Policies']

# 📌🐍 ----------------------------------------------------------------------
import re 
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
 
pattern = r"(FY\d{4} Q\d)"
#when u want only one line not next line for that we use [^\n]
matches = re.findall(pattern,text)
print(matches)
#o/p
#['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

# 📌🐍 ----------------------------------------------------------------------

import re 
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''
 
pattern = r"(FY\d{4} Q[1-4])"
#when u want only one line not next line for that we use [^\n]
matches = re.findall(pattern,text)
print(matches)

#o/p 
#['FY2021 Q1', 'FY2020 Q4', 'FY2021 Q1', 'FY2020 Q4']

# 📌🐍 ----------------------------------------------------------------------

import re 
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.'''

pattern = "FY\d{4} Q[1-4]|fy\d{4} Q[1-4]"

matches = re.findall(pattern,text, re.IGNORECASE)
print(matches)

# 📌🐍 ----------------------------------------------------------------------

import re 
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''

pattern = r'\d{4} Q[1]'

matches = re.findall(pattern, text)
print(matches)

# 📌🐍 ----------------------------------------------------------------------
#\$[0-9\.]+
import re 
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''

pattern = r'\$[0-9\.]+'

matches = re.findall(pattern, text)
print(matches)

# 📌🐍 ----------------------------------------------------------------------
#
import re 
text = '''The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.'''

pattern = r'\$([0-9\.]+)'

matches = re.findall(pattern, text)
print(matches)
# 📌🐍 ----------------------------------------------------------------------

import re

text = 'hi i have a problem with my order number 412888912'

pattern = r'order[^\d]*(\d+)'

matches = re.findall(pattern,text , re.IGNORECASE)
print(matches)

# 📌🐍 ----------------------------------------------------------------------


import re

text = 'hi with my order 412888912 i have a problem'

pattern = r'order[^\d]*(\d+)'


matches = re.findall(pattern,text , re.IGNORECASE)
print(matches)

# 📌🐍 ----------------------------------------------------------------------


import re

text = 'hi with my order #412888912 i have a problem'
pattern = r'order[^\d]*(\d+)'

matches = re.findall(pattern,text , re.IGNORECASE)
print(matches)

# 📌🐍 ----------------------------------------------------------------------

import re
def get_pattern_match(pattern , text):
    matches = re.findall(pattern, text)
    if matches :
        return matches[0]
    

pattern = r'order[^\d]*(\d+)'
text = 'hi with my order #412888912 i have a problem'

print(get_pattern_match(pattern , text))

# 📌🐍 ----------------------------------------------------------------------


import re

text = 'hi i have a problem with my order number 412888912 and email is shrikantilhe87@gmail.com and shrikantilhecomp@sanjivanicoe.org.in'
pattern = r'\w+@\w+.com|\w+@\w+.org.in|\w+@\w+.in'

matches = re.findall(pattern,text , re.IGNORECASE)
print(matches)

# 📌🐍 ----------------------------------------------------------------------

import re
text = '''Born: 28 June 1971 (age 52 years), Pretoria, South Africa
Net worth: 22,340 crores USD (2023) Forbes
Children: Vivian Jenna Wilson, Nevada Alexander Musk, Griffin Musk, Damian Musk, Kai Musk, Saxon Musk
Spouse: Talulah Riley (m. 2013–2016), Talulah Riley (m. 2010–2012), Justine Musk (m. 2000–2008)
Full name: Elon Reeve Musk'''

def get_pattern_match(pattern , text):
    matches = re.findall(pattern, text)
    if matches :
        return matches[0]
    

print(get_pattern_match('age \d+', text))
print(get_pattern_match('Born\: \d+ \w+ \d+', text))
print(get_pattern_match('name: (.*)', text))
print(get_pattern_match('Born: (\d+ \w+ \d+)', text))

# 📌🐍 ----------------------------------------------------------------------

import re
text = '''Dhirubhai Ambani was one of the sons of Hirachand Gordhanbhai Ambani, a village school teacher belonging to the Modh vaniya (Baniya) community and Jamnaben Ambani and was born in Chorwad, Malia Taluka, Junagadh district, Gujarat[11] on 28 December 1932.[12] He did his studies from Bahadur Khanji school. He left Aden in 1958 to try his hand at his own business in India in the textiles market. It is also said that he has worked at Petrol pump as a petrol vendor'''

def get_pattern_match(pattern , text):
    matches = re.findall(pattern, text)
    if matches :
        return matches[0]
    

print(get_pattern_match('age \d+', text))
print(get_pattern_match('Born\: \d+ \w+ \d+', text))
print(get_pattern_match('name: (.*)', text))
print(get_pattern_match('Born: (\d+ \w+ \d+)', text))

# 📌🐍 ----------------------------------------------------------------------

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












































































































































































































































































































































































































































































































































































































+