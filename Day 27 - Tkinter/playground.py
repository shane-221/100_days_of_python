def add(*args):
    print(args[1])

    x=0
    for n in args:
      x+=n
    return x

print(add(3,5,7,9))