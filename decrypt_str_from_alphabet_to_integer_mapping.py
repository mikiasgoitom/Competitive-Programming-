def freqAlphabets(s: str) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # nums = s.split('#')
    letterArr = []
    # for i in range(len(nums)):
    #     letterArr.append(alphabet[int(nums[i])])
    i = 0
    j = 1
    while i < len(s):
        if j + 1 < len(s) and s[j + 1] == '#': 
            letterArr.append(alphabet[int(s[i]+s[j]) -1])
            i+=3
            j+=3
        elif j + 2 < len(s) and s[j + 2] == '#':
            letterArr.append(alphabet[int(s[i]) - 1])
            letterArr.append(alphabet[int(s[j]+s[j+1]) -1])
            i+=4
            j+=4
        else:
            letterArr.append(alphabet[int(s[i]) - 1])
            if j < len(s):
                letterArr.append(alphabet[int(s[j]) - 1])
                j+=2      
            i+=2
    letters = ''.join(letterArr)
    return letters
# str = "1226#"
str = "26#11#418#5"
nums = freqAlphabets(str)
# nums = str.split('#')
print(nums)