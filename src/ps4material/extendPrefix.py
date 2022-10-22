# CSCI1100 Gateway to Computer Science
#
# Some code tools that might be useful in solving
# PS4: A Statistical Model of English Text

# addToModel : prefix * letter * dictionary -> dictionary
#
# Having seen prefix, we find letter following. Add this information
# to the dictionary.
#
def addToModel(prefix, letter, dictionary):
    if prefix in dictionary:
        dictionary[prefix].append(letter)
    else:
        dictionary[prefix] = [letter]
    return dictionary

# extendPrefix : prefix * letter * degree -> prefix
#
# prefix starts off empty "" and grows to length degree as we
# encounter letters.
#
def extendPrefix(prefix, letter, degree):
    if len(prefix) < degree:
        return prefix + letter
    else:
        return prefix[1:] + letter
