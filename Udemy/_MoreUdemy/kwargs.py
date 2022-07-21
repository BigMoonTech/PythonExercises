
# Kwargs - keyword arguments - Are used when you don't know how many arguments there will be in a function

def calculate(**kwargs):
    
    operation_dict = {
        "add": kwargs["first"] + kwargs["second"],
        "subtract": kwargs["first"] - kwargs["second"],
        "multiply": kwargs["first"] * kwargs["second"],
        "divide": kwargs["first"] / kwargs["second"]
    }
    
    # catch division by zero error
    if kwargs["second"] == 0:
       return "Error. Cannot divide by zero."
       
    is_float = kwargs["make_float"]
        
    if not is_float:
        return "{} {}".format(kwargs.get("message", "The result is"), int(operation_dict[kwargs["operation"]]))
    else:
        return "{} {}".format(kwargs.get("message", "The result is"), operation_dict[kwargs["operation"]])


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))
print(calculate(make_float=True, operation='divide', first=3.5, second=5))