
def encode(string):
    res = ""
    for i in string:
        res += str(len(i)) + "#" + i

    return res

def decode(string):
    res, i = [], 0

    while i < len(string):
        j = i 
        while string[j] != "#":
            j += 1
        length = int(string[i:j])
        res.append(string[j+1:j+length+1])
        i = j + length + 1

    return res


string = ["Jesus","loves","you"]

print(encode(string))
print(decode(string))