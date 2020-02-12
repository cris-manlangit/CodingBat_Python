def caught_speeding(speed, is_birthday):
  add_speed = 0
  if is_birthday:
    add_speed += 5
  if speed <= 60 + add_speed:
    return 0
  if speed <= 80 + add_speed and speed >= 61 + add_speed:
    return 1
  return 2
