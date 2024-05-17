>>> class NextClass:  # Define class
...     def printer(self, text):  # Define method
...         self.message = text  # Change instance
...         print(self.message)  # Access instance
...
>>> 
>>> x = NextClass()
>>> x.printer("Instance call")  # Call its method
Instance call
>>> x.message
'Instance call'
>>> NextClass.printer(x, "class call")  # Direct class call
class call
>>> x.message  # Instance changed again
'class call'
>>>