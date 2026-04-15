a_string = "AnTonIus"
lowercase = a_string.lower()
total = 0
for x in "aiueo":
    jml = lowercase.count(x)
    total += jml
print(total) #output4

a_string = "Gabriel NKS"
lowercase = a_string.lower()
for x in "aiueo":
    jml = lowercase.count(x)
    total += jml
print(total)
