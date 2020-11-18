# def greet(greeting, target):
#     return f"{greeting}! {target}"

import functools

greet = functools.partial(greet, 'hola')
print(greet('Bob'))