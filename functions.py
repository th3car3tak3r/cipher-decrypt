def calculate_character_frequencies(text, frequency_alphabet):
    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate through each character in the text
    for char in text:
        # Check if the character is already in the dictionary
        if char in char_count:
            # If it is, increment its count by 1
            char_count[char] += 1
        else:
            # If it's not, add it to the dictionary with count 1
            char_count[char] = 1

    #

    # Convert the dictionary to a list of tuples and return it
    return list(char_count.items())