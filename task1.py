#1. Python Regular Expressions Deep Dive
#Task 1: Email Extraction Enhancement
#Problem Statement: You have a script that extracts email addresses from a text
# but needs to be refined to exclude certain domains (e.g., '[exclude.com](http://exclude.com/)'). 
# Modify the script to extract all email addresses except those from the specified domain.

#Adapt the regex pattern to exclude email addresses from '[exclude.com](http://exclude.com/)'.
#text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
#emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", text)
#print(emails)




import re


text = "user1@domain.com, user2@exclude.com, user@domain.com,"
emails = re.split(r"\b[A-Za-z0-9._%+-]+@+\w[exclude]+\.[A-Z|a-z]{2,}\b", text)
print("Original email list : ")
print(text)
print("New list excluding 'exclude': ")
print(emails)