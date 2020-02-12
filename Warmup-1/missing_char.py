def missing_char(str, n):
  m = len(str)
  beg = str[0:n]
  end = str[n + 1:m]
  return beg + end
