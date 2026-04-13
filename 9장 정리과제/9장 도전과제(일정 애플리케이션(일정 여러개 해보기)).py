# 하나의 일자에 여러개 일정 넣을 수 있게 해보기
'''
입력한 날짜에 일정 넣는 일정관리 프로그램
특정한 날에 여러개 일정 등록가능
기능 메뉴화 --->>1.일정 등록 2.일정 조회 3.종료 
'''
def insert_schedule() :
    
    
    date = input("날짜를 입력하시오 : ")

    job = input("일정을 입력하시오 : ")

    if date not in mydict : #신규 일정
        mydict[date]=[job] #처음부터 리스트 변수로 값을 저장
    else :
        mydict[date].append(job)# 이미 일정이 있는 날짜


def print_schedule() :
    print(f"{mydict}")




mydict = {}
while True :
    
    n = int(input("1.일정등록     2.일정조회    3. 종료"))
    if n == 1 :
        insert_schedule()
    elif n == 2:
        print_schedule()
    elif n == 3 :
        print("프로그램 종료")
        break
    else :
        print("1~3중에 골라주세요")
