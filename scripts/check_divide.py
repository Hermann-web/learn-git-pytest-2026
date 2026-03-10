import sys
sys.path.append(".")

from exercise1.calculator import divide
import inspect

print("filename:", divide.__code__.co_filename)
print("source:")
print(inspect.getsource(divide))
try:
    divide(5,0)
    print("no exception")
except Exception as e:
    print(type(e).__name__, str(e))
