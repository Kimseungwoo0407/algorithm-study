word = input()

word2 = set(word.lower())
cnt = [0] * 123
ans = []

for i in word.lower():
    cnt[ord(i)] += 1

for i in word2:
    if cnt[ord(i)] == max(cnt):
        ans.append(i)

if len(ans) == 1:
    print(ans[0].upper())
else:
    print('?')