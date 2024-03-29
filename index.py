import json

frequency_file = open("./alphabet_frequency.json")
ciper_file = open("./cipher.txt")

cipher = ciper_file.read()
frequency_alphabet = json.loads(frequency_file.read())


#create character dictionary
char_count = {}

#measure the frequency of alphabet chars in the ciphertext
for cipher_char in cipher:
    char = cipher_char.upper()
    #if cipher_char is alphabet character
    if char in frequency_alphabet:
        if char in char_count:
            # If it is, increment its count by 1
            char_count[char] += 1
        else:
            # If it's not, add it to the dictionary with count 1
            char_count[char] = 1
    else:
        pass

#create character dictionary for frequencies        
char_frequencies = {}

#total number of chars in ciphertext
char_sum = total = sum(char_count.values())


#calculate frequencies
for char in char_count:
    char_frequencies[char] = round((char_count[char] / char_sum) * 100, 4)


def closest_value(data, target):
    # Find the key with the closest numeric value to the target value
    closest_key = min(data, key=lambda x: abs(data[x] - target))
    return closest_key



#### GENERATE NEW RESULT WITH FREQUENCY REPLACEMENTS ####
plain_text = ""

for char in cipher:
    if char.upper() in char_frequencies:
        plain_text = plain_text + closest_value(frequency_alphabet, char_frequencies[char.upper()])
    else:
        plain_text = plain_text + char
        pass


#### CALCULATING BIGRAM FREQUENCIES
bigram_count = {}

prev_char = None
for cipher_char in cipher:
    cipher_char = cipher_char.upper() 
    if prev_char is not None and prev_char.isalpha() and cipher_char.isalpha():
        if prev_char + cipher_char in bigram_count:
            bigram_count[prev_char + cipher_char] += 1
        else:
            bigram_count[prev_char + cipher_char] = 1
    prev_char = cipher_char

print("BIGRAM DICT-----")
print(dict(sorted(bigram_count.items(), key=lambda item: item[1], reverse=True)))

print("ALPHA DICT-----")
print(dict(sorted(frequency_alphabet.items(), key=lambda item: item[1], reverse=True)))
print("CIPHER DICT-----")
print(dict(sorted(char_frequencies.items(), key=lambda item: item[1], reverse=True)))

print("-------------------------")
print("CIPHER")
print(cipher)

plain_text = ""

decode_dict = {
    #BIGRAM
    "h": "T",
    "k": "H",

    #SINGLE
    "b": "O",
    "a": "E",
    "p": "A",
    "c": "R",
    "x": "L",
    "u": "S",
    "g": "Y",
    "i": "M",
    "l": "B",
    "n": "I",
    "z": "F",
    "d": "Q",
    "r": "U",
    "m": "C",
    "j": "N",
    "e": "P",
    "y": "X",
    "o": "G",
    "q": "D",
    "v": "W",
    "t": "Z",
    "s": "K",
    "f": "V"

}

for char in cipher:
    char = char.lower()
    if char.isalpha() and char in decode_dict:
        if char.isupper:
            plain_text += decode_dict[char]
        else:
            plain_text += decode_dict[char].lower()
    else:
        plain_text += char


print("-------------------------")
print("PLAINTEXT")
print(plain_text)


