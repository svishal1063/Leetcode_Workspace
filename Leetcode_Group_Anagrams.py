from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

result_dict = defaultdict(list)                 # We create a dictionary with contains list as as value.


for word in strs:
    count = [0] * 26                           ## We create a dummy list that would hold the value (0/1) corresponding to each alphabet from a-z
    
    for char in word:                          ## We give the character a value within (0-25 i.e 26 chars in English) by subtracting the ASCII value of char with the   
        count[ord(char)-ord("a")]+=1           ## ASCII value of char "a"

    result_dict[tuple(count)].append(word)     ## We add the "count" list to the dictionary as the key, converting it into a tuple as we can't have a list as a key 
                                               ## Then, we append the word that has the same character count to the "Count" key's value which is actually a list. 

print(list(result_dict.values()))              ## We print the values of result_dict alone which would return all the words that are anagrams as groups.
