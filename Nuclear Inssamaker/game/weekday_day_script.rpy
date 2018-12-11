# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label weekday_day_event :
#    if month == 3 :
#        if week == 3:
#            if day == 1 :
#                "null"
#
#            elif day == 2 :
#                "null"
#
#            elif day == 3 :
#                "null"
#
#            elif day == 4 :
#                "null"
#
#            elif day == 5 :
#                "null"
#
#            elif day == 6 :
#                "null"

#    if day < 6:
#        #낮 일정 소화
#        show bg lecture_room at truecenter
#        "[YoIl]요일 낮, 강의실에서 수업을 들었다."

    if day == 6 :
        "토요일 낮이 되었다."
        if day_schedule[month - 3][(week - 1) * 8 + day] == 1:
            call evening_study

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 2:
            call evening_club

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 3:
            call evening_gwa

        elif day_schedule[month - 3][(week - 1) * 8 + day] == 4:
            call evening_rest

    return
