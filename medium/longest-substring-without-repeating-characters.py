class Solution:
    """
    Given a string s, find the length of the longest substring without repeating characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We start creating a substring from the start of a string s by adding one letter at a time.
        # We cheack if each new letter already exists within the substring and if so, record the length
        # of the substring into a variable if it's greater than the value of the variable. Then we begin anew,
        # slicing the substring so that it begins after the first encounter of the duplicate letter.
        substr = ""
        length = 0
        for i in range(0, len(s)):
            index = substr.find(s[i])
            if substr.find(s[i]) < 0:
                substr += s[i]
                if len(substr) > length:
                    length = len(substr)
            else:
                if len(substr) > length:
                    length = len(substr)
                substr = substr[index+1:] + s[i]
                    
        return length
