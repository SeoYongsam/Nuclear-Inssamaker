# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

image planner_background = "planner_background.png"
image highlight = "highlight.png"

image sel_study = im.Scale("sel_study.png",98,98)   #1
image sel_club = im.Scale("sel_club.png",98,98)     #2
image sel_gwa = im.Scale("sel_gwa.png",98,98)       #3
image sel_rest = im.Scale("sel_rest.png",98,98)     #4


#start 함수에서 오는 곳
label sunday_room:
    scene room at truecenter

    show screen phone_icon
    show screen planner_icon


    s "일요일 낮이 되었습니다."
    p "밥을 먹었다. 체력을 회복한다"

    $hp += 10

    s "새로운 렌파이 게임을 만들었군요."


    call limitation #아직 구현 안된 것


    s "이야기와 그림, 음악을 더하면 여러분의 게임을 세상에 배포할 수 있어요!"

    return

label planner:
    show planner_background
    hide screen phone_icon
    hide screen planner_icon

    # 형광색 하이라이트 창
    if day <= 6 :
        show screen schedule_highlight
    else :
        hide screen schedule_highlight

    show screen schedule_mon
    show screen schedule_tue
    show screen schedule_wed
    show screen schedule_thu
    show screen schedule_fri
    show screen schedule_sat

    # 오른쪽 스케줄 창
    show screen schedule_button
    $ tmp_2 = day - 1
    "[day]일차 일정을 선택하세요."


    if day < 7:
        $ day_schedule[day-1] = tmp_1

#    hide screen schedule_button

    if tmp_1 != 0:
        if day <= 6:
            $ day += 1
        $ tmp_1 = 0

    if day == 7:
        hide screen schedule_highlight
        "일주일 일정을 실행하시겠습니까?"
        menu:
            "실행한다":
                jump weekday_run
            "수정한다":
                "미구현"


    jump planner

    return

label go_sunday_room :
    hide planner_background

    hide screen schedule_button
    hide screen schedule_highlight

    hide screen schedule_mon
    hide screen schedule_tue
    hide screen schedule_wed
    hide screen schedule_thu
    hide screen schedule_fri
    hide screen schedule_sat

    jump sunday_room

label phone:
    hide screen phone_icon
    hide screen planner_icon
    "핸드폰 화면이 구현되지 않았습니다."
    "일요일 화면으로 돌아갑니다"

    jump sunday_room
    return
