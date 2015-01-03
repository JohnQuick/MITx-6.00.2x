import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    yes = 0
    for i in range(numTrials):
        bucket = ["red","red","red","green","green","green"]
        drawed = []
        for j in range(3):
            drawed.append(bucket.pop(int(random.random()*len(bucket))))
        if drawed.count("red") == 3 or drawed.count("green") == 3:
            yes += 1
    return float(yes)/float(numTrials)