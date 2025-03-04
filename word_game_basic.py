from pygame import mixer
mixer.init() #미디어 파일을 사용하기 위한 초기화

mixer.music.load('assets/good.wav') #소리파일 path
mixer.music.play()

mixer.music.load('assets/bad.wav') #소리파일 path
mixer.music.play()

import random
import time
def gamerun():

# 텍스트 파일 경로
    file_path = "data/word.txt"
    words = []

# 파일 열기
    with open(file_path, 'r', encoding='utf-8') as file:
    # 파일의 각 줄을 리스트로 저장
        words = file.readlines()

# 각 줄의 앞뒤 공백 제거
        words = [line.strip() for line in words]

        correct_count = 0
        start_time = time.time()

        for i in range(5):
            # 임의의 단어 선택 (리스트에서 하나를 랜덤으로 선택)
            a = random.choice(words)

            print(f"Question #{i+1}: {a}")

            user_input = input("준비됐으면 문자를 입력하세요: ").strip()

            if user_input == a:
                print("정답")
                correct_count += 1
            else:
                print("오답")

    end_time = time.time()
    b_time = end_time - start_time

    if correct_count >= 3:
        print("합격입니다.")
        mixer.music.load('assets/good.wav') #소리파일 path
        mixer.music.play() # 합격이면 good 소리 재생
    else:
        print("불합격입니다.")
        mixer.music.load('assets/bad.wav') #소리파일 path
        mixer.music.play()


    print(f"게임 걸린 시간 : {b_time}초  맞춘 개수: {correct_count}개")

words = gamerun()
