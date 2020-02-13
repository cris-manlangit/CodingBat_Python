def end_other(a, b):
  long = a
  short = b
  if len(b) > len(a):
    long = short
    short = a
  return short.lower() == long[-len(short):].lower()