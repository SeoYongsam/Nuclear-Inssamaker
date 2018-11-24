# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label weekday_day_event :
    if month == 3 :
        if week == 3 :
            if day == 1 :
                "null"

            elif day == 2 :
                "null"

            elif day == 3 :
                "null"

            elif day == 4 :
                "null"

            elif day == 5 :
                "null"

            elif day == 6 :
                "null"

    #낮 일정 소화
    show bg lecture_room at truecenter
    "[YoIl]요일 낮, 강의실에서 수업을 들었다."

    return
