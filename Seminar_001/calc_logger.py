from datetime import datetime as dt

def logger(number01, number02, symbol, data): 
  time = dt.now().strftime('%H:%M')
  with open('logger.csv', 'a') as file: 
    file.write('{} calculation result: {} {} {} = {}\n'
                .format(time, number01, symbol, number02, data))
