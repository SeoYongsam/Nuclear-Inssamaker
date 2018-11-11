# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# 4월 1일 교복데이 이벤트

#이미지 선언
image gyobok = im.Scale("gyobok.jpg", 1280, 720)

# week5 day 1
label uniform:
    $i = 1
    while i <= 6:
        #if day == 30:

        "오늘은 만우절이다. 과 동기들이 다같이 교복을 입고 등교를 했다."
        "과 동기들이 점심식사를 함께 야외에서 배달음식을 먹자고 한다."
        "하지만 약속한 시간에 수업이 있다. 어떻게 할까?"

        menu:
            "수업을 째고 동기들과 점심을 먹으러 간다":
                #hp & 공부 파라미터-, 과 파라미터 up, 개별 캐릭터와 파라미터는 변함이 없고 과 친밀도가 올라감
                "수업을 쨌다."
                scene gyobok at truecenter
                "친구들이 점심 메뉴를 두고 의견이 갈리고 있다. 내가 나서서 정해야겠다."
                menu:
                    "짜장면, 짬뽕":
                        #장중이 + 삼용 파라미터 +
                        scene jjangge at truecenter
                        "짜장면을 시켰다."
                        "서비스로 탕수육과 군만두도 같이 와서 다양한 음식을 먹을 수 있었다."
                        "장중이는 어제 술을 마셨는지 짬뽕으로 해장을 하는 것 같다."
                        "삼용이도 오랜만에 중국 음식을 먹어서 그런지 기분이 좋은것 같다."
                        "아, 짜장면은 중국음식이 아니었지?"

                    "피자":
                        #진일이 + 현재 파라미터 +
                        scene pizza at truecenter
                        "피자를 시켰다."
                        "여러 종류의 피자를 시켜 먹어서 다양하게 먹을 수 있었다."
                        "진일이는 앞으로 착하게 살기로 한다며 피자를 종류별로 1개씩만 먹는다고 한다."
                        "참고로 피자 종류는 5가지지만 한명당 3조각만 먹을수 있다."
                        "현재가 미래에게 피자를 먹여주는게 보인다. 이래서 피자를 시키자고 한건가? 눈에 습기가 찬다."

                show phone_night at truecenter
                "[i]일차 밤, SNS를 확인했다."
                scene bg lecture_room
                $ i += 1

            "수업을 듣는다":
                jump weekday_run

    return
