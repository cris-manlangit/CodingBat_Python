def double_char(str):
  n = len(str)
  result = ''
  for i in range(n):
    result += str[i] + str[i]
  return result