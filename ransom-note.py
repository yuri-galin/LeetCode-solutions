class Solution:
    """
    Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

    Each letter in magazine can only be used once in ransomNote.
    """
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # We iterate over each letter in ransomNote, search for it in magazine and if we find it, we cut it out, moving onto the next letter.
        # If we don't find it, we return False.
        for letter in ransomNote:
            index = magazine.find(letter)
            if index < 0:
                return False
            
            magazine = magazine[:index] + magazine[index + 1:]
        return True
