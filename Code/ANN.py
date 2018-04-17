import statistics
import numpy as np
import cmath


class Ann(object):
    path = "C:/John/EAI_Prac6/Datasets/q2inputs.csv"
    file = open(path)
    inputs = None  # number of inputs from dataset - indicates the amount of input neurons
    hn = 4  # chosen amount of hidden neurons including the bias neuron
    data = []

    def get_data(self):
        i = 0
        for row in self.file:  # get the x and y axis' data into row
            self.data.append([])
            while True:  # loop to find all the coordinates
                if row.find(',') != -1:
                    ind = row.index(',')
                    sub = row[0:ind]
                    row = row[ind + 1:]  # take out the value from row that was appended to data
                    sub = float(sub)
                    self.data[i].append(sub)  # add the value to the aaray of coordinates
                else:
                    row = row[:-2]
                    row = float(row)
                    self.data[i].append(row)
                    i += 1
                    break
        self.inputs = i

        u = []  # to store the mean values for the samples of each input
        sd = []  # to store the standard deviation values for the samples of each input

        for i in self.data:
            u.append(statistics.mean(i))
            sd.append(statistics.stdev(i))

        self.data = np.array(self.data)  # convert the list to a numpy array to simplify mathematical tasks as seen next

        for i in range(0, len(self.data)):
            self.data[i] = (self.data[i]-u[i])/sd[i]  # normalizing the data


    def neural_network(self):

        self.get_data()  # get and normalize the given data

        W1 = np.random.randn(self.inputs + 1, self.hn)  # generate the first step of the weights randomly
        # + 1 is for the bias node

        W1 = weights*cmath.sqrt(1/self.inputs)  # scale the weights with the variance
        # one can not that this has no effect in this question but might help in the next one

        W2 = np.random.randn

        A=[]  # to store the first set of samples
        for i in range(0, self.inputs):
            A.append(self.data[i][0])
        A.append(1)  # the input value of the bias node

        Z2 = np.matmul(A, weights)
        print("done")
