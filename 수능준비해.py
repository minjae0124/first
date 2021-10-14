from datetime import datetime
import time
test = datetime(2022,11,17,00,00,00)
today = datetime.today()
time.sleep(2)
print(f"우리 수능 남은시간 계산하면{(test-today).days}일 남았다")
time.sleep(2)
print("시간 계속 가고있어..")
time.sleep(2)
while(1):
    today = datetime.today()
    print(f"{(test-today).days}일",end="")
    time.sleep(1)
    print(f"{(test-today).seconds}초")
    time.sleep(1)