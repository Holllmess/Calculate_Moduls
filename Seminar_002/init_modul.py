name = 'Nicolaus'
surname = 'Torch'
phone_number = '095228420'
comment = 'tea_ceremonymaker'

def init(data): 
  global name, surname, phone_number, comment

  list_data = data.split(' ') 
  name = list_data[0]
  surname = list_data[1]
  phone_number = list_data[2]
  comment = list_data[3]
  
