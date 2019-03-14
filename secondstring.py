
sent = input("Please enter a sentence: ")

splitsent = sent.split()
newSent = []

for i in range(0, len(splitsent), 2):
    word = splitsent[i] 
    newSent.append(word)

finSent = ' '.join(newSent)
print(finSent)


