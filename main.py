import cv2
import numpy as np
import time
import pytesseract
from AutomationFramework import Control
from AutomationFramework import GameScenes


pytesseract.pytesseract.tesseract_cmd = r"H:\Tools\Python\Tools\Tesseract\tesseract.exe"



def main():
    gameScreenCoords = Control.Screen.getScreenArea()
    CoorDict = Control.fileControl.initDict(gameScreenCoords)
    GameScenes.Tasks.MoglinForest(gameScreenCoords)
    findCoords(gameScreenCoords)






#Examples below
"""    while (True):
        gameScreenIm = Control.Screen.grabScreen(CoordinateMap.Coords.BconfirmFailure(gameScreenCoords))
        gameScreenNp = np.array(gameScreenIm)
        gameScreenNp = BRG2RGB(gameScreenNp)
        showGame(gameScreenIm)
        print(pytesseract.image_to_string(gameScreenNp))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break



    nextBoxIm = Control.Screen.grabScreen(CoordinateMap.Coords.BconfirmFailure(gameScreenCoords))
    nextBoxNp = np.array(nextBoxIm)
    txt = pytesseract.image_to_string(nextBoxNp)
    time.sleep(2)
"""


if __name__ == '__main__':
    main()
