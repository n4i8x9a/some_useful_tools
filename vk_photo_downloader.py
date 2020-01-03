import vk_api  # (pip install vk_api)
import time
import os
from threading import Thread
import requests

vk_session1=vk_api.VkApi(token="YOUR_VK_TOKEN_HERE")  # токен пользователя ВК
vk1=vk_session1.get_api()

owid=int(input("input owner id : "))  # ID пользователя или сообщества
alid=str(input("input album id : "))  # ID альбома

c=time.ctime()
c=c.replace(" ","_")
c=c.replace(":","_")
print(c)

os.mkdir(c)

i = 0
z = []

while (True):
    alb_list = []
    alb_list = vk1.photos.get(owner_id=owid, album_id=alid, count=1000, offset=i)['items']
    if (alb_list == []):
        break
    for ff in alb_list:
        z.append(ff)
    # z=z+alb_list
    del alb_list
    print(i)
    i += 1000

i = 0
url_list = []
for i in range(len(z)):
    url_list.append(z[i]['sizes'][-1]['url'])

del z
del alb_list

print('Count of photos : ', len(url_list))


ser1=round(len(url_list)/20)
ser2=2*ser1
ser3=3*ser1
ser4=4*ser1
ser5=5*ser1
ser6=6*ser1
ser7=7*ser1
ser8=8*ser1
ser9=9*ser1
ser10=10*ser1
ser11=11*ser1
ser12=12*ser1
ser13=13*ser1
ser14=14*ser1
ser15=15*ser1
ser16=16*ser1
ser17=17*ser1
ser18=18*ser1
ser19=19*ser1

ttime=0
k=0

def f1():
    print("potok 1")
    global c,url_list,ser1,ser2,ttime,k
    begin=time.time()
    for i in range(0,ser1):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end=time.time()
    ttime+=end-begin
    k+=1

def f2():
    print("potok 2")
    global c, url_list,ser1,ser2,ttime,k
    begin = time.time()
    for i in range(ser1, ser2):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:

            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)

            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f3():
    print("potok 3")
    global c, url_list,ser2,ser3,ttime,k
    begin = time.time()
    for i in range(ser2, ser3):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f4():
    print("potok 4")
    global c, url_list,ser3,ser4,ttime,k
    begin = time.time()
    for i in range(ser3, ser4):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f5():
    print("potok 5")
    global c, url_list,ser4,ser5,ttime,k
    begin = time.time()
    for i in range(ser4, ser5):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f6():
    print("potok 6")
    global c, url_list,ser5,ser6,ttime,k
    begin = time.time()
    for i in range(ser5, ser6):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f7():
    print("potok 7")
    global c, url_list,ser6,ser7,ttime,k
    begin = time.time()
    for i in range(ser6, ser7):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f8():
    print("potok 8")
    global c, url_list,ser7,ser8,ttime,k
    begin = time.time()
    for i in range(ser7,ser8):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f9():
    print("potok 9")
    global c, url_list,ser8,ser9,ttime,k
    begin = time.time()
    for i in range(ser8, ser9):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f10():
    print("potok 10")
    global c, url_list,ser9,ser10,ttime,k
    begin = time.time()
    for i in range(ser9, ser10):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f11():
    print("potok 11")
    global c, url_list,ser10,ser11,ttime,k
    begin = time.time()
    for i in range(ser10,ser11):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f12():
    print("potok 12")
    global c, url_list,ser11,ser12,ttime,k
    begin = time.time()
    for i in range(ser11,ser12):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f13():
    print("potok 13")
    global c, url_list,ser12,ser13,ttime,k
    begin = time.time()
    for i in range(ser12,ser13):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f14():
    print("potok 14")
    global c, url_list,ser13,ser14,ttime,k
    begin = time.time()
    for i in range(ser13,ser14):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f15():
    print("potok 15")
    global c, url_list,ser14,ser15,ttime,k
    begin = time.time()
    for i in range(ser14,ser15):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f16():
    print("potok 16")
    global c, url_list,ser15,ser16,ttime,k
    begin = time.time()
    for i in range(ser15,ser16):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f17():
    print("potok 17")
    global c, url_list,ser16,ser17,ttime,k
    begin = time.time()
    for i in range(ser16,ser17):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f18():
    print("potok 18")
    global c, url_list,ser17,ser18,ttime,k
    begin = time.time()
    for i in range(ser17,ser18):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f19():
    print("potok 19")
    global c, url_list,ser18,ser19,ttime,k
    begin = time.time()
    for i in range(ser18,ser19):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

def f20():
    print("potok 20")
    global c, url_list,ser19,ttime,k
    begin = time.time()
    for i in range(ser19, len(url_list)):
        with open(c + '/' + str(i) + '.jpg', 'wb') as f:
            while True:
                try:
                    re = requests.get(url_list[i])
                    break
                except TimeoutError:
                    time.sleep(2)
            f.write(re.content)
            f.close()
    end = time.time()
    ttime += end - begin
    k+=1

begg=time.time()

t1=Thread(target=f1)
t2=Thread(target=f2)
t3=Thread(target=f3)
t4=Thread(target=f4)
t5=Thread(target=f5)
t6=Thread(target=f6)
t7=Thread(target=f7)
t8=Thread(target=f8)
t9=Thread(target=f9)
t10=Thread(target=f10)
t11=Thread(target=f11)
t12=Thread(target=f12)
t13=Thread(target=f13)
t14=Thread(target=f14)
t15=Thread(target=f15)
t16=Thread(target=f16)
t17=Thread(target=f17)
t18=Thread(target=f18)
t19=Thread(target=f19)
t20=Thread(target=f20)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()
t11.start()
t12.start()
t13.start()
t14.start()
t15.start()
t16.start()
t17.start()
t18.start()
t19.start()
t20.start()

while(k!=20):
    continue
print("Time : ",time.time()-begg)