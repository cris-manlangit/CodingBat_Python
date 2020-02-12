def alarm_clock(day, vacation):
  wd = '7:00'
  we = '10:00'
  if vacation:
    wd = we
    we = 'off'
  if day >= 1 and day <= 5:
    return wd
  return we
