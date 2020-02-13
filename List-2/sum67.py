def sum67(nums):
  n = len(nums)
  sum = 0
  switch = 0
  for i in range(n):
    if nums[i] == 6:
      switch = 1
    if switch == 0:
      sum += nums[i]
    else:
      if nums[i] == 7:
        switch = 0
  return sum