def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(n):
  a = n / 10
  if n % 10 >= 5:
    return (a + 1) * 10
  return a * 10
