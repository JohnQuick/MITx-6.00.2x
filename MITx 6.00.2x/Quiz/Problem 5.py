import random, pylab

def sampleQuizzes():
    midTerm1 = []
    midTerm2 = []
    finalExam = []

    for i in range(50, 81):
        midTerm1.append(i)
    for i in range(60, 91):
        midTerm2.append(i)
    for i in range(55, 96):
        finalExam.append(i)

    finalScores = []
    for trial in range(10000):
        finalScores.append(random.choice(midTerm1)*0.25+random.choice(midTerm2)*0.25+random.choice(finalExam)*0.5)

    def checkScore(x):
        if 70 <= x <= 75:
            return True

    return len(filter(checkScore, finalScores))/float(10000)

#print sampleQuizzes()

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    midTerm1 = []
    midTerm2 = []
    finalExam = []

    for i in range(50, 81):
        midTerm1.append(i)
    for i in range(60, 91):
        midTerm2.append(i)
    for i in range(55, 96):
        finalExam.append(i)

    finalScores = []
    for trial in range(numTrials):
        finalScores.append(random.choice(midTerm1)*0.25+random.choice(midTerm2)*0.25+random.choice(finalExam)*0.5)

    return finalScores

def plotQuizzes():
    results = generateScores(10000)
    pylab.hist(results,7)
    pylab.title('Distribution of Scores')
    pylab.xlabel('Final Score')
    pylab.ylabel('Number of Trials')
    pylab.show()

plotQuizzes()