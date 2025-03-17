string = "PAYPALISHIRING"
numRows = 3

def zigzag_conversion(string,numRows):
    if numRows == 1:
        return string
    
    i = 0
    d = 1
    rows = [[]] * numRows
    final_string = ""

    print(rows)
    for c in string:
        rows[i].append(c)
        if i == 0:
            d = 1
        elif i == numRows - 1:
            d = -1

        i += d

    print(rows)

    for x in rows:
        final_string += "".join(x)
    return final_string

print(zigzag_conversion(string,numRows))