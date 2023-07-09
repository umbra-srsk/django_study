from random import randint

class GawiBawiBoException(Exception):
    def __int__(self):
        pass


def game_process(player_num):
    computer_num = randint(1, 3)
    prn = {1: '가위', 2:'바위', 3:'보'}
    print(f'player:{prn[player_num]} vs computyer:{prn[computer_num]}')

    if(player_num - computer_num) in [1, 2]:
        print('당신이 이겼습니다')
    elif player_num == computer_num :
        print('비겼습니다')
    else:
        print('당신이 졌습니다')


def play():
    while True:
        try:
            player_num = int(input('가위:1 / 바위:2 / 보:3 / 게임 종료:4 \n 숫자를 입력하세요 '))
            if player_num not in [1, 2, 3, 4]:
                raise GawiBawiBoException()
            if player_num == 4:
                print("제밌으셨나여")
                break

        except ValueError:
            print('숫자만 입력')

        except GawiBawiBoException:
            print('1, 2, 3, 4 중에 하나만 입력')

        except:
            print('관리자에게 문의')
            break

        else:
            game_process(player_num)
    
    print("다음에 또 놀러오세요")

if __name__ == '__main__':
    play()