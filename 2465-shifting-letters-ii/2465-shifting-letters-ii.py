class Solution(object):
    def shiftingLetters(self, s, shifts):
        
        n = len(s)
        shift_array = [0] * (n + 1)  

        for start, end, direction in shifts:
            shift_value = 1 if direction == 1 else -1
            shift_array[start] += shift_value
            shift_array[end + 1] -= shift_value  

        for i in range(1, n):
            shift_array[i] += shift_array[i - 1]
        
        result = []
        for i, char in enumerate(s):
            net_shift = shift_array[i] % 26
            new_char = chr((ord(char) - ord('a') + net_shift) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)