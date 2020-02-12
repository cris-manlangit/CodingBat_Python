def string_splosion(str):
  n = len(str)
  result = ''
  for i in range(n + 1):
    result += str[:i]
  return result
