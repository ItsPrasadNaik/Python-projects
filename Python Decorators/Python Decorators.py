def log_message(func):
    def message(*vals):
        res = func(*vals)
        file = open('C:/Users/nprasad/PycharmProjects/pythonProject/ZeOmega Self Learn/tmp/decorator_logs.txt', 'a+')
        file.write(res)
        return res
    return message

@log_message
def a_function_that_returns_a_string():
      return "A string"
@log_message
def a_function_that_returns_a_string_with_newline(st):
      return "{}\n".format(st)
@log_message
def a_function_that_returns_another_string(string=""):
      return "Another string"

print(a_function_that_returns_a_string())
print(a_function_that_returns_a_string_with_newline(input("Enter Your Name : ")))
print(a_function_that_returns_another_string())

