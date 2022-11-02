class Solution:
    """
    Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
    
    The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8,
    and -2.7335 would be truncated to -2.
    
    Return the quotient after dividing dividend by divisor.
    
    Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1].
    For this problem, if the quotient is strictly greater than 2^31 - 1, then return 2^31 - 1, and if the quotient is strictly less than -2^31,
    then return -2^31.
    """
    def divide(self, dividend: int, divisor: int) -> int:
        # As division/multiplication are unavailable to us, we have to use addition/subtraction.
        # We could add/subtract the divisor iteration after iteration without change, but that would take ages when we get to greater numbers.
        # We can significantly speed up the process by using arithmetic progression: each iteration we add up divisors.
        is_neg = False
        if (dividend < 0) ^ (divisor < 0):
            is_neg = True
            
        dividend = abs(dividend)
        divisor = abs(divisor)
  
        quotient = 0
        while divisor <= dividend:
            decrement = divisor
            count = 1
            while decrement <= dividend:
                dividend -= decrement
                decrement += decrement
                quotient += count
                count += count
  
        if is_neg:
            quotient = -quotient

        return max(min(quotient, 2**31 - 1), -2**31)
