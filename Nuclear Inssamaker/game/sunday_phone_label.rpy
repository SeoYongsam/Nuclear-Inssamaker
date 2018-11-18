# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label phone:
    show screen phone_UI
    show screen phone_button_in_homescreen

    hide screen dateShow
    show screen dateShow
    hide screen sunday_room_UI
    show screen sunday_room_UI
    hide screen hp_and_loneliness_show
    show screen hp_and_loneliness_show

    while True:
        window hide
        pause

    return
