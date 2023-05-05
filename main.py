def to_upper(name):
    return name.upper()


def say_hello(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hello, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    name = 'TrainWithShubham'
    say_hello(name)
    up = to_upper(name)
    print(up)