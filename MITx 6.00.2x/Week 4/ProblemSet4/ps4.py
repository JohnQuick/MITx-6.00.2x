# 6.00.2x Problem Set 4

import numpy
import random
import pylab
from ps3b import *

#
# PROBLEM 1
#        
def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005
    numViruses = 100
    maxPop = 1000
    timeStepDelays = [0, 75, 150, 300]
    treatSteps = 150
    
    results = []

    for timeStepDelay in timeStepDelays:
        results.append([])
        for trial in range(numTrials):
            viruses = []
            for i in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            patient = TreatedPatient(viruses, maxPop)

            for step in range(timeStepDelay+treatSteps):
                if step == timeStepDelay:
                    patient.addPrescription('guttagonol')
                patient.update()
        
            results[timeStepDelays.index(timeStepDelay)].append(patient.getTotalPop())

    # Four axes, returned as a 2-d array
    f, axarr = pylab.subplots(2, 2)
    axarr[0, 0].hist(results[0])
    axarr[0, 0].set_title('0 time step delays')
    axarr[0, 1].hist(results[1])
    axarr[0, 1].set_title('75 time step delays')
    axarr[1, 0].hist(results[2])
    axarr[1, 0].set_title('150 time step delays')
    axarr[1, 1].hist(results[3])
    axarr[1, 1].set_title('300 time step delays')
    # Fine-tune figure; hide x ticks for top plots and y ticks for right plots
    #pylab.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
    #pylab.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
    pylab.show()

#simulationDelayedTreatment(1000)




#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005
    numViruses = 100
    maxPop = 1000
    noDrugTimeSteps = 150
    grimpexDelayedTimeSteps = [300, 150, 75, 0]
    twoDrugsTimeSteps = 150

    results = []

    for grimpexDelayed in grimpexDelayedTimeSteps:
        results.append([])
        for trial in range(numTrials):
            viruses = []
            for i in range(numViruses):
                viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))
            patient = TreatedPatient(viruses, maxPop)

            for step in range(noDrugTimeSteps + grimpexDelayed + twoDrugsTimeSteps):
                if step == noDrugTimeSteps:
                    patient.addPrescription('guttagonol')
                if step == noDrugTimeSteps + grimpexDelayed:
                    patient.addPrescription('grimpex')
                patient.update()

            results[grimpexDelayedTimeSteps.index(grimpexDelayed)].append(patient.getTotalPop())

    f, axarr = pylab.subplots(2, 2)
    axarr[0, 0].hist(results[0])
    axarr[0, 0].set_title('300 time step delays')
    axarr[0, 1].hist(results[1])
    axarr[0, 1].set_title('150 time step delays')
    axarr[1, 0].hist(results[2])
    axarr[1, 0].set_title('75 time step delays')
    axarr[1, 1].hist(results[3])
    axarr[1, 1].set_title('0 time step delays')
    pylab.show()

simulationTwoDrugsDelayedTreatment(1000)