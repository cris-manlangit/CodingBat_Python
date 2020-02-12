def front_times(str, n):
  result = ''
  m = str
  if len(str) > 3:
    m = str[:3]
  for i in range(n):
    result += m
  return result
