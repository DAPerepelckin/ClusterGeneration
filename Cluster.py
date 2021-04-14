import itertools as it

import numpy as np
from PIL import Image, ImageDraw

import NonaryFabric as nf


class cluster:
    # матрица хрянящая наш кластер
    matrix = []
    # массив отслеживающий количество цветов
    countOfColor = []
    # массив хранящий оставшиеся цвета после создания всех девяток
    arrayOfRemainderColors = []

    # конструктор кластера
    def __init__(self):

        self.matrix = np.zeros((80, 100), dtype=int)
        self.countOfColor = [1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000]

        # массив девяток
        arr = []
        nonaryFabric = nf.NonaryFabric()

        # создание по 5 девяток каждого цвета
        for i in range(5):
            for j in range(8):
                self.countOfColor[j] -= 9
                arr.append(nonaryFabric.create(1, [j]))

        # создание по 3 девятки на каждую комбинацию из 2 цветов
        for i in range(3):
            for j in list(it.combinations(range(8), 2)):
                self.countOfColor[j[0]] -= 5
                self.countOfColor[j[1]] -= 4
                arr.append(nonaryFabric.create(2, j))

        # создание по 2 девятки на каждую комбинацию из 3 цветов
        for i in range(2):
            for j in list(it.combinations(range(8), 3)):
                self.countOfColor[j[0]] -= 3
                self.countOfColor[j[1]] -= 3
                self.countOfColor[j[2]] -= 3
                arr.append(nonaryFabric.create(3, j))

        # создание по 2 девятки на каждую комбинацию из 4 цветов
        for i in range(2):
            for j in list(it.combinations(range(8), 4)):
                self.countOfColor[j[0]] -= 2
                self.countOfColor[j[1]] -= 2
                self.countOfColor[j[2]] -= 2
                self.countOfColor[j[3]] -= 3
                arr.append(nonaryFabric.create(4, j))

        # создание по 2 девятки на каждую комбинацию из 5 цветов
        for i in range(2):
            for j in list(it.combinations(range(8), 5)):
                self.countOfColor[j[0]] -= 1
                self.countOfColor[j[1]] -= 2
                self.countOfColor[j[2]] -= 2
                self.countOfColor[j[3]] -= 2
                self.countOfColor[j[4]] -= 2
                arr.append(nonaryFabric.create(5, j))

        # создание по 3 девятки на каждую комбинацию из 6 цветов
        for i in range(3):
            for j in list(it.combinations(range(8), 6)):
                self.countOfColor[j[0]] -= 1
                self.countOfColor[j[1]] -= 1
                self.countOfColor[j[2]] -= 1
                self.countOfColor[j[3]] -= 2
                self.countOfColor[j[4]] -= 2
                self.countOfColor[j[5]] -= 2
                arr.append(nonaryFabric.create(6, j))

        # создание по 5 девяток на каждую комбинацию из 7 цветов
        for i in range(5):
            for j in list(it.combinations(range(8), 7)):
                self.countOfColor[j[0]] -= 1
                self.countOfColor[j[1]] -= 1
                self.countOfColor[j[2]] -= 1
                self.countOfColor[j[3]] -= 1
                self.countOfColor[j[4]] -= 1
                self.countOfColor[j[5]] -= 2
                self.countOfColor[j[6]] -= 2
                arr.append(nonaryFabric.create(7, j))

        # создание по 6 девяток на каждый из 8 цветов.
        # в девятке 9 ячеек а значит один цвет будет 2 раза
        # для точного контроля количества цветов делаем, чтобы каждый из 8 цветов был "диминирующим" по 6 раз
        for i in range(6):
            for c in range(8):
                colors = np.arange(8)
                colors[7], colors[c] = colors[c], colors[7]
                self.countOfColor[colors[0]] -= 1
                self.countOfColor[colors[1]] -= 1
                self.countOfColor[colors[2]] -= 1
                self.countOfColor[colors[3]] -= 1
                self.countOfColor[colors[4]] -= 1
                self.countOfColor[colors[5]] -= 1
                self.countOfColor[colors[6]] -= 1
                self.countOfColor[colors[7]] -= 2
                arr.append(nonaryFabric.create(8, colors))

        # перемешиваем массив и приводим к виду матрицы 33 на 20 девяток
        np.random.shuffle(arr)
        arr = np.reshape(arr, (33, 20))

        # формирруем матрицу цветов из матрицы девяток
        self.matrix = self.getMatFromNonaries(arr)

        # хаотично распределяем оставшиеся цвета
        self.arrayOfRemainderColors = self.countOfColorToArrayOfColor()

        # вставляем недостающие(крайние ряды)
        self.appendRows()

        # приписываем крайний правый(сотый) столбец цветов
        self.matrix = np.insert(self.matrix, 99, self.arrayOfRemainderColors, axis=1)

    # получение матрицу цветов из матрицы девяток
    @staticmethod
    def getMatFromNonaries(arr):
        mat = []
        for i in range(33):
            row = []
            for j in range(20):
                if row.__len__() == 0:
                    row = arr[i][j].getMatrix()
                else:
                    row = np.vstack((row, arr[i][j].getMatrix()))
            if mat.__len__() == 0:
                mat = row
            else:
                mat = np.hstack((mat, row))
        return mat

    # создание перемешанного массива недостающих цветов
    def countOfColorToArrayOfColor(self):
        arr = []
        for i in range(8):
            for j in range(self.countOfColor[i]):
                arr.append(i)
        np.random.shuffle(arr)
        return arr

    # вставка недостающих строк
    def appendRows(self):
        for i in range(10):
            self.matrix = np.insert(self.matrix, i * 8, np.array(self.arrayOfRemainderColors[0:99]), axis=0)
            self.arrayOfRemainderColors = self.arrayOfRemainderColors[99:]
            self.matrix = np.insert(self.matrix, (i + 1) * 8 - 1, np.array(self.arrayOfRemainderColors[0:99]), axis=0)
            self.arrayOfRemainderColors = self.arrayOfRemainderColors[99:]

    # вывод для удобста отладки
    def print(self):
        print(self.matrix)

    # вывод в txt файл
    def printf(self, filePath):
        np.savetxt(filePath, self.matrix, '%1d', delimiter='')

    # вывод в картинку
    def printfTIFF(self, filePath):
        image = Image.new('RGB', (1296, 1128), 'black')
        iDraw = ImageDraw.Draw(image)
        row = -1
        for i in range(80):
            if i % 8 == 0:
                row += 1
            for j in range(100):
                for w in range(8):
                    for h in range(8):
                        iDraw.point((50 + 12 * j + w, 50 + 12 * i + h + 8 * row), self.NUMtoRGB(self.matrix[i][j]))

        image.save(filePath)

    # вывод палитры
    def printColors(self, filePath):
        image = Image.new('RGB', (220, 158), 'black')
        iDraw = ImageDraw.Draw(image)
        for i in range(8):
            for w in range(8):
                for h in range(8):
                    iDraw.point((50 + 16 * i + w, 50 + h), self.NUMtoRGB(i))
            iDraw.text((50 + 16 * i, 70), '{}'.format(i), (255, 255, 255))
        image.save(filePath)

    # перевод числа в цвет
    @staticmethod
    def NUMtoRGB(num):
        if num == 0:
            return 255, 0, 0
        elif num == 1:
            return 255, 191, 0
        elif num == 2:
            return 127, 255, 0
        elif num == 3:
            return 0, 255, 63
        elif num == 4:
            return 0, 255, 255
        elif num == 5:
            return 0, 63, 255
        elif num == 6:
            return 127, 0, 255
        elif num == 7:
            return 255, 0, 191
