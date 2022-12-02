from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData()
def testPenData(hiddenLayers = [24]):
    return buildNeuralNet(penData, maxItr = 200, hiddenLayerList = hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [16]):
    return buildNeuralNet(carData, maxItr = 200,hiddenLayerList = hiddenLayers)

testCarData()


def Q5():
    results_pen = [testPenData()[1] for i in range(5)]
    print("Pen Results")
    print("Max Accuracy: " + str(max(results_pen)))
    print("Average Accuracy: " + str(average(results_pen)))
    print("Std Dev: " + str(stDeviation(results_pen)))

    results_car = [testCarData()[1] for i in range(5)]

    print("Car Results")
    print("Max Accuracy: " + str(max(results_car)))
    print("Average Accuracy: " + str(average(results_car)))
    print("Std Dev: " + str(stDeviation(results_car)))

# Q5()

def Q6():
    for i in range(0, 41, 5):
        pen = []
        for _ in range(5):
            pen.append(testPenData([i])[1])
        print("Perceptrons: ", i)
        print("Maximum Accuracy: ", max(pen))
        print("Average Accuracy: ", average(pen))
        print("Standard Deviation: ", stDeviation(pen))


    for i in range(0, 41, 5):
        car = []
        for _ in range(5):
            car.append(testCarData([i])[1])
        print("Perceptrons: ", i)
        print("Maximum Accuracy: ", max(car))
        print("Average Accuracy: ", average(car))
        print("Standard Deviation: ", stDeviation(car))
Q6()