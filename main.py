
# ******************************
# Make your Code
# ******************************
numbers =[] 
for i in range(5):
    number = int(input())
    numbers.append(number)

maxnum = max(numbers)
minnum = min(numbers)
numbers.remove(maxnum)
numbers.remove(minnum)
sum = 0
for i in range(len(numbers)):
    sum += numbers[i]
print(sum)