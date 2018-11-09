# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label weekday_run:
    hide screen sunday_room_UI
    call hide_planner_button
    # 낮 이벤트 넣기 전, 정기적 낮 수업을 위해 새로운 이미지를 첨부했습니다.
    # (이후 강의실 도트나 좀 더 좋은 그림 나오면 수정하겠습니다)
    scene bg lecture_room

    # while문에 논리행 몇 개를 추가해서 낮, 밤 일정을 추가해보았습니다.
    $ day = 1
    while day <= 6:
        $ YoIl = day_name[day]
        "[YoIl] 낮, 강의실에서 수업을 들었다."
        scene black

        "[YoIl] 저녁에\n"
        if day_schedule[((week - 1) * 7 + day) % 28] == 1:
            extend "공부했다"
        elif day_schedule[((week - 1) * 7 + day) % 28] == 2:
            extend "동아리 연습했다"
        elif day_schedule[((week - 1) * 7 + day) % 28] == 3:
            extend "과활동했다"
        elif day_schedule[((week - 1) * 7 + day) % 28] == 4:
            extend "휴식했다"
        else :
            extend "에러"

        show phone_night at truecenter
        "[YoIl] 밤, SNS를 확인했다."
        scene bg lecture_room
        $ day += 1

    "일요일 화면으로 돌아갑니다."
    call weekday_schedule_reset
    jump sunday_room
    return

label weekday_schedule_reset:
#    $ i = 1
#    while i < 7:
#        $ day_schedule[i] = 0
#        $ i += 1
    if ((week - 1) * 7 + day) % 28 == 0:
        $ i = 1
        while i < 28:
            $ day_schedule[i] = 0
            $ i += 1

    $ day = 1
    $ week += 1
    $ for_day_schedule_select = 0
    return
