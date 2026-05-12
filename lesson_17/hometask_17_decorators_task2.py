def exceptions_decorator(func):
     def wrapper(*args, **kwargs):
         try:
             result = func(*args, **kwargs)
             return result
         except Exception as e:
             print (f"Caught exception: {e}")
             return

     return wrapper

@exceptions_decorator
def divide(a, b):
    return a / b

if __name__ == "__main__":
    print(divide(1, 0))