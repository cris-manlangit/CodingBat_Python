def sum2(nums):
  n = len(nums)
  if n == 0:
    return 0
  if n == 1:
    return nums[0]
  return nums[0] + nums[1]
