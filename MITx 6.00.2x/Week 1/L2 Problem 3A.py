import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    random.seed(0)
    return random.randrange(10,21,2)