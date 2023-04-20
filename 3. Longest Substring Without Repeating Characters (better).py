# Linear time solution, be careful when indexing lists

def longest(s):
    empty = False
    longest = 1

    if s == "":
        empty = True
        return 0

    if not empty:
        letters = []
        for i in s:
            if i not in letters:
                letters.append(i)

            else:
                if len(letters) > longest:
                    longest = len(letters)

                letters = letters[letters.index(i)+1:]

                letters.append(i)

            if len(letters) > longest:
                longest = len(letters)

        return longest

s = "aabaab!bb"
print(longest(s))