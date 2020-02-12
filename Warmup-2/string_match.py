def string_match(a, b):
  long = a
  short = b
  if len(short) > len(long):
    long = b
    short = a
  count = 0
  for i in range(len(short) - 1):
    if long[i:i+2] == short[i:i+2]:
      count += 1
  return count
