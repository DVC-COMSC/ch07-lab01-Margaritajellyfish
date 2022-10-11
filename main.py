
# ******************************
# Make your Code
# ******************************
numbers = list(map(int, input().split()))
max_ = max(numbers)
min_ = min(numbers)
numbers.remove(max_)
numbers.remove(min_)
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)