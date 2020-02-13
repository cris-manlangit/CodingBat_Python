def count_evens(nums):
  n = len(nums)
  count = 0
  for i in range(n):
    if nums[i] % 2 == 0:
      count += 1
  return count