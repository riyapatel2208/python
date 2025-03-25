#replace word

import sys

if len(sys.argv) < 4:
    print("use: python Pr10U2.py gujarat.txt Gujarat Gujrat")
    sys.exit(1)

old_word = sys.argv[2]
new_word = sys.argv[3]

with open(sys.argv[1],'r') as file:
    txt = file.read()

txt_display = txt.replace(old_word,new_word)

with open(sys.argv[1],'w') as file:
    file.write(txt_display)

print(txt_display)