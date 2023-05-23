# your code goes here!
class Anagram:
    """Class Anagram in anagram.py"""

    def __init__(self, word):
        # Initialize the class with a word
        self.word = word

    def match(self, word_list):
        # Method to find anagrams of the initialized word in a word list
        matches = []  # Store the matching anagrams

        for word in word_list:
            # Iterate through each word in the word list

            # Check if the sorted lowercase version of the current word is equal
            # to the sorted lowercase version of the initialized word.
            # This compares the characters of the words regardless of their case.
            if (
                sorted(word.lower()) == sorted(self.word.lower())
                and word.lower() != self.word.lower()
            ):
                # If the conditions are satisfied, the current word is considered
                # an anagram of the initialized word, so append it to the matches list.
                matches.append(word)

        # Return the list of matching anagrams
        return matches
