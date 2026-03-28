'''5. 두 개의 정수를 입력받아 계산 연산자 출력하는 프로그램 작성
      (파이썬에서 제공하는 내장 함수 max(x,y),min(x,y)도 사용해보자)'''
## 1번째 방법
## 변수 입력받기
x = int(input("x 값을 입력하시오. "))
y= int(input("y 값을 입력하시오. "))

print(f"두수의 합 : {x + y}")
print(f"두수의 차 : {x - y}")
print(f"두수의 곱 : {x * y}")
print(f"두수의 평균 : {(x + y)/2}")
print(f"두수의 큰수 : {max(x, y)}")
print(f"두수의 작은수 : {min(x,  y)} \n \n")


## 2번쨰 방법 (리스트를 활용하여 변수가 아무리 추가 되어도 평균을 구하기 쉽게)
print("2번째 풀이(리스트 활용) \n")
x = int(input("x 값을 입력하시오. "))
y= int(input("y 값을 입력하시오. "))
z = int(input("z값을 입력하시오. "))

#공백 리스트 생성
list_num = []

#공백 리스트에 추가
list_num.append(x)
list_num.append(y)
list_num.append(z)
print(list_num)

#리스트 안 숫자를 더한 값을 반환하는 함수
total_sum = sum(list_num)
#리스트 길이를 반환하는 함수
count = len(list_num)
avg = total_sum/count


print(f"입력한 변수 갯수 : {count}")
#f-String 변수의 소수점을 2자리만 반환 
print(f"변수들의 평균 : {avg:.2f}")

