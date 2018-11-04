# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.


label WeekSchedule:
    while i <= 6:
        $ tmp = day_schedule[i-1]
        "[i]일차 스케줄입니다. 하하 [tmp]"
        $ i += 1
    return
