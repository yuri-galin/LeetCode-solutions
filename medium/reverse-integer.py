class Solution:
  """
  Given a signed 32-bit integer x, return x with its digits reversed.
  If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.
  """
  def reverse(self, x: int) -> int:
    # We convert integer to string and reverse it. Then we compare the resulting string with the limits digit by digit
    # to determine if the reversed string lies outside them.
    reversed = str(x)[::-1]
    limit = "2147483647"
    factor = 1
    if x < 0:
      limit = limit[:-1] + "8"
      factor = -1
      reversed = reversed[:-1]

    if len(reversed) == len(limit):
      for i in range(len(reversed)):
        if int(reversed[i]) > int(limit[i]):
          return 0
        elif int(reversed[i]) < int(limit[i]):
          break
          
    return int(reversed) * factor
