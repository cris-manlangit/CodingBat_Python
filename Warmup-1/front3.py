def front3(str):
  n = len(str)
  if n < 3:
    return str + str + str
  result = str[:3]
  return result + result + result
