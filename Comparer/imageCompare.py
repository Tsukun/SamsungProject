import cv2
import numpy as np
import matplotlib.pyplot as plt
#import Server

class ImageDiff:
    def __init__(self, image):
        self.image = image
        self.average = 0

    def MatrixDCT(self):
        dimension = 32
        arr = np.zeros((dimension, dimension))
        arrDCT = np.zeros((dimension, dimension))
        self.image = cv2.resize(self.image, (dimension, dimension), interpolation = cv2.INTER_LANCZOS4)

        for i in range(dimension):
            for j in range(dimension):
                arr[i][j] = np.cos(np.pi / dimension * (j + 1 / 2) * i)

        for i in range(dimension):
            for j in range(dimension):
                for k in range(dimension):
                    arrDCT[i][j] += arr[i, k] * self.image[k, j]

        self.image = arrDCT
        return arrDCT

    def chainsBit(self):
        self.image = cv2.resize(self.image, (8, 8), interpolation=cv2.INTER_LANCZOS4)
        arr = []
        for k in range(8):
            for l in range(8):
                self.average += self.image[k][l]
        self.average /= 64
        for i in range(8):
            for j in range(8):
                if self.image[i][j] < self.average:
                    arr.append(0)
                else:
                    arr.append(1)
        return arr

class Work:
    def __init__(self, image1, image2 ):
        Source_Image = ImageDiff(image1)
        Source_Image.MatrixDCT()

        Diff_Image = ImageDiff(image2)
        Diff_Image.MatrixDCT()

        self.Bits_Different = Diff_Image.chainsBit()
        self.Bits_Source = Source_Image.chainsBit()

    def HammingDistance(self):
        count = 0
        for i in range(64):
            if (self.Bits_Different[i] != self.Bits_Source[i]):
                count += 1
        return count


def viewImage(image, name_of_window="Image Window"):
    image = cv2.resize(image, (256, 256), interpolation=cv2.INTER_LANCZOS4)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

