## Anagram is a word or a phrase that's formed by the re-arranging of the original word
## with the same letters appearing only once.

s = "a"
t = "ab"
if len(s) != len(t):
    print(False)
    exit()
else:
    char_list = [x for x in s]
    for x in t:
        if x in char_list:
            char_list.remove(x)

if len(char_list)==0:
    print("True")
else:
    print("False")

        
