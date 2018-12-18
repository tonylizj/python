input()
nums = input().split(' ')

sum = 0
for i in range(len(nums)):
    sum += int(nums[i])

print(sum)