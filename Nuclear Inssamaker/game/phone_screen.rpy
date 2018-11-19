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
            action Jump("phone_close")
            
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
                    #tmp_width = len(msg[1])
                    $ tmp_height = msg[1].count("\n")
                    $ tmp = []
                    $ lines = []
                    #$ tmp_width = len(msg[1]) / (msg[1].count("\n") + 1)

                    $ lines = string.split(msg[1], "\n")
                    for each_line in lines :
                        $ tmp.append(len(each_line))
                    $ tmp_width = max(tmp)

                    if msg[0] == "주인공" :
                        hbox xpos 434 - (10 + tmp_width * 17) ypos 4:
                            vbox :
                                add im.Scale("phone/ktalk/my_talk.png", 10 + tmp_width * 17 , 33 + tmp_height * 24)
                                null height -36 - tmp_height * 24
                                hbox xpos 6 ypos 8 :
                                    text "{color=#000}%s" %msg[1] size 18
                        null height 12

                    else :
                        hbox xpos 4 ypos 4:
                            if msg[0] != 0 :
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
                                    null height 5
                                    add "phone/ktalk/2.png"
                                    null height -20
                                    hbox xpos 6:
                                        text "{color=#000}%s" %msg[0] size 18
                                    null height 2
                                    add im.Scale("phone/ktalk/3.png", 10 + tmp_width * 17, 33 + tmp_height * 24) # 33+24x
                                    null height -33 - tmp_height * 24
                                    hbox xpos 6 ypos 6 :
                                        text "{color=#000}%s" %msg[1] size 18
                            else :
                                null width 67
                                vbox:
                                    #null height -15
                                    add im.Scale("phone/ktalk/3.png", 10 + tmp_width * 17, 33 + tmp_height * 24)
                                    null height -33 - tmp_height * 24
                                    hbox xpos 6 ypos 6 :
                                        text "{color=#000}%s" %msg[1] size 18

                        null height 12

        add "phone/ktalk/0.png" xpos 420 ypos 40
