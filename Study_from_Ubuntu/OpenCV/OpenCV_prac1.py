import cv2
import numpy as np
import matplotlib.pyplot as plt

class compareImg:

    def __init__(self):
        pass

    def readImg(self, filepath):
        img = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
        cv2.namedWindow("root", cv2.WINDOW_NORMAL)
        cv2.imshow("root", img)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()
        return img

    def diffImg(self, img1, img2):

        orb = cv2.ORB_create()
        kp1, des1 = orb.detectAndCompute(img1, None)
        kp2, des2 = orb.detectAndCompute(img2, None)

        bf = cv2.BFMatcher(cv2.NORM_HAMMING, croosCheck = True)
        matches = bf.match(des1, des2)
        matches = sorted(matches, key = lambda x:x.distance)

        bf = cv2.BFMatcher()
        matches = bf.knnMatch(des1, des2, k=2)

        good = []
        for rep, rep2 in matches:
            if rep.distance < 0.75 * rep2.distance:
                good.append([m])

        knn_img = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good, NOne, flags =2)
        plt.imshow(knn_img)
        plt.show()

    def run(self):

        path1 = r"/home/kimhippo/바탕화면/Python Practice/Python Practice from Ubuntu/OpenCV/Homer_Simpson_2006.png"
        path2 = r"/home/kimhippo/바탕화면/Python Practice/Python Practice from Ubuntu/OpenCV/Homer_Simpson_2.png"
        img1 = self.readImg(path1)
        img2 = self.readImg(path2)

        self.diffImg(img1, img2)


if __name__ == '__main__':
    cImg = compareImg()
    cImg.run()




