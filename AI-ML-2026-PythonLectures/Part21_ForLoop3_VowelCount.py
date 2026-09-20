word = "artificial"
count = 0

print("==============Approach1==================")
for ch in word:
    if ch in 'aeiou':
        count += 1
print("Total count of vowels:", count)

print("==============Approach2==================")
word2 = "artificial"
count2 = 0
for ch in word2:
    if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'):
        count2 += 1
print("Total count of vowels:", count2)