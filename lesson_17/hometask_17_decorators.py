#Decorator. Task 1.

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_decorator(func):
     def wrapper(*args):
         result = func(*args)
         logging.info(f"Called {func.__name__} with args {args}")
         return result
     return wrapper

@log_decorator
def function(name, profession):
    print('Hello %s!' % name, profession)

if __name__ == "__main__":
    function("Olena", "QA")