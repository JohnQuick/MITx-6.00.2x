import random, pylab

balls = []
for i in range(1000):
    if i <500:
        balls.append('White')
    else:
        balls.append('Black')

random.shuffle(balls)

#print balls
#print 'White Balls: '+ str(balls.count('White'))
#print 'Black Balls: '+ str(balls.count('Black'))
#print 'Total Balls: '+ str(len(balls))

def LV():
    n = 1
    while random.choice(balls) != 'White':
        n+=1

    return n

def MC(k):
    location = random.choice(range(1000))
    n = 1
    while balls[location] != 'White':
        if n > k:
            return 0
        location += 1
        if location >= 1000:
            location -= 1000
        n += 1

    return n

def problem7_1():
    histogram = [ 0 for i in range(1,1000)]  # intialize the list to be all zeros
    for i in range(1000):
        result = LV()
        histogram[result] += 1
    pylab.plot(histogram)
    pylab.show()

def problem7_2(k):
    histogram = [ 0 for i in range(1,1000)]  # intialize the list to be all zeros
    for i in range(1000):
        result = MC(k)
        histogram[ result ] += 1
    pylab.plot( histogram )
    pylab.show()



#problem7_1()
#problem7_2(100)