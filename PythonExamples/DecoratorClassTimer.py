"""
	DecoratorClassTimer.py
	This is an example on using a decorator class. 
	Example from:
		Python Tutorial: Decorators - Dynamically Alter The Functionality Of Your Functions
		https://www.youtube.com/watch?v=FsAPt_9Bf3U
"""

class decorator_timer(object):
	import time

	def __init__(self,orig_func):
		self.orig_func = orig_func		

	def __call__(self,*args,**kwargs):
		t1 = time.time()
		result = self.orig_func(*args,**kwargs)
		elapsed = time.time() - t1
		print("{} ran in : {} sec.".format(self.orig_func.__name__, elapsed))
		return result
	

import time

# use both timer decorator class for display_info function
@decorator_timer 
def display_info(name,age):
	time.sleep(1)
	print("display_info ran with arguments ({},{})".format(name,age))

display_info("Annabelle",10)

