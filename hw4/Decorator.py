def show(func):
    def new_func(*args, **kwargs):
        print("Running function", func.__name__)
        print("Positional arguments are", args)
        print("Keyword arguments are", kwargs)
        result = func(*args, **kwargs)
        print("Result:", result)
        return result
    return new_func

@show 
def sum(a,b):
    return a+b

sum(10,22)