# 1) 아아 : 2000 2) 라떼 : 2500
drinks = ["아이스 아메리카노" , "카페 라떼"]
prices = [1500, 2500]

while True:
    menu = input(f"1) {drinks[0]} {prices[0]}  2) {drinks[1]} {prices[1]} 3) 주문종료 : ")
    if menu == "1":
        print("아이스 아메리카노를 주문하셨습니다. 가격은 2000원 입니다")
    elif menu == "2":
        print("카페 라떼를 주문하셨습니다. 가격은 2500원 입니다")
    elif menu == "3":
        print("주문을 종료합니다")
        break
    else:
        print(f"{menu}번 메뉴는 존재하지 않습니다. 아래 메뉴에서 골라주세요")

print(f"총 주문 금액 : {total_price}원")