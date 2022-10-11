
# ******************************
# Make your Code
# ******************************
numbers = list(map(int, input().split()))
maxnum = max(numbers)
minnum = min(numbers)
numbers.remove(maxnum)
numbers.remove(minnum)
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)