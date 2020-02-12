def make_chocolate(small, big, goal):
  req_big = goal / 5
  req_small = goal % 5
  
  if big < req_big:
    req_small += (req_big - big) * 5
    
  if small >= req_small:
    return req_small
  return -1
