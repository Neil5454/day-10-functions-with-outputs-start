#Functions with Outputs

def format_name(f_name, l_name):
  formatted_f_name = (f_name.title())
  formatted_l_name = (l_name.title())
  return f"{formatted_f_name} {formatted_l_name}" #output replaces the part of the code where the function is called (i.e. row 8...format_name)

formatted_string = format_name("nEIl", "cohen")
print(formatted_string)
#or print(format_name("nEIl", "cohen"))
