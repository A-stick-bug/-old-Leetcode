# know when to use for/while loops, for this question, while loop is much better
# try to make code not break on edge cases
# use while loop to keep 2 pointers in range

def longestPalindrome(s: str) -> str:
    longest = 1
    out = s[0]
    for i in range(len(s)):  # for every index (and pair of indices)

        start = end = i  # center is one element
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > longest:
                out = s[start:end + 1]
                longest = end - start + 1
            start -= 1
            end += 1

        start, end = i, i + 1  # center is 2 elements
        while start >= 0 and end < len(s) and s[start] == s[end]:
            if end - start + 1 > longest:
                out = s[start:end + 1]
                longest = end - start + 1
            start -= 1
            end += 1
    return out


s = ""
print(longestPalindrome(s))
