import csv







class ann(object):
    path = "C:/John/EAI_Prac6/Datasets/q2inputs.csv"
    file = open(path)
    data = [[],[]]



    def get_data(self):
        for row in self.file:                           # get the x and y axis' data into row
            i = 0
            while True:                                 #loop to find all the coordinates
                if row.find(',') != -1:
                    ind = row.index(',')
                    sub = row[0:ind]
                    self.data[i].append(sub)              #add the value to the aaray of coordinates
                else:
                    self.data[i].append(row)


        print("done")
