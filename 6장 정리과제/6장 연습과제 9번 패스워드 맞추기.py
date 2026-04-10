#알파벳 소문자 3글자 숫자 2글자 패스워드를 만들고
#알아맞추는 프로그램 작성
import sys

user_pass = input("5자리 패스워드(알파벳 소문자 3개, 숫자 2개)를 입력하시오: ")



# 알파벳 소문자 리스트 
alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k',
                 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u','v',
                 'w', 'x', 'y', 'z',]

# 숫자 리스트 
password_num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


try_count = 0

for p1 in alphabet_list:    
    for p2 in alphabet_list: 
        for p3 in alphabet_list: 
            for p4 in password_num:  
                for p5 in password_num:  
                    
                    try_count += 1
                    
                    # 문자열과 숫자를 결합하기 위해 str()로 변환
                    guess = p1 + p2 + p3 + str(p4) + str(p5)
                    
                    # 1000번째 시도마다만 출력하여 진행 상황 출력
                    if try_count % 1000 == 0:
                        print(f"[{try_count}회 시도 중] 현재 시도: {guess}")

                    # 추측한 패스워드가 사용자의 패스워드와 일치하는지 확인
                    if guess == user_pass:
                        print("\n=======================================================")
                        print(f"성공! {try_count}회 시도 끝에 패스워드를 찾았습니다.")
                        print(f"당신의 패스워드는 '{user_pass}' 입니다.")
                        print("=======================================================")
                        
                        sys.exit()

