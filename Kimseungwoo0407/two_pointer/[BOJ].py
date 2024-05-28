string = input()

alphabet = set()

for i in string:
    if i.isalpha():
        alphabet.add(i.lower())

if len(alphabet) == 26:
    print('YES')
else:
    print('NO')