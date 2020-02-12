def array_count9(nums):
  n = len(nums)
  count = 0
  for i in range(n):
    if nums[i] == 9:
      count +=1
  return count
