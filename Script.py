import pyautogui, time, os

pyautogui.FAILSAFE = True

#for 16:9 resolution
openPacksButtonPercentages = (0.4052, 0.839)
centerPackPercentages = (0.1932, 0.463)
packOpeningSlotPercentages = (0.576, 0.469)
topCardPercentages = (0.588, 0.251)
leftCardPercentages = (0.4208, 0.3537)
rightCardPercentages = (0.7781, 0.3528)
bottomLeftCardPercentages = (0.4922, 0.7806)
bottomRightCardPerecentages = (0.6922, 0.792)
doneButtonPercentages = (0.5849, 0.5185)

defaultScreenshotFoldername = 'Hearthstone packs'

desktopPath = os.path.join(r"C:\Users",os.getlogin(),'Desktop')
screenshotPath = os.path.join(r"C:\Users",os.getlogin(),'Pictures')
screenshotFolderName = input("Folder name for pack screenshots: ")
if not screenshotFolderName:
   screenshotPath = os.path.join(screenshotPath,defaultScreenshotFoldername)
else:
   screenshotPath = os.path.join(screenshotPath,screenshotFolderName)

if not os.path.exists(screenshotPath):
    os.makedirs(screenshotPath)

packCount = int(input("Enter number of packs to be opened: "))

hearthstoneWindow = pyautogui.getWindow('Hearthstone')
time.sleep(3)


def countCoordinatesOfPoint(percentages):
    try:
        w1,h1,w2,h2 = hearthstoneWindow.get_position()
        x = round(w1 + (w2-w1)*percentages[0])
        y = round(h1 + (h2-h1)*percentages[1])
        return x,y;
    except:
        SystemExit(0)


def clickInWindow(percentages,delay):
    x,y = countCoordinatesOfPoint(percentages)
    pyautogui.moveTo(x,y,delay)
    pyautogui.click()
    return;

#packopening loop
for i in range(packCount):
    #drag pack to opening slot and reveal cards
    clickInWindow(openPacksButtonPercentages,0)
    packx, packy = countCoordinatesOfPoint(centerPackPercentages)
    pyautogui.moveTo(packx,packy,4)
    openingSlotx, openingSloty = countCoordinatesOfPoint(packOpeningSlotPercentages)
    pyautogui.dragTo(openingSlotx,openingSloty,0.5)
    clickInWindow(topCardPercentages,5)
    clickInWindow(leftCardPercentages,0.5)
    clickInWindow(bottomLeftCardPercentages,0.5)
    clickInWindow(bottomRightCardPerecentages,0.5)
    clickInWindow(rightCardPercentages,0.5)
    #go through all cards once again just to be safe
    clickInWindow(topCardPercentages,0.3)
    clickInWindow(leftCardPercentages,0.3)
    clickInWindow(bottomLeftCardPercentages,0.3)
    clickInWindow(bottomRightCardPerecentages,0.3)
    clickInWindow(rightCardPercentages,0.3)
    clickInWindow(topCardPercentages,0.3)
    time.sleep(0.5)
    #take screenshot
    pyautogui.press('printscreen')
    #press 'done' button
    clickInWindow(doneButtonPercentages,0.5)
    #move screenshot from desktop to desired directory
    for file in os.listdir(desktopPath):
        if file.startswith('Hearthstone Screenshot') and file.endswith('.png'):
            os.rename(os.path.join(desktopPath,file),os.path.join(screenshotPath,file))
    print ('{0} of {1} packs have been opened'.format(str(i+1),str(packCount)))
    time.sleep(1)
