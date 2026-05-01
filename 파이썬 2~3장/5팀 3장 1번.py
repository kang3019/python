#사용자에게 초값을 입력받아 시간,분,초로 변환 출력

#사용자로부터 입력받기
sec = int(input("변환할 초를 입력해주세요 : "))

#시간 변환
hour = sec // 3600

remain_time = sec % 3600

min = remain_time // 60

remain_sec = remain_time%60

print("입력한",sec,"초는", hour ,"시간",min,"분",remain_sec,"초")

#소스를더블 클릭해서 실행한 경우에 실행창이 자동으로 닫히는걸 방지
input()
