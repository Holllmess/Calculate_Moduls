from random import randint

def get_temperature(sensor): 
  return randint(-20, 0) if sensor else randint(0, 20)  # можно записывать по разному 

def get_preassure(sensor):   # preassure - давление 
  if sensor:                                            # можно записывать по разному 
    return randint(700, 750)
  else: 
    return randint(750, 800)

def get_wind_speed(sensor): 
  if sensor == 1:                                       # можно записывать по разному
    return randint(0, 30)
  else:
    return randint(30, 70)

def data_collection(sensor = 1): 
  return (get_temperature(sensor), get_preassure(sensor), get_wind_speed(sensor))