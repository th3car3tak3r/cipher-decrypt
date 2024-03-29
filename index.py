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
'''bigram_count = {}

prev_char = None
for cipher_char in plain_text:
    cipher_char = cipher_char.upper() 
    if prev_char is not None and prev_char.isalpha() and cipher_char.isalpha():
        if prev_char + cipher_char in bigram_count:
            bigram_count[prev_char + cipher_char] += 1
        else:
            bigram_count[prev_char + cipher_char] = 1
    prev_char = cipher_char  '''

print(dict(sorted(char_frequencies.items(), key=lambda item: item[1], reverse=True)))
print(cipher)

plain_text = ""

decode_dict = {
    "a": "E", 
    "p": "O", 
    "u": "N", 
    "h": "A", 
    "b": "T", 
    "z": "O",
    "k": "R"
}

for char in cipher:
    char = char.lower()
    if char.isalpha() and char in decode_dict:
        plain_text += decode_dict[char]
    else:
        plain_text += char


print("-------------------------")
print(plain_text)

#print(cipher.replace("a", "e").replace("p", "o").replace("u", "n").replace("h", "a").replace("b", "s").replace("k", "r"))
'''print(dict(sorted(bigram_count.items(), key=lambda item: item[1], reverse=True)))
print(plain_text.lower().replace("ee","th"))'''

