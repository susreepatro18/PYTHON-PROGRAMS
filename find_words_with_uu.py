def find_words_with_uu(file_path):
    with open(file_path, 'r') as file:
        words = file.readlines()

    words_with_uu = [word.strip() for word in words if 'uu' in word.lower()]
    return words_with_uu


# Path to the sowpods.txt file
file_path = 'sowpods.txt'

words_with_uu = find_words_with_uu(file_path)
for word in words_with_uu:
    print(word)
