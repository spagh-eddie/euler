def find(n, matrix):
    """Finds the n adjacent numbers (including diagonally) in matrix
    with the largest product"""
    def phasor(lst):
        new = []
        for i in range(-1,2):
            for j in range(-1,2):
                if i!=0 or j!= 0:
                    if len(lst) > 1:
                        new.append([lst[0:-1]] + [[lst[-1][0]+i, lst[-1][1]+j]])
                    else:
                        new.append([lst[0]] + [[lst[-1][0]+i, lst[-1][1]+j]])
        return new
    def partition(partitions=[]):
        if partitions == []:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    partitions.append(([[i,j]]))
        else:
            new = []
            for i in range(len(partitions)):
                new.extend(phasor(partitions[i]))
            partitions = new
        return partitions
    reduce(lambda _, _: partition, list(range(n+1)))
