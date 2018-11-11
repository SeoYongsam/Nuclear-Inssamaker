# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#피시방 이벤트

#이미지 선언
image pcbang = im.Scale("pcbang.jpeg", 1280, 720)

#label pcbang:
label pcbang:

    $ i = 1
    while i <= 6:
        "[i]일차 낮, 강의실에서 수업을 들었다."

        scene black

        "[i]일차 일정은\n"
#        if day ==
        extend "갑자기 대현이가 현재, 미래, 그리고 진일이와 함께 게임을 하러 PC방에 가자고 한다."
        "가게 되면 오늘 오후 스케줄은 계획대로 진행하지 못하는데... 어떡할까?"

        menu:
            "PC방에 같이 가서 게임을 한다":
                scene pcbang at truecenter
                "결국 친구들이랑 PC방에 같이 갔다"
                "5명이서 같이 할 수 있는 게임으로는 '리그 오브 레전드' 가 최고라며 팀 게임을 같이 했다."
                "재밌게 한 것 같다."
                "다만 내가 잘 못해서 자주 죽었는데 친구들이 게임을 잘해서 자주 이긴 것 같다. 왠지 죽을 때 마다 진일이 표정이 조금 씩 굳어지는 것 같았지만 내 상상인것 같다."

                show phone_night at truecenter
                "[i]일차 밤, SNS를 확인했다."

                return


            "정중히 거절하고 예정된 계획대로 하루를 보낸다":
                pause

                return

        if day_schedule[i] == 1:
            extend "공부했다"
        elif day_schedule[i] == 2:
            extend "동아리 연습했다"
        elif day_schedule[i] == 3:
            extend "과활동했다"
        elif day_schedule[i] == 4:
            extend "휴식했다"
        else :
            extend "에러"

        show phone_night at truecenter
        "[i]일차 밤, SNS를 확인했다."

        scene bg lecture_room
        $ i += 1

    "일요일 화면으로 돌아갑니다."
    call weekday_schedule_reset
    jump sunday_room

    return
