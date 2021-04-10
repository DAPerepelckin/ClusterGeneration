import random

import numpy as np

import Nonary as Nonary


# класс, реализующий фабричный метод создания девяток
class NonaryFabric:
    def create(self, color_count, colors):
        created = self._get_nonary(color_count, colors)
        return created

    def _get_nonary(self, color_count, colors):
        if color_count == 1:
            return self.nonary1(colors)
        elif color_count == 2:
            return self.nonary2(colors)
        elif color_count == 3:
            return self.nonary3(colors)
        elif color_count == 4:
            return self.nonary4(colors)
        elif color_count == 5:
            return self.nonary5(colors)
        elif color_count == 6:
            return self.nonary6(colors)
        elif color_count == 7:
            return self.nonary7(colors)
        elif color_count == 8:
            return self.nonary8(colors)

    # формирование девятки из 1 цвета
    def nonary1(self, colors):
        mat = np.zeros((3, 3), int)
        mat.fill(colors[0])
        return Nonary.nonary(mat)

    # формирование девятки из 2 цветов
    def nonary2(self, colors):
        mat = [[colors[0], colors[0], colors[0]],
               [colors[0], colors[0], colors[1]],
               [colors[1], colors[1], colors[1]]]
        mat = self.shuffle(mat)
        return Nonary.nonary(mat)

    # формирование девятки из 3 цветов
    def nonary3(self, colors):
        mat = [[colors[0], colors[0], colors[0]],
               [colors[1], colors[1], colors[1]],
               [colors[2], colors[2], colors[2]]]
        mat = self.shuffle(mat)
        return Nonary.nonary(mat)

    # формирование девятки из 4 цветов
    def nonary4(self, colors):
        mat = [[colors[0], colors[0], colors[1]],
               [colors[1], colors[2], colors[2]],
               [colors[3], colors[3], colors[3]]]
        mat = self.shuffle(mat)
        return Nonary.nonary(mat)

    # формирование девятки из 5 цветов
    def nonary5(self, colors):
        mat = [[colors[0], colors[1], colors[1]],
               [colors[2], colors[2], colors[3]],
               [colors[3], colors[4], colors[4]]]
        mat = self.shuffle(mat)
        return Nonary.nonary(mat)

    # формирование девятки из 6 цветов
    def nonary6(self, colors):
        mat = [[colors[0], colors[1], colors[2]],
               [colors[3], colors[3], colors[4]],
               [colors[4], colors[5], colors[5]]]
        mat = self.shuffle(mat)
        return Nonary.nonary(mat)

    # формирование девятки из 7 цветов
    def nonary7(self, colors):
        mat = [[colors[0], colors[1], colors[2]],
               [colors[3], colors[4], colors[5]],
               [colors[5], colors[6], colors[6]]]
        mat = self.shuffle(mat)
        return Nonary.nonary(mat)

    # формирование девятки из 8 цветов(последнего цвета 2 раза)
    def nonary8(self, colors):
        mat = [[colors[0], colors[1], colors[2]],
               [colors[3], colors[4], colors[5]],
               [colors[6], colors[7], colors[7]]]
        mat = self.shuffle(mat)
        return Nonary.nonary(mat)

    # перемешивание матрицы алгоритмом Кнута
    @staticmethod
    def shuffle(mat):
        for i in range(2):
            for j in range(2):
                index = random.randint(0, 8)
                a = index // 3
                b = index % 3
                mat[i][j], mat[a][b] = mat[a][b], mat[i][j]
        return mat
