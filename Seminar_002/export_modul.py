import init_modul as im

def export():
  with open('namebook.csv', 'a') as nb:
    nb.write(f'{im.name}, {im.surname}, {im.phone_number}, {im.comment};\n')
