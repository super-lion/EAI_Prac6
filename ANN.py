import csv







class ann(object):
    path = "C:/John/EAI_Prac6/Datasets/q2inputs.csv"
    file = open(path)
    data = [[],[]]



    def get_data(self):
        i = 0
        for row in self.file:                           # get the x and y axis' data into row

            while True:                                 #loop to find all the coordinates
                if row.find(',') != -1:
                    ind = row.index(',')
                    sub = row[0:ind]
                    row = row[ind+1:]                   #take out the value from row that was appended to data
                    sub = float(sub)
                    self.data[i].append(sub)     #add the value to the aaray of coordinates
                else:
                    row = row[:-2]
                    row = float(row)
                    self.data[i].append(row)
                    i+=1
                    break
        for a in range(0,2):
            max = None
            for b in  self.data[a]:
                if max == None:
                    max = b
                elif b > max:
                    max = b

            for b in range(0,len(self.data[a])):
                self.data[a][b] = self.data[a][b]/max






        print("done")
