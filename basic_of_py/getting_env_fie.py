import os
import dotenv
import functools 
dotenv.load_dotenv()
print(os.getenv("API_KEY"))


a = [1,2,3,4,5,6,7,8,9,10]



def multiply(x, y):
    return x * y


result = functools.reduce(multiply, a)
print(result)

