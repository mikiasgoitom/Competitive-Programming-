def longestCommonPrefix(strs) -> str:
    result = ""
    if not strs:
        return result
    strs = sorted(strs)
    first = strs[0]
    last = strs[-1]
    for i in range (min(len(first), len(last))):
        if not first[i] == last[i]:
            return result
        result += first[i]
    return result
strs = ["ab","a"]
result = longestCommonPrefix(strs)
print("result: " + result)