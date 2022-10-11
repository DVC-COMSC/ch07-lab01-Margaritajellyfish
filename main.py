
# ******************************
# Make your Code
# ******************************
numbers = list(map(int, input().split()))
numbers.remove(max)
numbers.remove(min)
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)