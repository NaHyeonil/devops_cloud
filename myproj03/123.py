"""
1.반복문을 활용하여, 효과적으로 3단/6단/9단 구구단 출력하기
"""
for 숫자 in range(3, 10, 3):
    print("### {}단 ###".format(숫자))
    for i in range(1, 10):
        계산결과 = 숫자 * i
        print("{} * {} = {}".format(숫자, i, 계산결과))
    print("")

"""
2.1이상 100미만 범위에서 3과 5의 공배수를 모두 출력하기 (공배수 : 2개 이상의 자연수의 공통인 배수)
"""
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

"""
3.1이상 100미만 범위에서 3과 5의 공배수를 합을 출력하기
"""
result = 0
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        result += i

print(result)

"""
4.구구단 퀴즈 break 안 쓴 버전
"""
for number in range(2, 10):
    for i in range(1, 10):
        if number >= i:
            print(f"{number} * {i} = {number * i}")


for number in range(2, 10):
    for i in range(1, number + 1):
        print(f"{number} * {i} = {number * i}")