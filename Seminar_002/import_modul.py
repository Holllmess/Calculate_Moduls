def importt(): 
  with open('namebook.csv', 'r') as nb:
    item = nb.read()
    return item