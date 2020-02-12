def not_string(str):
  n = len(str)
  if n > 2 and str[:3] == 'not':
    return str
  return 'not ' + str
