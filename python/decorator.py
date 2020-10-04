import functools

BALANCE = 100
LOGGED_IN = True


def login_required(func):
  @functools.wraps(func)
  def wrapper():
    if LOGGED_IN:
      func()
    else:
      print("You're not logged in!")
  return wrapper

# wrapping a function
def get_bal():
  print(f"Your Balance is: {BALANCE}")

get_bal = login_required(get_bal)

# syntactic sugar for decorator
@login_required
def get_balance():
  print(f"Your Balance is: {BALANCE}")

get_balance()
get_bal()
