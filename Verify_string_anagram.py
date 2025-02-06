# Verify if two given strings are anagrams
# Ignore capitalization
# “cork” and “rock” -> True
# hello an hotel -> False



def isAnagram(string1, string2):
    print("\nVerify if two strings are anagrams [{}] and [{}]".format(string1, string2))
    if len(string1) != len(string2):
        print("==> The strings have different lengths so they are not anagrams")
        return False
    # Create a dictionary for the first string
    statistics = {}
    for index in range(len(string1)):
        if string1[index].lower() in statistics:
            statistics[string1[index].lower()] +=  1
        else:
            statistics[string1[index].lower()] = 1

    # Go through the second string to check characters from the dictionary
    for index in range(len(string2)):
        if string2[index].lower() in statistics:
            statistics[string2[index].lower()] -= 1
            if statistics[string2[index].lower()] < 0:
                print("==> The second string has too many [{}]".format(string2[index].lower()))
                return False
        else:
            print("==> The second string has at least one different character: [{}]".format(string2[index]))
            return False

    print("==> The strings are anagrams")
    return True

assert (isAnagram("hellooo", "hotel") == False)
assert (isAnagram("hello", "hotel") == False)
assert (isAnagram("cork", "Rock") == True)
assert (isAnagram("cork", "rocr") == False)