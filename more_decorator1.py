"""
python中的装饰器分为两类：函数装饰器和类装饰器。
"""
# 不带参数的装饰器。即@decorator

"""
@decorator
"""

# a decorator receives the method it's wrapping as a variable 'f'
def increment(f):
    # we use arbitrary args and keywords to
    # ensure we grab all the input arguments.
    def wrapped_f(*args, **kw):
        # note we call f against the variables passed into the wrapper,
        # and cast the result to an int and increment .
        return int(f(*args, **kw)) + 1
    return wrapped_f  # the wrapped function gets returned.
@increment
def plus(a, b):
    return a + b
#等价于
#def plus(a, b):
#    return a + b
#plus = increment(plus)

result = plus(4, 6)
if result == 11:
    print('good')