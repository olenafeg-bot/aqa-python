string = input()

unique_chars = set(string)
count = len(unique_chars)
if count > 10:
    print(True)
else:
    print(False)