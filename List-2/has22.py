def has22(nums):
  n = len(nums)
  switch = 0
  for i in range(n):
    if switch == 1 and nums[i] == 2:
      return True
    if nums[i] == 2:
      switch = 1
    else:
      switch = 0
  return False