#import mymodule
# greeting = mymodule.greet('SESAC')
# print(greeting)

# greeting = mymodule.greet_kor('John')
# print(greeting)

#==========================================

# from mymodule import greet, greet_kor

# greeting = greet('SESAC')
# print(greeting)

# greeting = greet_kor('John')
# print(greeting)

#==============
from mymodule import *

greeting = greet('SESAC')
print(greeting)

greeting = greet_kor('John')
print(greeting)
