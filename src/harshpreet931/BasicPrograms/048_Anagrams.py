def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

result = are_anagrams("listen", "silent")
print("Are 'listen' and 'silent' anagrams?", result)
