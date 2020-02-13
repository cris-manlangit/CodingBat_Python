def count_code(str):
  n = len(str)
  count = 0
  for i in range(n-3):
    if str[i:i+2] == 'co' and str[i+3] == 'e':
      count += 1
  return count