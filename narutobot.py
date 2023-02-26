import pyautogui as pg
import time
from AppOpener import open
count=0
r_count=0
time.sleep(2)
#open discord app
open("discord")
time.sleep(2)
while True:
        option1 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option1.png",region=(312,377,1340,788))
        option2 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option2.png",region=(312,377,1340,788))
        option3 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option3.png",region=(312,377,1340,788))
        if count <10:       
                count = count + 1
                print(count)                   
                pg.typewrite("n m")
                pg.hotkey('enter')

                time.sleep(5)
                option1 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option1.png",region=(312,377,1340,788))
                option2 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option2.png",region=(312,377,1340,788))
                option3 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option3.png",region=(312,377,1340,788))
                organic1 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\organic1.png",region=(312,377,1340,788))
                if organic1 is not None:
                        print("organic 1 found")
                        pg.moveTo(option1)
                        pg.click(interval=1)
                organic2 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\organic2.png",region=(312,377,1340,788))
                if organic2 is not None:
                        print("organic 2 found")
                        pg.moveTo(option2)
                        pg.click(interval=1)
                organic3 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\organic3.png",region=(312,377,1340,788))
                if organic3 is not None:
                        print("organic 3 found")
                        pg.moveTo(option3)
                        pg.click(interval=1)
                time.sleep(60)
        
        if count == 10:
                r_count=r_count+1
                print("report")
                print(r_count)
                print("resetting counter")
                count = 0
                pg.typewrite("n r")
                pg.hotkey('enter')
                time.sleep(9)
                option1 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option1.png",region=(312,377,1340,788))
                option2 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option2.png",region=(312,377,1340,788))
                option3 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\option3.png",region=(312,377,1340,788))

                report1 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\report1.png",region=(312,377,1340,788),confidence=0.99)
                if report1 is not None:
                        print("report 1 found")
                        pg.moveTo(option1)
                        pg.click(interval=1)

                report2 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\report2.png",region=(312,377,1340,788),confidence=0.99)
                if report2 is not None:
                        print("report 2 found")
                        pg.moveTo(option2)
                        pg.click(interval=1)
                        

                report3 =pg.locateCenterOnScreen(r"C:\Users\shwet\Desktop\report3.png",region=(312,377,1340,788),confidence=0.99)
                if report3 is not None:
                        print("report 3 found")
                        pg.moveTo(option3)
                        pg.click(interval=1)

        



        




