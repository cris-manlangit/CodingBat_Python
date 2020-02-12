def last2(str):
  n = len(str)
  count = 0
  if n < 3:
    return count
  last2 = str[n-2:n]
  for i in range(n-2):
    if last2 == str[i:i+2]:
      count +=1
  return count
