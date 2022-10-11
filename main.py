
# ******************************
# Make your Code
# ******************************
numbers = list(map(int, input().split()))
max = numbers.max()
min = numbers.min()
numbers.remove(max)
numbers.remove(min)
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)
