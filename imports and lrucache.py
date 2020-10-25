import sys
import whileloop
import time
from functools import lru_cache

print(sys.path)
whileloop.while_loop()

@lru_cache(maxsize = 5)
def kd(m):
	time.sleep(m)
	return m
	
print("starting")
kd(3)
print("done and again starting")
print("starting")
kd(3)
print("done and again starting")
