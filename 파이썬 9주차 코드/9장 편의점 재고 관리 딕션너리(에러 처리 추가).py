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


def insert_item() :
    if len(item_dict) <= 50 : 
        while True :
            item_key = input("물품명을 입력해주세요 : ")
            if item_key not in item_dict.keys() :
                item_dict[item_key] = int(input("재고량을 입력해주세요 : "))
                print("등록완료")
                break
            else :
                print("이미 등록됌!")
                continue
    else :
        print("종류가 50개를 넘었습니다!")
        return


def inc_cut() :
    while True :
        item_key = input("추가 할 물품명을 입력해주세요 : ")
        if item_key not in item_dict.keys() :
            print(f"{item_key}는 없는 물품입니다!")
            continue
        else : 
            item_dict[item_key] += int(input("추가 할 재고량을 입력해주세요 : "))
            print("등록완료")
            break

def dec_cut() :
    while True :
        item_key = input("감소 할 물품명을 입력해주세요 : ")
        if item_key not in item_dict.keys() :
            print(f"{item_key}는 없는 물품입니다!")
            continue
        else : 
            check = int(input("감소  할 재고량을 입력해주세요 : "))
            if item_dict[item_key] - check < 0 :
                print("재고량이 음수가 됩니다.")
                return
            else :
                print("등록완료")
                break

        
def delete_item() :
    item_key = input("삭제 할 물품명을 입력해주세요 : ")
    item_dict.pop[item_key]
    print("삭제완료")


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
            inc_cut()
        elif n == 3 :
            dec_cut()
        elif n == 4 :
            delete_item()
        elif n == 5 :
            all_item_print()
        elif n == 6 :
            print("종료합니다")
            break
        else :
            print("1~6중 택 1 \n")


