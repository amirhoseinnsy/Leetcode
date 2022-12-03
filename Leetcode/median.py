# getting list
nums1 = [0, 0, 0, 0, 0]
nums2 = [-1, 0, 0, 0, 0, 0, 1]
nums3 = []

# merge lists
for i in nums2:
    nums3.append(i)
for i in nums1:
    nums3.append(i)

# sort list
nums3.sort()

# compute middle of the list
index = len(nums3) / 2

# compute median of the list items
if len(nums3) % 2 == 0:
    answer = (nums3[int(index)] + nums3[int(index - 1)]) / 2
else:
    answer = nums3[int(index - 0.5)]

# print the answer
print(answer)



