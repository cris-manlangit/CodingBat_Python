def close_far(a, b, c):
  return (abs(a - b) < 2 and abs(a - c) >= 2 and abs(b - c) >= 2) or (abs(a - b) >= 2 and abs(a - c) < 2 and abs(b - c) >= 2)
