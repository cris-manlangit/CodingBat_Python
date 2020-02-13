def count_hi(str):
  n = len(str)
  count = 0
  for i in range(n-1):
    if str[i:i+2] == 'hi':
      count += 1
  return count