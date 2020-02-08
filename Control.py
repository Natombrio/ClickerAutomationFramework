import numpy as np
import win32api
import win32con
import win32gui
import pytesseract
import cv2
import json
from PIL import ImageGrab


pytesseract.pytesseract.tesseract_cmd = r"H:\Tools\Python\Tools\Tesseract\tesseract.exe"


class Screen:
    def getPixelColor(gameScreenCoords, pixel):
        gameScreenIm = Control.Screen.grabScreen(gameScreenCoords)
        gameScreenIm = BRG2RGB(gameScreenIm)
        return gameScreenIm[pixel]

    def getScreenArea():
        topLeft = Mouse.getMouseCoords("Move mouse to top left corner and press enter")
        bottomRight = Mouse.getMouseCoords("Move mouse to bottom right corner and press enter")
        return (topLeft + bottomRight)

    def showGame(gameScreen):
        cv2.imshow("window", gameScreen)

    def __relaToAbs__(absCoords, gameScreenCoords):
        x = gameScreenCoords[0] + absCoords[0]
        y = gameScreenCoords[1] + absCoords[1]
        return (x, y)

    def __absToRela__(absCoords, gameScreenCoords):
        x = absCoords[0] - gameScreenCoords[0]
        y = absCoords[1] - gameScreenCoords[1]
        return (x, y)


    def grabScreen(gameScreenCoords):
        screenGrab = ImageGrab.grab(
            (gameScreenCoords[0], gameScreenCoords[1], gameScreenCoords[2], gameScreenCoords[3]))
        return np.array(screenGrab)

    def BRG2RGB(gameScreen):
        return cv2.cvtColor(gameScreen, cv2.COLOR_BGR2GRAY)


class Modes:
    def findCoords(gameScreenCoords):
        while (True):
            name = input("'qqq' to quit, Enter name of object: ")
            if name == "qqq":
                break
            coords = Control.Mouse.getRelaMouseCoords(name, gameScreenCoords)
            print(coords)



class Mouse:
    def mouseMove(coords):
        win32api.SetCursorPos((coords[0], coords[1]))

    def mouseClick(coords):
        Mouse.mouseMove(coords)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, coords[0], coords[1])
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, coords[0], coords[1])

    def getRelaMouseCoords(prompt, gameScreenCoords):
        absCoords = win32gui.GetCursorPos()
        relaCoords = Screen.__absToRela__(absCoords, gameScreenCoords)
        return relaCoords

    def getMouseCoords(prompt):
        input(prompt)
        return win32gui.GetCursorPos()

class CoordinatePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getPoint(self):
        return (self.x, self.y)

class fileControl:
    def initDict(gameScreenCoords):
        coordDict = {}
        with open("CoordinateMap.json", 'r') as f:
            jsonData = f.read()
            jsonData = json.loads(jsonData)
        return jsonData

class Ocr:
    def checkOcrStrInCoords(coordBox, lookForStr):
        nextBoxIm = Screen.grabScreen(coordBox)
        nextBoxNp = np.array(nextBoxIm)
        if lookForStr in pytesseract.image_to_string(nextBoxNp):
            return True
        else:
            return False
