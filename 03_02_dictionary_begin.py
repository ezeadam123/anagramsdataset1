#!/usr/bin/env python
# coding: utf-8

# In[20]:


#file opening format:
# word = open(filename, node)

#OPENING DATA FILE
word = open('words', 'r')

#READING LINES IN DATA FILE
wordlist = word.readlines()

print(wordlist[10000:10005])

print("The amount of words in our data set: " + str(len(wordlist)) + " words.")


#i is the ELEMENT, v is the VALUE

#wordclean = []
#for i in wordlist:
#    if i != 1:   
#        i.strip().lower()
#        wordclean.update(i)
    
    
#using a for loop to clean out the list

wordclean = [i.strip().lower() for i in wordlist]
print(wordclean[:10])


wordunique = list(set(wordclean))
print(wordunique[:10])

wordunique.sort()
print(wordunique[:15])


# In[ ]:


strip_aaron = 'Aaron\n'.strip()
print(strip_aaron)

lower_aaron = strip_aaron.lower()
print(lower_aaron)


# In[34]:


word = open('words', 'r')


wordclean = [i.strip().lower() for i in word]
print(wordclean[:10])

wordunique = list(set(wordclean))
print(wordunique[:10])

print("                       ------------------Random set of words in the Dictionary--------------------\n")
wordunique.sort()
print(wordunique[50 : 80])


# In[35]:


word = open('words', 'r')


wordclean = sorted(list(set([i.strip().lower() for i in word])))

print(wordclean[800:815])


# In[40]:




print(sorted('lines'))

#anagrams

print(sorted('lines') == sorted('eilns')) #if this prints true, then these TWO SORTS ARE ANAGRAMS!

print(sorted('lines') == sorted('miles')) #not an ANAGRAM


# In[60]:


def sortedversion(word):
    return ''.join(sorted(word))

print(sortedversion('maggrant'))

if sortedversion('maggrant') == sortedversion('aaggmnrt'):
    print("these nutz")




# In[62]:


#example of join method
':'.join(['a', 'b', 'c'])


# In[66]:


def anagram(word):
    
    return''.join(sorted(word))

print(anagram('maybe'))

def conditional():
    if anagram('maybe') == anagram('abemy'):
        print("Is an anagram!")
        
conditional()


# In[1]:


def sortedversion(word):
    return ''.join(sorted(word))

sortedversion('lives')
print(sortedversion('lives'))

word = open('words', 'r')
wordclean = sorted(list(set([i.strip().lower() for i in word])))

#for i in wordclean
#    if sortedversion(i) == sortedversion(myword):
#        return i

                        # ALGORITHM IN PSUEDEOCODE
#i = book 
#if sortedversion('book') == sortedversion('listen') then return i
#so if 'bkoo' == 'eilnst'
#return book

def anagram(myword):
    
    return [i for i in wordclean if sortedversion(i) == sortedversion(myword)]


# In[12]:


anagram('silent')
get_ipython().run_line_magic('timeit', "anagram('dictionary')")


# In[15]:


words_bysig = {}


for i in wordclean:
    print(i)
    words_bysig[sortedversion(i)].append(i)
    

    


# In[ ]:


import collections 

