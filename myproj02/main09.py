import random
import time


animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
]

input("준비 되셨으면, 엔터키를 입력해주세요.")

random.shuffle(animal_names)

begin_time = time.time()

ok_counter = 0

# for count in range(5):
#     random_name = random.choice(animal_names)
# 방법1 : 이미 사용된 random_namedmf 받았다면 다시 가져오는 것.
for random_name in animal_names[0:9]:
    print(random_name)
    line = input(">>> ")
    if random_name == line:
        ok_counter += 1
        print("정확합니다.")
    else:
        print("오타가 있어요.")

end_time = time.time()

print(f"{ok_counter}번 성공하셨습니다.")
print(f"총 {end_time - begin_time}초가 걸리셨어요.")
print(f"분당 {38/(end_time - begin_time)*60}타 입니다.")