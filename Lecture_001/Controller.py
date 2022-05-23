import Model_sub as Model
import View

def button_click(): 
  value_a = View.get_value()
  value_b = View.get_value()
  Model.init(value_a, value_b)
  result = Model.do_it()
  View.view_data(result)