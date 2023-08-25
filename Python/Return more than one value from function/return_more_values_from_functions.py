# %%
def my_func():
    return 1


my_func()

# %%
one = my_func()
print(type(one))


# %%
def multiple_values():
    return 1, 2


multiple_values()
type(multiple_values())

# %%
one, two = multiple_values()
print(one)
print(two)

# %%
my_tuple = (1, 2)
my_other_tuple = 1, 2

print(type(my_tuple))
print(type(my_other_tuple))

# %%
my_single_tuple = (1,)
type(my_single_tuple)

# %%
my_tuple = (1, 2, 3, 4)
one, two, *the_rest = my_tuple
print(one)
print(two)
print(the_rest)
type(the_rest)


# %%
def returning_a_dictionary():
    return {"one": 1, "two": 2, "three": 3, "four": 4}


my_dict = returning_a_dictionary()

my_dict["four"]
