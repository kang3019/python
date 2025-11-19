'''
사용자에게 2이상의 정수 n과 연산자는 둘(+,*)중 하나를 입력받기
연산자가 곱이면 1~n까지 곱 계산
연산자가 더하기면 1~n까지 합 계산
결과값 화면 출력
함수 사용하기 전과 후 비교
'''


'''
#1번 요구
num= int(input("2 이상의 정수 입력"))
op = input("+,*중 하나 입력")



#2번 요구
if op == "+" :
    result = 0 #초기화
    for i in range(1,num+1) :        
        result += i
    print(num,"까지의 숫자 합은",result)

elif op == "*" :
    result = 1 #초기화
    for j in range(2,num+1) :
        result *= j
    print(num,"까지의 숫자 곱은",result)

else :
    print("잘못된 연산자 입력")
'''

#====== 3번 요구사항
#합 함수
def hap(n) :
    result = 0
    for i in range(1,n+1) :
        result += i
    return result
#곱하기 함수
def mult(n) :
    result = 1
    for i in range(2,n+1) :
        result *= i
    return result
    

num= int(input("2 이상의 정수 입력 : "))
op = input("+,*중 하나 입력")

if op == "+" :
    print(hap(num))

elif op == "*" :
    print(mult(num))
else :
    print("연산자 오류")
