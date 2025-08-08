def limit_uses(uses):
    def decorator(func):
        counter = 0
        def wrapper(*args, **kwargs):
            nonlocal counter 
            counter += 1
            if counter <= uses:
                value = func(*args, **kwargs)
                return value
            else:
                print("You've run out of uses.")
        return wrapper
    return decorator

@limit_uses(2)
def greet_person(host, guest):
    return f"{host} says hello to {guest}"

# greet_person = limit_uses(greet_person)
print(greet_person("Dave", "Mary"))
print(greet_person("Dave", "Nick"))
print(greet_person("Dave", "Sue"))
print(greet_person("Dave", "Stewart"))