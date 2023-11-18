import sys
g = ""
b = ""
for letter in sys.argv[1]:
    if (letter.lower() == "A".lower()):
        g += "A"
        b += "00"
    if (letter.lower() == "G".lower()):
        g += "G"
        b += "01"
    if (letter.lower() == "T".lower()):
        g += "T"
        b += "10"
    if (letter.lower() == "C".lower()):
        g += "C"
        b += "11"

print(c)
print(b)
print("reference:https://genome.ucsc.edu/cgi-bin/hgBlat")