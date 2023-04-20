# know when to use for/while loops, for this question, while loop is much better
# try to make code not break on edge cases
# use while loop to keep 2 pointers in range

def longestPalindrome(s: str) -> str:
    longest = 1
    out = ""
    if len(s) == 0:
        return out

    out = s[0]

    for i in range(len(s)):
        start, end = i, i

        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > longest:
                out = s[start:end + 1]
                longest = end - start + 1
            start -= 1
            end += 1

        start = i
        end = i + 1
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > longest:
                out = s[start:end + 1]
                longest = end - start + 1
            start -= 1
            end += 1
    return out


s = ""
print(longestPalindrome(s))
