from time import sleep
from AutomationFramework.Control import *


class Tasks():




#EXAMPLES BELOW
"""
    def _RewardsScreen_(gameScreenCoords):
        if Ocr.checkOcrStrInCoords(Coords.BconfirmRewards(gameScreenCoords), "Next"):
            Mouse.mouseClick(Coords.PconfirmRewards(gameScreenCoords))
            return True
        else:
            return False

    def _Attack_(gameScreenCoords):
        if Ocr.checkOcrStrInCoords(Coords.Battack(gameScreenCoords), "Attack"):
            Mouse.mouseClick(Coords.Pattack(gameScreenCoords))
            return True
        else:
            return False

    def _Death_(gameScreenCoords):
        if Ocr.checkOcrStrInCoords(Coords.BconfirmDeath(gameScreenCoords), "Next"):
            Mouse.mouseClick(Coords.PconfirmDeath(gameScreenCoords))
            sleep(3)
            for i in range(3):
                Mouse.mouseClick(Coords.PdeathYes(gameScreenCoords))
                sleep(0.1)
            return True
        else:
            return False

    def _Combat_(gameScreenCoords):
        while Tasks._RewardsScreen_(gameScreenCoords) is False:
            Tasks._Attack_(gameScreenCoords)
            if Tasks._Death_(gameScreenCoords):
                return "Death"
            sleep(0.5)

    def MoglinForest(gameScreenCoords):
        while True:
            Mouse.mouseClick(Coords.PTwilly(gameScreenCoords))
            sleep(0.1)
            Mouse.mouseClick(Coords.PMoglinForest(gameScreenCoords))
            sleep(0.1)
            Mouse.mouseClick(Coords.PLetsGo(gameScreenCoords))
            sleep(1.3)
            Mouse.mouseClick(Coords.PReady(gameScreenCoords))
            sleep(3)
            while (True):
                if Tasks._Combat_(gameScreenCoords) == "Death":
                    sleep(3)
                    break
                sleep(2)
                Mouse.mouseClick(Coords.PmoglinMore(gameScreenCoords))
                sleep(1)
                Mouse.mouseClick(Coords.PmoglinMore(gameScreenCoords))
"""