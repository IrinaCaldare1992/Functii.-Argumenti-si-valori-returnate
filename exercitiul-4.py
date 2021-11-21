def wrap_brackets( text ):
  return "(" + text + ")"
def wrap_sq_brackets( text ):
  return "[" + text + "]"
def wrap_sign( text ):
  return "<" + text + ">"

print(wrap_sign(wrap_sign(wrap_sign(wrap_sq_brackets(wrap_sq_brackets(wrap_sq_brackets(wrap_brackets("1234"))))))))