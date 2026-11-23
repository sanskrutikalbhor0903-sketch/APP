#email address and mobile number pattern code:
import re 
text="""Welcome to the lab towards too abcto
hi i am abc
contact me on abc@gmail.com
you can contact me on my mob number 6006243234
hi i am xyz
contact me on xyz@gmail.com
you can contact me on my mob number 9008765432
"""
pattern=r'\b[A-Za-z0-9._-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
pattern2=r'\b[6-9][0-9]{9}\b'
p=re.findall(pattern,text)
p1=re.findall(pattern2,text)
print(p)
print(p1)