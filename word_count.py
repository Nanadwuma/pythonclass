'''text = """
a b c a a b c d c d d d a a 
""" 


#print(text)
#print(text.split())
#print(len(text.upper()))

word_count = {}

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

'''



#Create a dictionary with letters as keys 
# And the count of how many times they appears as an interger.
# Assign each of the word as a key in dictionary and provide 1 as its value.
# Use a function to check if a word is inside a dictionary already
# And count the number of times the words appear in the text.

text = """
It is time to build an economy that is not dependent on charity and handouts. 
But an economy that looks past commodities to position our country in the global market.
We can and we should be able to build a Ghana that looks to her own resources and 
proper management to engineer social and economic growth in our country.
We have a responsibility to make our country attractive for the young generation. 
They should feel they have a worthwhile future if they stay and build their nation. 
There will never be enough aid to develop Ghana to the level we want. 
We’re not disclaiming aid but we do want to discard a mindset of dependency and living on handouts. 
It’s unhealthy both for the giver and the receiver.
We do not want to remain the beggars of the world. We do not want to be dependent on charity.
There’s no pride or dignity in poverty. It is a global agenda that seeks to leave no one behind.
"""

word_count = {}
print(text.split())

for word in text.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)
