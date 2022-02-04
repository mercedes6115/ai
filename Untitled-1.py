# %%
print("hello world")

# %%
import datetime

now=datetime.datetime.now()

if(now.hour >= 12):
    print(f'현재 시각은 {now.hour}시 {now.minute}분 오후입니다')
else:
    print(f'현재 시각은 {now.hour}시 {now.minute}분 오전입니다')

# %%
i=0
while True:
    print(f'{i}번째 반복입니다.')
    i+=1
    
    inp=input('종료할까요')
    if inp in['y','Y']:
        print('종료')
        break

# %%
print("i wanna ")

# %%
#enumerate 열거함수

student=['진구','철수','미애','형구','진수']

for i,j in enumerate (student):
    print(f'{i}번 {j}')

