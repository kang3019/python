'''
<편의점 재고 관리 프로그램>

1.재고관리 정보를 저장할 빈 딕셔너리 변수를  만듦
2.신규 물품명과 재고량을 입력받는다


3. 메뉴 : 1.신규 물품 재고 등록, 2.특정 물품 재고량 증가, 3.재고량 감소
          4.물품 삭제, 5.전체 물품 출력, 6. 종료

- 에러체크1 : 관리하는 물품 종류 수 50개 넘을 수 없음 - 완
- 에러체크2 : 신규 물품 등록할 때 이미 등록된 물품이면 에러처리 - 완
- 에러체크3 : 재고량 증가/감소,물품 삭제 전 등록된 물품인지 확인
- 에러체크4 : 재고량 감소시 재고량 음수면 안됌
'''

def item_key_check(flag) :
    while True :
        item_key = input("물품명 : ")
        if flag == 0 and item_key in item_dict.keys() :
            print("이미 있는 물품임!")
            continue
        elif flag == 1 and item_key not in item_dict.keys() :
            print(f"{item_key}는 없는 물품임!")
            continue
        else : #요구 조건에 맞는 물품명을 입력한 경우
            break
    return item_key


#신규 물품 등록
def insert_item() :
    if len(item_dict) >= 50 : 
        print("종류가 50개를 넘었습니다!")
        return

    item_key = item_key_check(0)

    item_dict[item_key] = int(input("재고량 : "))


#물품 재고량 증가
def inc_cnt() :
    item_key = item_key_check(1)
    inc_cnt = int(input("재고 증가량 : "))
    item_dict[item_key] += inc_cnt


#물품 재고량 감소
def dec_cnt() :
    item_key = item_key_check(0)
    dec_cnt = int(input("재고 감소량 : "))
    if item_dict[item_key] - dec_cnt < 0 :
        print("재고량이 음수가 됩니다")
        return
    item_dict[item_key] -= dec_cnt

#물품 삭제       
def delete_item() :
    item_key = item_key_check(1)
    item_dict.pop[item_key]
    print("삭제완료")

#물품 출력
def all_item_print() :
    for item_key in sorted(item_dict.keys()) :
        print("%7s\t%5d" %(item_key,item_dict[item_key]))

#전역변수 생성
msg = "1.물품등록 2.재고량 증가 3.재고량 감소 4.물품 삭제 5.전체물품 출력 6.종료 : "
item_dict = {}



if __name__=='__main__' : #파이썬에서는 main()함수를 따로 지정하지 않아도 되므러 여기서부터 실행문장 시작이라는 뜻의 관용구

    while True :
        n = int(input(msg))

        if n == 1 :
            insert_item()
        elif n == 2 :
            inc_cnt()
        elif n == 3 :
            dec_cnt()
        elif n == 4 :
            delete_item()
        elif n == 5 :
            all_item_print()
        elif n == 6 :
            print("종료합니다")
            break
        else :
            print("1~6중 택 1 \n")


