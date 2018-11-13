# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

screen phone_UI() :
    add Solid("#000c")
    add "phone/phone_body.png"
    add "phone/screen_main.png" xpos 420 ypos 40

    # 'X'버튼(나가기 버튼)
    vbox xpos 880 ypos 16 :
        imagebutton :
            idle "phone/exitButton.png"
            hover "phone/exitButton_on.png"
            action Hide("phone_UI", dissolve), Hide("phone_button_in_homescreen", dissolve), Hide("fbook", dissolve), Hide("ktalk", dissolve), SetVariable("ktalk_mode",1), Jump("sunday_room")

    #홈버튼
    vbox xpos 620 ypos 672 :
        imagebutton :
            idle "phone/homebutton.png"
            hover "phone/homebutton_on.png"
            action Hide("fbook"), Hide("ktalk"), SetVariable("ktalk_mode",1), Show("phone_button_in_homescreen")


screen phone_button_in_homescreen() :
    hbox xpos 428 ypos 564 :
        spacing 8
        imagebutton :
            idle "phone/icon_fbook.png"
            hover "phone/icon_fbook_on.png"
            action Hide("phone_button_in_homescreen"), Show("fbook")

        imagebutton :
            idle "phone/icon_talk.png"
            hover "phone/icon_talk_on.png"
            action Hide("phone_button_in_homescreen"), Show("ktalk")

screen fbook :
    viewport :
        xpos 420 ypos 40
        xsize 440 ysize 624
        draggable True
        mousewheel True
        arrowkeys True

        add "fbook_screen_posts"

    add "fbook_screen_tab" xpos 420 ypos 40

screen ktalk:
    if ktalk_mode == 1 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 624
            draggable True
            mousewheel True
            arrowkeys True

            add "phone/ktalk_friends.png" xpos 420 ypos 40

        add "phone/button_friends_sel.png" xpos 420 ypos 588
        imagebutton :
                xpos 640 ypos 588
                idle "phone/button_talk.png"
                hover "phone/button_talk_on.png"
                action SetVariable("ktalk_mode", 2)

    elif ktalk_mode == 2 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 548
            draggable True
            mousewheel True
            arrowkeys True

            add "phone/ktalk_list.png" xpos 420 ypos 40

        imagebutton :
                xpos 420 ypos 588
                idle "phone/button_friends.png"
                hover "phone/button_friends_on.png"
                action SetVariable("ktalk_mode", 1)

        add "phone/button_talk_sel.png" xpos 640 ypos 588
