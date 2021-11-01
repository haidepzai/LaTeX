letters="ABCDEFG"
for idx, letter in enumerate(letters):
    for idy, letter2 in enumerate(letters[idx + 1:]):
        print(idx, letter, idy, letter2)