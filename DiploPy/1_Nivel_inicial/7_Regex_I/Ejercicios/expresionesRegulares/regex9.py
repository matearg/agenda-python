import re
patron1 = re.compile(r'((?P<name>ap8)(?(name)9|))')

mail = 'ap89 ap8 rp8 rp4 w'
print(patron1.search(mail))
"""
patron2 = re.compile(r'(<)?(\w+@\w+(?i:\.\w+)+)(?(1)>|$)')
mail1 = "<user@host.com>"
mail2 = "user@host.com"
mail3 = "<user@Host.com"
mail4 = "user@host.com>"
print(patron2.search(mail1))
print(patron2.search(mail2))
print(patron2.search(mail3))
print(patron2.search(mail4))
print("----------------------------------------------")
print(patron2.match(mail1))
print(patron2.match(mail2))
print(patron2.match(mail3))
print(patron2.match(mail4))"""
print("###########################################")
patron3 = re.compile(r'(<)?(\w+@\w+(?i:\.\w+)+)(?(1)>|$)')
mail1 = "<user@host.com>"
mail2 = "user@host.com"
mail3 = "user@Host.com"
mail4 = "user@host.com>"

print(patron3.search(mail1))
print(patron3.search(mail2))
print(patron3.search(mail3))
print(patron3.search(mail4)) 
print("----------------------------------------------")
print(patron3.match(mail1))
print(patron3.match(mail2))
print(patron3.match(mail3))
print(patron3.match(mail4))
