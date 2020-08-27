from skimage.filters import threshold_local
from argparse import ArgumentParser
from imutils import grab_contours
from imutils import is_cv2
from imutils import paths
from time import time
import numpy as np
import cv2
import os

ap = ArgumentParser()
ap.add_argument('-d', '--dataset', required = True)
ap.add_argument('-o', '--option', required = False, default = 'f')
opt = ap.parse_args()

def otsu(img):
    fileName = img.split(os.path.sep)[-1]
    os.makedirs('bin', exist_ok=True)

    sTime = time()
    (T, threshInv) = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    otsu = cv2.bitwise_and(img, img, mask=threshInv)

    print(f'otsu : {time() - sTime:.4f}')
    cv2.imwrite(f'bin/{fileName}', otsu)

def edgeCanny(img):
    fileName = img.split(os.path.sep)[-1]

    wide = cv2.Canny(img, 10, 200)
    print(f'canny wide : {time() - sTime:.4f}')

    mid = cv2.Canny(img, 30, 150)
    print(f'canny mid : {time() - sTime2:.4f}')

    tight = cv2.Canny(img, 240, 250)
    print(f'canny tight : {time() - sTime3:.4f}')

    os.makedirs('edge/wide', exist_ok = True)
    os.makedirs('edge/mid', exist_ok = True)
    os.makedirs('edge/tight', exist_ok = True)

    cv2.imwrite(f'edge/wide/{fileName}', wide)
    cv2.imwrite(f'edge/mid/{fileName}', mid)
    cv2.imwrite(f'edge/tight/{fileName}', tight)

def AdaptiveBin(img, idx):
    fileName = img.split(os.path.sep)[-1]
    os.makedirs('adap/cv', exist_ok = True)
    os.makedirs('adap/sci', exist_ok=True)

    sTime = sTime2 = time()
    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
    print(f'{idx}. \nadap cv method : {time() - sTime:.4f}')

    T = threshold_local(img, 29, offset=5, method="gaussian")
    thresh2 = (blurred < T).astype("uint8") * 255
    print(f'adap sci method : {time() - sTime2:.4f}')

    cv2.imwrite(f'adap/cv/{fileName}', thresh)
    cv2.imwrite(f'adap/sci/{fileName}', thresh2)

def adapArea(img):

    os.makedirs('cont/cv', exist_ok=True)
    os.makedirs('cont/sci', exist_ok=True)

    oriImg = img.copy()
    cvImg = img.copy()
    sciImg = img.copy()

    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = grab_contours(cnts)

    cvAreas = []

    if len(cnts) >= 1:
        for c in cnts:
            cvArea = cv2.contourArea(c)
            cvAreas.append(cvArea)

            cv2.drawContours(cvImg, [c], -1, (0, 255, 0), 1)
        
        stack = np.hstack([oriImg, cvImg])
        cv2.imwrite(f'cont/cv/{fileName}.jpg', stack)
    else:
        cvAreas.append(0.0)

    T = threshold_local(img, 29, offset=5, method="gaussian")
    thresh2 = (img < T).astype("uint8") * 255

    cnts = cv2.findContours(thresh2.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = grab_contours(cnts)
    sciAreas = []
    
    if len(cnts) >= 1:
        for c in  cnts:
            sciArea = cv2.contourArea(c)
            sciAreas.append(sciArea)

            cv2.drawContours(sciImg, [c], -1, (0, 255, 0), 1)

        stack = np.hstack([oriImg, sciImg])
        cv2.imwrite(f'cont/sci/{fileName}.jpg', stack)
    else:
        sciAreas.append(0.0)

    return max(cvAreas), max(sciAreas)

def otsuArea(img):

    (_, threshInv) = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    otsu = cv2.bitwise_and(image, image, mask=threshInv)
    cnts = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = grab_contours(cnts)

    areas = []

    if cnt >= 1:
        for c in  cnts:
            area = cv2.contourArea(c)
            areas.append(area)
    else:
        areas.append(0.0)

    return max(areas)

def adapRotate(option, *args):

    path = 'rotate/real' if option.upper() == 'T' else 'rotate/fake'

    os.makedirs(path, exist_ok=True)
    gray = args[0].copy()

    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 25, 15)
    conts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    conts = grab_contours(conts)

    clone = args[1].copy()
    for cont in conts:
        box = cv2.minAreaRect(cont)
        x, y, theta = box
        box = np.int0(cv2.BoxPoints(box) if is_cv2() else cv2.boxPoints(box))
        cv2.drawContours(clone, [box], -1, (0, 255, 0), 1)

        print(f'x1 : {x[0]:.2f}, x2: {x[1]:.2f} \ny1 : {y[0]:.2f}, y2 : {y[1]:.2f}\ntheta : {theta:.2f}\n')
    
    cv2.imwrite(f'{path}/{fileName}.jpg', clone)

if __name__ == '__main__':
    imgpath = list(sorted(paths.list_images(opt.dataset)))
    for (idx, img) in enumerate(imgpath):
        image = cv2.imread(img)

        image = image[370: 382, 299: 317]
        fileName = img.split(os.path.sep)[-1].replace('.jpg', '')
        print(fileName)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        #* test codes *#
        # adapRotate(opt.option, gray, image)

        # otsu(img)
        # edgeCanny(img)
        # AdaptiveBin(img, idx)
        cvArea, sciArea = adapArea(blurred)
        print(sciArea)
        # otsuArea(img)
        cv2.waitKey(1)

