# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label phone :
    show screen phone_UI
    show screen phone_button_in_homescreen

    #if day == 0 :
    hide screen dateShow
    show screen dateShow
    hide screen upper_right_UI
    show screen upper_right_UI

    while True:
        window hide
        pause

    return

label phone_close :
    hide screen phone_UI
    hide screen phone_button_in_homescreen
    hide screen fbook
    hide screen ktalk
    show screen phone_icon

    if day == 0:
        jump sunday_room

    return
