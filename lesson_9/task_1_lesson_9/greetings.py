# Модуль з привітанням

def say_hello(name):
    return f'Привіт, {name}'

def say_goodbye(name ):
    return f'До побачення, {name}'

if __name__ == '__main__':    
    print(say_hello('John'))
    print(say_goodbye('John'))