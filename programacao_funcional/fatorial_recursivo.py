def fatorial(n):
    return n * (fatorial(n - 1) if (n - 1) > 1 else 1)


if __name__ == '__main__':
    print(f'10! = {fatorial(10)}')
    '''
    Curiosidade:
    6 semanas em segundos é igual a 10!
    6 * 7 * 24 * 60 * 60

    6 * 7 * 8 * 3 * 10 * 6 * 3 * 20
    6 * 7 * 8 * 9 * 10 * 2 * 3 * 4 * 5
    '''
