def longestCommonPrefix(arr1, arr2) -> int:
    def generate_prefixes(num):
        s = str(num)
        return [s[:i+1] for i in range(len(s))]
    prefix_set = set()
    for a in arr1:
        prefix_set.update(generate_prefixes(a))
    max_len = 0
    for b in arr2:
        prefixes = generate_prefixes(b)
        for prefix in prefixes:
            if prefix in prefix_set:
                max_len = max(max_len, len(prefix))
    return max_len
arr1 = [1, 10, 100]
arr2 = [1000]

r = longestCommonPrefix(arr1, arr2)
print(r)