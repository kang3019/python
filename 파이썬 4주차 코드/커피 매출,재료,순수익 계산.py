#커피 단가 입력받기
americano_price = int(input("아메리카노 1잔의 가격 : "));

cafelatte_price = int(input("카페라떼 1잔의 가격 : "));

capucino_price = int(input("카푸티노 1잔의 가격 : "));
print()

#커피 판매 갯수 입력받기
americanos = int(input("아메리카노 판매 개수: "))

cafelattes = int(input("카페라떼 판매 개수: "))

capucinos = int(input("카푸치노 판매 개수: "))
print()


#총매출 계산
sales = americanos*americano_price
sales = sales + cafelattes*cafelatte_price
sales = sales + capucinos*capucino_price

#재료비 계산
cost = americanos*1000
cost += cafelattes*1000
cost += capucinos * 1000
#순수익 계산
onlySales = sales - cost

print("총 매출은", sales, "입니다.")
print("총 재료비는", cost, "입니다.")
print("순수익은", onlySales, "입니다.")
