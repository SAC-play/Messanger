import time
import threading
 
#함수 정의, 함수 내부에 threading 정의
def printhello():
    input("to fishish this program input enter")
    print("greetings!")
    
    #threading을 정의한다. 5초마다 반복 수행함.
    threading.Timer(5, printhello).start()
 
#printhello 
printhello()


import time
import schedule #
 
#특정 함수 정의
def printhello():
    print("Hello!")
 
 
schedule.every(30).minutes.do(printhello) #30분마다 실행
schedule.every().day.at("09:30").do(printhello) #월요일 00:10분에 실행
schedule.every().day.at("15:30").sleep(job) #매일 10시30분에 
 
#실제 실행하게 하는 코드
while True:
    schedule.run_pending()
    time.sleep(1)


