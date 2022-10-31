class Solution:
    def romanToInt(self, s: str) -> int:
        number_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        numbers = [number_dict[letter] for letter in s]
        
        i = 0
        while i < len(numbers)-1:
            if numbers[i] == numbers[i+1]:
                numbers[i] += numbers[i+1]
                del numbers[i+1]
            elif numbers[i] > numbers[i+1]:
                if i+2 <= len(numbers)-1 and numbers[i+2] > numbers[i+1]:
                    numbers[i+2] -= numbers[i+1]
                    del numbers[i+1]
                else:
                    numbers[i] += numbers[i+1]
                    del numbers[i+1]
            else:
                numbers[i+1] -= numbers[i]
                del numbers[i]
        
        return numbers[i]
