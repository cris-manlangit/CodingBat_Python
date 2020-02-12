def front_back(str):
  n = len(str)
  if n < 2:
    return str
  beg = str[0:1]
  mid = str[1:n-1]
  end = str[n-1:n]
  return end + mid + beg
