def count_vowels_consonants(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

vowels, consonants = count_vowels_consonants("Hello, World!")
print("Vowels:", vowels)
print("Consonants:", consonants)
