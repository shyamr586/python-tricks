# if a text has multiple delimiters such as , or ; or white spaces, use the following code to 
# split multiple delimiters
import re

text = "aaa bbbb;cccc,ddddd\teeeee     fffff"
newtext = re.split(r'[;,\s]\s*', text)
print (newtext)