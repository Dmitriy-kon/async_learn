import asyncio

def greeting(name):
    return f"Hello {name}"

def farewell(name):
    return f"Goodbye {name}"

def process_name(callback, name):
    return callback(name)

name = "Антон"

result = process_name(greeting, name)
print(result)

result = process_name(farewell, name)
print(result)
