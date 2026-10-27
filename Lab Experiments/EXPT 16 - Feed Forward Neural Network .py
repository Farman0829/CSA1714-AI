import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]

print("Feed Forward Neural Network Output:")

for x in inputs:
    h1 = sigmoid(x[0] * 0.5 + x[1] * 0.5)
    h2 = sigmoid(x[0] * 0.5 + x[1] * 0.5)

    output = sigmoid(h1 + h2)

    print(round(output, 8))
