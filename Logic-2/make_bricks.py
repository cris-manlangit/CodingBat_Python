def make_bricks(small, big, goal):
  req_big = goal / 5
  req_small = goal % 5
  
  if big < req_big:
    req_small += (req_big - big) * 5
    
  return small >= req_small
