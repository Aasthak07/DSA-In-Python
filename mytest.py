freq = [(0, chr(i + ord('a'))) for i in range(26)]
print(freq)
s=input("enter the string: ")
for ch in s:
        index = ord(ch) - ord('a')
        freq[index] = (freq[index][0] + 1, ch)