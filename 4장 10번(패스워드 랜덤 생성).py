#10.알파벳 소문자와 숫자중에서 3글자를 랜덤으로 선택해 패스어드 생성
#(random 라이브러리 사용,random.choice(리스트명)->리스트에서 랜덤으로 하나 선택)

#랜덤 라이브러리 호출 후 r로 별명
import random as r

list_p = ['a','b','c','d','e','f','g','h','i','j','k',
          'l','m','n','o','p','q','r','s','t','u','v',
          'w','x','y','z','1','2','3','4','5','6','7','8','9']

#숫자를 받아올지도 모르니까 문자열로 변환
p1 = str(r.choice(list_p))

p2 = str(r.choice(list_p))

p3 = str(r.choice(list_p))

print(f"생성된 패스워드 : {p1+p2+p3}")
