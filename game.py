print("\t 갤러그 게임 시작")
print("====================================")

print("\t    게임 설명") ##게임 설명
print("1. 적 비행기가 출현하면 미사일로 격추시키세요")
print("2. 적 비행기가 미사일을 쏘면 반대방향으로 움직여 피하세요.")
print("3. 게임을 종료하려면 4를 입력해 종료하세요")
print("4. 1,2,3,4 숫자외에 다른 키를 입력하면 게임이 종료됩니다.")
print("====================================")
print("")

event = {
    '적 비행기 출현!' : '1',
    '적 비행기가 왼쪽으로 미사일 발사!' : '2',
    '적 비행기가 오른쪽으로 미사일 발사!' : '3'
}


def game(computer, mine):
    result = '0'
    if event[computer] == '1' and mine == '1' :
        result = '적비행기를 격추시켰습니다!'
        return result
    elif event[computer] == '2' and mine == '2' :
        result = '미사일을 피했습니다!'
        return result
    elif event [computer] == '3' and mine == '3' :
        result = '미사일을 피했습니다.'
        return result
    else :
        result = '공격을 당했습니다. 게임오버...'
        return result

while True :
    import random
    list = ['적 비행기 출현!', '적 비행기가 오른쪽으로 미사일 발사!', '적 비행기가 왼쪽으로 미사일 발사!']
    enemy = random.choice(list)
    print('{}'.format(enemy))
    print('')
    print('1.미사일 발사 2.오른쪽이동 3.왼쪽이동 4.종료')
    number = input('숫자를 입력하세요: ')

    if number == '4' :
        break
    elif (number != '1') and (number != '2') and (number != '3') and (number != '4') :
        print('올바른 값을 입력하세요.')
        print('게임오버...')
        break
    else : 
        print('당신의 입력값? ', number)
        print('{}'.format(game(enemy, number)))
        print('')
        print('게임을 계속 진행합니다.')
    print('--------------------------')

print('게임을 종료합니다. ')