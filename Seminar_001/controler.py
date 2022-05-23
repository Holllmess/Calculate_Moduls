import model_complex as model
import view 
import calc_logger as cl

def button_click(): 
  number_1 = view.get_value()
  number_2 = view.get_value02()
  symbol01 = view.get_symbol()
  result = model.calculator(number_1, number_2, symbol01)
  view.view_data(result)
  cl.logger(number_1, number_2, symbol01, result)