def coffee(quantitiy, price):
    change = price - (200 * quantitiy)
    if change >= 0:
        prn(quantitiy, change)
    else :
        prn()


def prn(quantitiy=0, change=0):
    if quantitiy == 0 & change == 0:
        print('돈이 부족')
    else:
        print(f'커피{quantitiy}잔이 나왔습니다 \n 잔돈 {change}원이 나왔습니다')


def start():
    q = input('커피 몇 잔이 필요하신가요?')
    p = input('돈을 넣어주세요 (1잔당 200원)')
    coffee(int(q), int(p))




# __name__:해당 파일이 실행됬을 때 이름저장
# 외부에서 import 해서 실행 되는 경우: 파일이름
# 파일이 직접 실행 되는 경우 : "__main__"
if __name__ == '__main__':
    # 프로그램의 주 진입점
    start()