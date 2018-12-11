#Created by TEMAL Chakib macbookpro on 11/12/2018.

from urllib.request import urlopen
import datetime
import time
import threading

bufferHTTPStrings = []
urlString = ""

def sendToServerInTime() :
    global urlString
    global bufferHTTPStrings
    while True:
        try:
            time.sleep(1)
            id = 299
            times = str(datetime.datetime.now())
            dt = ('%'.join(times.split(' ')))
            nc = 33
            st = 77
            var1 = 145003
            urlString = "http://www.mmi.iutmulhouse.uha.fr/einsert.php?id=" \
                        + str(id) + "&dt=" + dt + "&nc=" + str(nc) + "&st=" + str(st) + "&var1=" + str(var1)

            urlopen(urlString)
            print("TH1 sended : " + urlString)
        except Exception as e:
            print('TH1 : HTTPError = not sended')
            bufferHTTPStrings.append(urlString)
            print(len(bufferHTTPStrings))
        finally:
            time.sleep(1)

def sendDataToServerLate() :
    global bufferHTTPStrings
    while True:
        if len(bufferHTTPStrings) > 0 :
            for i in range(0, len(bufferHTTPStrings)):
                try:
                    print("TH2 try to send the late... : " + bufferHTTPStrings[i])
                    urlopen(bufferHTTPStrings[i])
                    print("TH2 Sended " + bufferHTTPStrings[i])
                    bufferHTTPStrings.remove(bufferHTTPStrings[i])
                except Exception as e :
                    pass
                finally:
                    time.sleep(1)

try:
    t = threading.Thread(name='sendToServerInTime', target=sendToServerInTime)
    t2 = threading.Thread(name='sendDataToServerLate', target=sendDataToServerLate)

    t.start()
    t2.start()
except:
   print ("Error: unable to start thread")
