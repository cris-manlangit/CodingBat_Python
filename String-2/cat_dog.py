def cat_dog(str):
  n = len(str)
  countc = 0
  countd = 0
  for i in range(n-2):
    if str[i:i+3] == 'cat':
      countc += 1
    if str[i:i+3] == 'dog':
      countd += 1
  return countc == countd