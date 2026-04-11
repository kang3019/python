import random as r

#숫자 10개를 랜덤하게 중복 없이 뽑고 최고값을 리턴하는 함수
def find_max() :
    
    while (len(nList) < 10) :
        n = r.randint(1,100)
        if (n not in nList) : # nList에 숫자 n이 있는지 확인
            nList.append(n)
        else :
            continue
    big = nList[0]
    for i in range(1,len(nList)) :
        if big < nList[i] :
            big =  nList[i]
    return big




    
#전역변수 선언 추가로 리스트기 때문에 global 안써도 함수에서 사용 가능    
nList = []

print(f"리스트 중 최고 값은 {find_max()}입니다")

for i in nList :
    print(i)
    

    
        
    









