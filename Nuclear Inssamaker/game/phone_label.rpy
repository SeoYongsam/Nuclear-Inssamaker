# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label phone :
    show screen phone_UI
    show screen phone_button_in_homescreen

    #if day == 0 :
    hide screen dateShow
    show screen dateShow
    hide screen always_except_planner_UI
    show screen always_except_planner_UI
    hide screen hp_and_loneliness_show
    show screen hp_and_loneliness_show

    while True:
        window hide
        pause

    return

label phone_close :
    hide screen phone_UI
    hide screen phone_button_in_homescreen
    hide screen fbook
    hide screen ktalk
    $ ktalk_mode = 1

    if day == 0:
        jump sunday_room

    return
