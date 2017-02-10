
secret = "lbh zhfg hayrnea jung lbh unir yrnearq"
offset = 13
alphabet = "abcdefghijklmnopqrstuvwxyz"
result = ""

for char in secret:
    if char not in alphabet:
        new_char = char
    else:
        idx = alphabet.find(char)
        new_idx = idx + offset
        if new_idx > 25:
            new_idx = new_idx - 26
        new_char = alphabet[new_idx]

    result += new_char


print result
