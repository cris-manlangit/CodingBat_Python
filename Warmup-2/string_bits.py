def string_bits(str):
  result = ''
  n = len(str)
  for i in range(n):
    if i % 2 == 0:
      result += str[i]
  return result
