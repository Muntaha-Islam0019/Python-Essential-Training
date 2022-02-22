def main():
    a_tuple = ('meow', 'grrr', 'purr')
    # If I remove the asterisk from the next line, it prints the tuple
    # If it remains the same, then the elements of the tuple gets printed one-by-one
    kitten(*a_tuple)

def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')

if __name__ == '__main__': main()