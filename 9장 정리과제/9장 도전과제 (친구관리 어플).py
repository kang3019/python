'''
리스트를 사용하여 친구의 이름,전화번호,주소(00동)을 관리하는 프로그램 작성,
메뉴 : 신규친구입력(동명이인 ㄱㄴ),이름으로 검색,주소 검색,이름으로 찾아 내용 수정,이름 삭제(같은 이름 여러개인 경우 사용자가 그중 골라서 삭제)
'''

#친구 등록
def insert_friend() :
    name = input("친구이름 : ")
    phone = input("폰번호 : ")
    addr = input("주소(동) : ")
    friend.append([name,phone,addr])

#이름 친구 검색
def search_by_name() :
    inp_name = input("찾을 사람의 이름을 검색해주세요 : ")
    cnt = 0 #이름 있는지 확인

    for name,phone,addr in friend :
        if name == inp_name :
            print(f"번호는 {phone}, 주소는 {addr}입니다")
            cnt += 1 #있는 사람이기에 +1
    if cnt == 0 :
        print("등록되지 않는 이름입니다.")

#주소로 검색하기
def search_by_addr() :
    addr = input("주소(동): ")
    cnt = 0 #해당 주소에 사는 친구 여부 확인용
    
    for i in range(len(friend)) :
        if friend[i][2] == addr :
            print(f"이름:{friend[i][0]}, 폰번호: {friend[i][1]}")
            cnt+= 1
        if cnt == 0 :
            print(f"{addr}에는 사는 친구가 없습니다")

#이름 찾아 내용 수정
def change_by_name() :
    change_index  = []
    cnt = 0

    name = input("정보를 수정할 친구 이름을 입력 : ")

    for i in range(len(friend)) :
        if friend[i][0] == name :
            cnt += 1
            print(f"{cnt}번째 {name}의 친구,폰번호: {friend[i][1]}, 주소: {friend[i][2]} 입니다")
            change_index.append(i)

    if cnt == 0 :
        print("등록되지 않은 이름입니다.")
    elif cnt == 1 :
        friend[0][1] = input("변경할 번호 : " )
        friend[0][2] = input("변경할 주소 : " )
    else :
        answer = int(input("몇번째 친구를 수정할까요? : "))
        friend[answer-1][1] = input("변경할 번호 : " )
        friend[answer-1][2] = input("변경할 주소 : " )

 #이름으로 삭제하기
def delete_by_name() :
    delete_index = [] # 동명이인들의 인덱스값 저장 
    name = input("친구이름: ")
    cnt = 0
    
    for i in range(len(friend)) :
        if friend[i][0] == name :
            print(f"{cnt+1}번 친구 폰번호: {friend[i][1]}, 주소: {friend[i][2]}")
            delete_index.append(i)
            cnt+= 1
            
    if cnt == 0 :
        print("등록되지 않은 이름입니다")
        return
     
    elif cnt == 1 :
       index = delete_index[0]
    else :
       cnt = int(input("몇번 친구를 삭제할까요? "))
       index = delete_index[cnt-1] 
  
    del friend[index]
    
    print("삭제완료")           


# 전체 친구 출력
def all_friend_print() :
    new_list = sorted(friend)
    for i  in  new_list :
        print("%-7s\t%-10s\t%-10s\n" %(i[0], i[1], i[2]))


            



#메세지 지정
msg = "1.친구등록(동명이인 가능), 2.이름으로 검색하기,3.주소로 검색하기,4.이름찾아 내용 수정, 5.이름으로 삭제하기 ,6.전체 출력 7.종료 : "

friend = []

if __name__ == '__main__' :
    while True :
        n = int(input(msg))

        if n == 1 :
            insert_friend()
        elif n == 2 :
            search_by_name()
        elif n == 3:
            search_by_addr()
        elif n == 4:
            change_by_name()
        elif n == 5:
            delete_by_name()
        elif n == 6:
            all_friend_print()
        elif n == 7 :
            print("프로그램 종료")
            break
        else :
            print("1~7중 선택하세요 \n")
