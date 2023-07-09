#match ~ case
#3.10 ~


a = input('1 ~ 3 사이의 숫자 입력 :')
match a:
    case "1":
        print("one")
    case "2":
        print("two")
    case "3":
        print("three")


season = 3
match season:
    case 12 | 1 | 2:
        print("겨울")
    case 3 | 4 | 5:
        print("봄")
    case 6 | 7 | 8:
        print("여름")
    case 9 | 10 | 11:
        print("가을")
    case _:
        print("1 ~ 12 사이의 값을 입력")


for _ in range(10):
    print("hello world")
# _ 언더바는 굳이 값을 사용할 필요 없을때