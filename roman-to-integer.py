class Solution:
    """
    Given a roman numeral, method romanToInt() converts it to an integer.
    """
    def romanToInt(self, s: str) -> int:
        # As roman numerals use different letters for different orders of magnitude, you basically need to add up all the roman digits to convert
        # a roman numeral to integer.
        # The problem is the digraphic digits like IV and CD, because if we just add them up as is, we'll get 6 and 600 instead of expected 4 and 400.
        # We could choose to try and divide the roman numeral string into parts, but luckily for us it's uneccessary, as romans used the system
        # where IV equals V minus I and CD equals D minus C, so it all comes down to deciding when to add and when to subtract.
        
        number_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # We get the letters out of the way by converting them to integers right away.
        numbers = [number_dict[letter] for letter in s]
        
        # Next, we compare each integer to the next to see which one is greater. If first one is greater, we add the next one to it,
        # if the next one is greater, we subtract the first one.
        # The special case is when a digraphic digit follows a digit of the greater order of magnitude: MCM equals 1900, but the rules so far will convert it to 2100.
        # So, if the first integer is greater than the next, we need to check for digraphic digits and get rid of them by converting them to a single one.
        # The whole algorithm is as follows.
        i = 0
        while i < len(numbers)-1:
            if numbers[i] > numbers[i+1]:
                if i+2 <= len(numbers)-1 and numbers[i+2] > numbers[i+1]:
                    numbers[i+2] -= numbers[i+1]
                    del numbers[i+1]
            elif numbers[i] >= numbers[i+1]:
                numbers[i] += numbers[i+1]
                del numbers[i+1]
            else:
                numbers[i+1] -= numbers[i]
                del numbers[i]
        
        return numbers[i]
