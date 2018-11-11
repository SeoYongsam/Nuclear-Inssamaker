#이벤트

label lecture:
    scene bg lecture_room
    '[i]일차 낮, 강의실에서 수업을 들었다'
    return

label lecture_sleep:
    scene bg lecture_room
    '[i]일차 낮, 너무 피곤하다 어떻게 할까'

    scene black
    menu:
        "그냥 잔다":
            "너무 피곤해서 잠이 들었다."
        "수업을 듣는다":
            jump lecture
    return
