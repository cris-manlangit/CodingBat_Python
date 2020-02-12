def combo_string(a, b):
  long = a
  short = b
  if len(short) > len(long):
      long = b
      short = a
  return short + long + short
