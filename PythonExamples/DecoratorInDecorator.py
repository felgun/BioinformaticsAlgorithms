"""
	DecoratorInDecorator.py
	This is an example on using a decorator in some other decorators. 
	Example from:
		Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
		https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""

#import the decorator wraps 
from functools import wraps

def logger(orig_func):
	import logging
	logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

	#use the wraps decorator for the original function
	@wraps(orig_func) 
	def wrapper(*args,**kwargs):
		logging.info(
			"Ran using args: {} and kwargs: {}".format(args,kwargs))
		return orig_func(*args,**kwargs)

	return wrapper


def timer(orig_func):
	import time

	#use the wraps decorator for the original function
	@wraps(orig_func)
	def wrapper(*args,**kwargs):
		t1 = time.time()
		result = orig_func(*args,**kwargs)
		elapsed = time.time() - t1
		print("{} ran in : {} sec.".format(orig_func.__name__, elapsed))
		return result
	return wrapper

import time

# use both timer decorator and logger decorator for display_info function
@timer
@logger 
def display_info(name,age):
	time.sleep(1)
	print("display_info ran with arguments ({},{})".format(name,age))

display_info("Feliz",24)

