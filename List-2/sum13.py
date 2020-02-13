def sum13(nums):
  n = len(nums)
  switch = 0
  sum = 0
  for i in range(n):
    if nums[i] == 13:
      switch = 1
    else:
      if switch == 0:
        sum += nums[i]
      switch = 0
  return sum