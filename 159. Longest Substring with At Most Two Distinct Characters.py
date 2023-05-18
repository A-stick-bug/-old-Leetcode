from collections import defaultdict

def longest_distinct(s):
    start = end = 0
    window = defaultdict(int)
    res = 0
    while end < len(s):
        window[s[end]] = end
        end += 1
        if len(window) > 2:
            delete = min(window.values())
            window.pop(s[delete])
            start = delete + 1
        res = max(res,end-start+1)

    return res


print(longest_distinct("ccaabbb"))