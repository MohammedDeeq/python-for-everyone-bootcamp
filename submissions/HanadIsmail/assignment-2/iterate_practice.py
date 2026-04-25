

## Assignment 5: Iterate and slice (for + range + enumerate)

nums = list (range(10))
print("step 2 ",nums[::2])

print("Reversed" , nums[::-1])

for i in range(3,8):
    print(i)

for i , num in enumerate(nums):
    print(i , ": ", num)

dic = ({"name": "abdi" , "team": "barcelona"})

for k, v in dic.items():
    print(k,v)
