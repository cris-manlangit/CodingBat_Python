def xyz_there(str):
  n = len(str)
  if n < 3:
    return False
  for i in range(n-2):
    if str[i:i+3] == 'xyz':
      if (i > 0 and str[i-1] != '.') or i == 0:
        return True
  return False