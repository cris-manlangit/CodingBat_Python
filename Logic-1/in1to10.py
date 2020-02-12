def in1to10(n, outside_mode):
  if n == 1 or n == 10:
    return True
  if outside_mode:
    return n < 1 or n > 10
  return n > 1 and n < 10
