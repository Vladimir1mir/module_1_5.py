immutable_var = (1, [2], 3.0, 'String',  True)
print(immutable_var)
#print(type(immutable_var[3]))
#immutable_var[0]=10
#print(immutable_var)

# Выведено:TypeError: 'tuple' object does not support item assignment
# Tuple - такая же коллекция, как и список, но неизменяемая.
# Элементы внутри кортежа могут быть разным.
# Может внутри себя содержать изменяемые объекты.
# Кортеж занимает меньше памяти чем список.

mutable_list = [1, [2], 3.0, 'String',  True]
mutable_list[0]=10
print(mutable_list)
#List - изменяемая коллекция.