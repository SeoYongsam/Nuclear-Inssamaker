# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label weekday_run:
    call hide_planner_button
    # 낮 이벤트 넣기 전, 정기적 낮 수업을 위해 새로운 이미지를 첨부했습니다.
    # (이후 강의실 도트나 좀 더 좋은 그림 나오면 수정하겠습니다)
    scene bg lecture_room

    # while문에 논리행 몇 개를 추가해서 낮, 밤 일정을 추가해보았습니다.
    $ i = 1


    while i <= 6:
        $ j = renpy.random.randint(1,3)
        if j == 1:
            call lecture_sleep
        else :
            call lecture

        scene black
        "[i]일차 일정은\n"
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

        scene black
        show phone_night at truecenter
        "[i]일차 밤, SNS를 확인했다."
        $ i += 1

    "일요일 화면으로 돌아갑니다."
    call weekday_schedule_reset
    jump sunday_room
    return

label weekday_schedule_reset:
    $ i = 1
    while i < 7:
        $ day_schedule[i] = 0
        $ i += 1

    $ day = 1
    return
