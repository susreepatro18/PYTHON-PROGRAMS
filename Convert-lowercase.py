def are_anagrams_sorting(s1, s2):
    # Remove spaces and convert to lowercase for case insensitive comparison
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Sort the strings and compare
    return sorted(s1) == sorted(s2)


def are_anagrams_frequency(s1, s2):
    # Remove spaces and convert to lowercase for case insensitive comparison
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # If lengths are different, they can't be anagrams
    if len(s1) != len(s2):
        return False

    # Initialize frequency counters
    freq1 = {}
    freq2 = {}

    # Count frequencies of characters in s1
    for char in s1:
        if char in freq1:
            freq1[char] += 1
        else:
            freq1[char] = 1

    # Count frequencies of characters in s2
    for char in s2:
        if char in freq2:
            freq2[char] += 1
        else:
            freq2[char] = 1

    # Compare frequency counters
    return freq1 == freq2


s1 = "Listen"
s2 = "Silent"
print(are_anagrams_sorting(s1, s2))
print(are_anagrams_frequency(s1, s2))    