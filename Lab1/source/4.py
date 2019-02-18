word = input('enter the string:')
long = 1
x = 1
cur_len = 1
dict = {word[0] : 0}

while x < len(word):
     letter = word[x]
     if letter in dict:
        x = dict[letter] + 1
        dict.clear()
        longest = max(long, cur_len)
        cur_len = 0
     else:
        dict[letter] = x
        cur_len = cur_len + 1
        x = x + 1

long = max(long, cur_len)


print('String is:',word[:long],'\nLength is:',long)