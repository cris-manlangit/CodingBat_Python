def centered_average(nums):
  n = len(nums)
  count = 0
  sum = 0
  n = len(nums)
  lrg = nums[0]
  sml = nums[0]
  for i in range(n):
    lrg = max(lrg, nums[i])
    sml = min(sml, nums[i])
    sum += nums[i]
    count += 1
  return (sum - lrg - sml) / (count - 2)