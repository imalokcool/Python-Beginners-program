from string import ascii_letters

s= input()
ns=''
for c in s:
    if c in ascii_letters:
            ns=ns+ascii_letters[(ascii_letters.index(c)-1)%len(ascii_letters)]
    else:
        ns+=c
print(ns)