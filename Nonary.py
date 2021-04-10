import numpy as np


# класс девятки
class nonary:
    matrix = []

    def __init__(self, mat):
        self.matrix = np.zeros((3, 3), dtype=int)
        self.matrix = mat

    # получение содержимого девятки
    def getMatrix(self):
        return self.matrix

    # выводы для удобвства отладки
    def printf(self, filePath):
        np.savetxt(filePath, self.matrix, '%1d')

    def print(self):
        print(self.matrix)
