import textwrap

def simple_wrap(string, max_width):
    return textwrap.fill(string, max_width)

def wrap(string, max_width):
    current = string

    while len(current) > 0:
        if len(current) >= max_width:
            print(current[:max_width])
            current = current[max_width:]
        else:
            print(current)
            break
       
string, max_width = input(), int(input())
result = simple_wrap(string, max_width)
print(result)