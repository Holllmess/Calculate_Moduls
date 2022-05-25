from user_interface import *
from init_modul import *
from export_modul import *
from import_modul import * 

def button_click():
  move = input('If You want to export data enter "e", and if You want import - "i": ')
  if move == 'e':
    data = get_data()
    init(data)
    export()
  elif move == 'i':
    print(importt())
  else:
    print('Start from the beginning. Enter either "e" or "i", nothing more, please love.')