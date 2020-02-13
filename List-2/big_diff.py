def big_diff(nums):
  n = len(nums)
  lrg = nums[0]
  sml = nums[0]
  for i in range(n):
    lrg = max(lrg, nums[i])
    sml = min(sml, nums[i])
  return lrg - sml