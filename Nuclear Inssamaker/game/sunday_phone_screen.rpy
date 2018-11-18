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
            action Hide("phone_button_in_homescreen"), Show("ktalk",msg_list="messages")

screen fbook :
    viewport :
        xpos 420 ypos 40
        xsize 440 ysize 624
        xmaximum 440 ymaximum 624
        draggable True
        mousewheel True
        arrowkeys True

        add "fbook_screen_posts"

    add "fbook_screen_tab" xpos 420 ypos 40

screen ktalk(msg_list):
    if ktalk_mode == 1 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 624
            draggable True
            mousewheel True
            arrowkeys True

            add "phone/ktalk_friends.png" #xpos 420 ypos 40

        add "phone/button_friends_sel.png" xpos 420 ypos 588
        imagebutton :
                xpos 640 ypos 588
                idle "phone/button_talk.png"
                hover "phone/button_talk_on.png"
                action SetVariable("ktalk_mode", 2)

    # 원래 2, 대화창 모드
    elif ktalk_mode == 3 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 548
            draggable True
            mousewheel True
            arrowkeys True

            add "phone/ktalk_list.png" #xalign 0.5 #ypos 40

        imagebutton :
                xpos 420 ypos 588
                idle "phone/button_friends.png"
                hover "phone/button_friends_on.png"
                action SetVariable("ktalk_mode", 1)

        add "phone/button_talk_sel.png" xpos 640 ypos 588

    # 원래 3, 친구 대화 목록
    elif ktalk_mode == 2 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 624
            yinitial 1.0
            draggable True
            mousewheel True
            arrowkeys True

#            add "phone/ktalk_list.png" #xalign 0.5 #ypos 40

#            vbox : #xalign 0.5 yalign 0.5 :
#                null height 66
#                add "phone/ktalk/1.png"
#                null height 10
#                add "phone/ktalk/1.png"

            vbox : #xalign 0.5 yalign 0.5 :
                null height 66

                for msg in messages :
                    hbox xpos 4 ypos 4:
                        if msg[0] == "장중" :
                            add "phone/ktalk/jangjung.png"

                        elif msg[0] == "진일" :
                            add "phone/ktalk/jinil.png"

                        elif msg[0] == "삼용" :
                            add "phone/ktalk/samyong.png"

                        elif msg[0] == "현재" :
                            add "phone/ktalk/hyunjae.png"

                        elif msg[0] == "미래" :
                            add "phone/ktalk/mirae.png"

                        elif msg[0] == "동아" :
                            add "phone/ktalk/dongah.png"

                        else :
                            add "phone/ktalk/1.png"

                        null width 3
                        vbox :
                            add "phone/ktalk/2.png"
                            null height -20
                            text "{color=#000}%s" %msg[0] size 18
                            null height 2
                            add "phone/ktalk/3.png"
                            null height -48
                            hbox xpos 6 ypos 6 :
                                text "{color=#000}%s" %msg[1] size 34
                    null height 15

        add "phone/ktalk/0.png" xpos 420 ypos 40
