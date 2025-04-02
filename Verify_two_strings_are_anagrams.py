# Verify if two given strings are anagrams
# Ignore capitalization and empty spaces
# “cork” and “rock” -> True
# hello hotel -> False


def isAnagram(workingString1, workingString2):
    print("\nVerify if two strings are anagrams [{}] and [{}]".format(workingString1, workingString2))
    # Clear strings from empty spaces
    workingString1 = removeEmptySpacesFromString(workingString1)
    workingString2 = removeEmptySpacesFromString(workingString2)

    if len(workingString1) != len(workingString2):
        print("==> The strings have different lengths so they are not anagrams")
        return False

    # Create a dictionary for the first string
    statistics = {}
    for index in range(len(workingString1)):
        if workingString1[index].lower() in statistics:
            statistics[workingString1[index].lower()] +=  1
        else:
            statistics[workingString1[index].lower()] = 1

    # Go through the second string to check characters from the dictionary
    for index in range(len(workingString2)):
        if workingString2[index].lower() in statistics:
            statistics[workingString2[index].lower()] -= 1
            if statistics[workingString2[index].lower()] < 0:
                print("==> The second string has too many [{}]".format(workingString2[index].lower()))
                return False
        else:
            print("==> The second string has at least one different character: [{}]".format(workingString2[index]))
            return False

    print("==> The strings are anagrams")
    return True

def removeEmptySpacesFromString(stringToVerify):
    return stringToVerify.replace(' ', '')

assert (isAnagram("hellooo", "hotel") == False)
assert (isAnagram("hello", "hotel") == False)
assert (isAnagram("cork", "Rock") == True)
assert (isAnagram("cork", "rocr") == False)
assert (isAnagram("Grey wolf", "glory few") == True)
assert (isAnagram("Eleven plus two", "Twelve plus one") == True)
assert (isAnagram("dormitory", "dirty room") == True)