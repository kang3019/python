'''사용자에게 이름,나이,주소를 입력받아 리스트 원소를 저장하기
f String에서 출력하기'''

#공백 리스트 생성
info_list = []

#이름 입력받기
name = input("당신의 이름을 입력해주세요 : ")

age = int(input("당신의 나이를 입력해주세요 : "))

addr = input("당신의 주소를 입력해주세요 : ")

#공백 리스트에 결과 값을 추가함
info_list.append(name)

info_list.append(age)

info_list.append(addr)


#결과를 보면 리스트 타입이 다른걸 알 수 있는데 다른 언어는 불가능
print(info_list)


print(f"이름은 {info_list[0]} \n나이는 {info_list[1]} \n사는 지역은 {info_list[2]}")
