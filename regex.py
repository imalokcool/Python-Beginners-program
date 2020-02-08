import re
text = "Hi my name is Alok Kumar"
x = re.search("^Hi.*Kumar$",text)
if (x):
    print("Present")
else:
    print("Absent")