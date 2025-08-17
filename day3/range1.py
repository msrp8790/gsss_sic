'''num = 10

for i in range(num):
    print(f"i={i}")
    i += 2

#-------------------------------------------------'''

def my_range(*var_args):
    if len(var_args) < 1 or len(var_args) > 3:
        print("TypeError . You gave either 0 or more than 3 Args")
        return
    if len(var_args)==1:
        i=0
        while i < var_args[0]:
            yield 
            i += 1
num = 10
for i in my_range(num):
    print(i, end = ',')