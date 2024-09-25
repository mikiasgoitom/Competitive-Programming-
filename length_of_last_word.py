def lengthOfLastWord(s: str) -> int:
        l = s.split()
        print(l)
        return(len(l[-1]))
s = "   fly me   to   the moon  "
i = lengthOfLastWord(s)
print(i)