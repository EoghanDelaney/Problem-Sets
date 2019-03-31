# For this problem I used the python documentation

# Firstly ask the user to input a sentence
sent = input("Please enter a sentence: ")

# The sentence is then split into a list of words
splitsent = sent.split()
# We then declare a new sentence
newSent = []


for i in range(0, len(splitsent), 2): # Now for each number from zero to the quantity of words in the sentence the user inputted, increasing in twos
    word = splitsent[i] # As it loops through select word in the position of i
    newSent.append(word) # Add that word into the new sentence 

finSent = ' '.join(newSent) # Join all these words into a sentence
print(finSent)


