﻿# Ren'Py automatically loads all script files ending with .rpy. To use this
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
            action Hide("phone_button_in_homescreen"), Show("ktalk")

screen fbook :
    add im.Scale("phone/fbook/fbook_background.png", 440, 624) xpos 420 ypos 40
    viewport :
        xpos 420 ypos 148
        xsize 440 ysize 516
        xmaximum 440 ymaximum 516
        yinitial 1.0
        draggable True
        mousewheel True
        arrowkeys True

        vbox xpos 420 ypos 148 xsize 440:
            vbox :
                for msg in fbook_post :
                    if msg[0] == "본문" :
                        $ tmp_height = 105 + msg[3].count("\n") * 26

                        add im.Scale("phone/fbook/fbook_post.png", 440, tmp_height)
                        null height -tmp_height
                        hbox xsize 440 ysize tmp_height xpos 8 ypos 8:
                            add "fbook_profile"

                            vbox xsize 380 :
                                null height 5
                                text "{color=#000}%s" %msg[1] size 18
                                null height 2
                                text "{color=#808080}%s" %msg[2] size 15
                                null height 10

                                $ lines = string.split(msg[3], "\n")
                                for each_line in lines :
                                    $ tmplist = list(each_line)
                                    if tmplist[0] == " " :
                                        $ del tmplist[0]
                                    $ tmp = ''.join(tmplist)

                                    text "{color=#000}%s" %tmp size 20


                    elif msg[0] == "댓글시작" :
                        add "phone/fbook/comment_top.png"
                        add im.Scale("phone/fbook/comment_mid.png", 440, 40)
                        null height -40
                        vbox xsize 440 ysize 40 :
                            text "{color=#000}댓글" size 20 xpos 20 yalign 0.6

                    elif msg[0] == "댓글" :
                        $ tmp_height = 65 + msg[2].count("\n") * 26

                        add im.Scale("phone/fbook/comment_mid.png", 440, tmp_height)
                        null height -tmp_height
                        hbox xsize 425 ysize tmp_height xpos 15:
                            add "phone/fbook/comment_profile.png"
                            vbox :
                                add "phone/fbook/comment_message_topbot.png"
                                add im.Scale("phone/fbook/comment_message_mid.png", 356, tmp_height-15)
                                null height - (tmp_height-15)
                                vbox ysize tmp_height-15:
                                    text "{color=#000}%s" %(msg[1]) xpos 12 yalign 0.5 size 17
                                    text "{color=#505050}%s" %(msg[2]) xpos 12 yalign 0.5 size 17
                                add "phone/fbook/comment_message_topbot.png"

                    elif msg[0] == "댓글종료" :
                        add "phone/fbook/comment_bottom.png"

                    elif msg[0] == "그림자" :
                        add "phone/fbook/fbook_post_shadow.png"

    add "fbook_screen_tab" xpos 420 ypos 40

screen ktalk:
    if ktalk_mode == 1 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 624
            draggable True
            mousewheel True
            arrowkeys True

            add "phone/ktalk/ktalk_friends.png" #xpos 420 ypos 40

        add "phone/button_friends_sel.png" xpos 420 ypos 588
        imagebutton :
                xpos 640 ypos 588
                idle "phone/button_talk.png"
                hover "phone/button_talk_on.png"
                action SetVariable("ktalk_mode", 2)

    # 원래 2, 대화창 모드
    elif ktalk_mode == 2 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 548
            draggable True
            mousewheel True
            arrowkeys True
            vbox :
                add "phone/ktalk/ktalk_list.png" #xalign 0.5 #ypos 40
                null height -572
                imagebutton :
                    idle "phone/ktalk/talklist1.png"
                    hover "phone/ktalk/talklist1_on.png"
                    action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "그룹")#, Call("change_group_talk")
                null height -92
                vbox xsize 440 ysize 92 :
                    text "{color=#000}단톡(순서는 신경쓰지 마시오)" xalign 0.5 yalign 0.5
                null height -1

                imagebutton :
                    idle "phone/ktalk/talklist2.png"
                    hover "phone/ktalk/talklist2_on.png"
                    action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "장중")
                null height -92
                vbox xsize 440 ysize 92 :
                    text "{color=#000}장중" xalign 0.5 yalign 0.5
                null height -1

                imagebutton :
                    idle "phone/ktalk/talklist3.png"
                    hover "phone/ktalk/talklist3_on.png"
                    action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "진일")
                null height -92
                vbox xsize 440 ysize 92 :
                    text "{color=#000}진일" xalign 0.5 yalign 0.5
                null height -1

                imagebutton :
                    idle "phone/ktalk/talklist4.png"
                    hover "phone/ktalk/talklist4_on.png"
                    action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "삼용")
                null height -92
                vbox xsize 440 ysize 92 :
                    text "{color=#000}삼용" xalign 0.5 yalign 0.5
                null height -1

                imagebutton :
                    idle "phone/ktalk/talklist5.png"
                    hover "phone/ktalk/talklist5_on.png"
                    action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "동아")
                null height -92
                vbox xsize 440 ysize 92 :
                    text "{color=#000}동아" xalign 0.5 yalign 0.5
                null height -1

                imagebutton :
                    idle "phone/ktalk/talklist6.png"
                    hover "phone/ktalk/talklist6_on.png"
                    action Null
                null height -92
                vbox xsize 440 ysize 92 :
                    text "{color=#000}현재?" xalign 0.5 yalign 0.5
                null height -1


        imagebutton :
                xpos 420 ypos 588
                idle "phone/button_friends.png"
                hover "phone/button_friends_on.png"
                action SetVariable("ktalk_mode", 1)

        add "phone/button_talk_sel.png" xpos 640 ypos 588

    # 원래 3, 친구 대화 목록
    elif ktalk_mode == 3 :
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 624
            yinitial 1.0
            draggable True
            mousewheel True
            arrowkeys True
            #edgescroll (200, 1000)

#            add "phone/ktalk_list.png" #xalign 0.5 #ypos 40

#            vbox : #xalign 0.5 yalign 0.5 :
#                null height 66
#                add "phone/ktalk/1.png"
#                null height 10
#                add "phone/ktalk/1.png"
            if talk_with_who == "그룹" :
                vbox : #xalign 0.5 yalign 0.5 :
                    null height 66
                    for msg in grouptalk.message :
                        #tmp_width = len(msg[1])
                        $ tmp_height = 33 + msg[1].count("\n") * 24
                        $ tmp = []
                        $ lines = []

                        #$ tmp_width = len(msg[1]) / (msg[1].count("\n") + 1)

                        $ lines = string.split(msg[1], "\n")
                        for each_line in lines :

                            $ hangul = re.compile('[^~가-힣]+')
                            $ KletterFull = len(hangul.sub('',each_line))
                            $ hangul = re.compile('[^ㄱ-ㅣ]+')
                            $ KletterHalf = len(hangul.sub('',each_line))
                            $ letter_without_Kletter = len(each_line) - KletterFull - KletterHalf
                            $ each_line_width = 10 + KletterFull*17 + KletterHalf*15 + letter_without_Kletter*10
                            $ tmp.append(each_line_width)

                        $ tmp_width = max(tmp)

                        if msg[0] == "주인공" :
                            vbox xpos 434 - (tmp_width) ypos 4:
                                add im.Scale("phone/ktalk/my_talk.png", tmp_width , tmp_height)

                                null height -tmp_height
                                hbox xsize tmp_width :
                                    add "phone/ktalk/dot.png"
                                    null width tmp_width -8
                                    add "phone/ktalk/dot.png"
                                null height tmp_height - 8
                                hbox xsize tmp_width :
                                    add "phone/ktalk/dot.png"
                                    null width tmp_width -8
                                    add "phone/ktalk/dot.png"

                                null height -3 - tmp_height
                                vbox xpos 6 ypos 8 :
                                    $ lines = string.split(msg[1], "\n")
                                    for each_line in lines :
                                        $ tmplist = list(each_line)
                                        if tmplist[0] == " " :
                                            $ del tmplist[0]
                                        $ tmp = ''.join(tmplist)

                                        text "{color=#000}%s" %tmp size 18
                            null height 12

                        else :
                            hbox xpos 4 ypos 4:
                                if msg[0] != "날짜" and msg[0] != "연속" :
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
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}%s" %msg[0] size 18
                                        null height 4
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 67
                                    vbox:
                                        #null height -15
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "날짜":
                                    vbox xsize 440 ysize 30 :
                                        text "{color=#000}%s" %msg[1] size 25 xalign 0.5 yalign 0.5

                            null height 12

            elif talk_with_who == "장중" :
                vbox : #xalign 0.5 yalign 0.5 :
                    null height 66
                    for msg in jangjung.message :
                        #tmp_width = len(msg[1])
                        $ tmp_height = 33 + msg[1].count("\n") * 24
                        $ tmp = []
                        $ lines = []

                        #$ tmp_width = len(msg[1]) / (msg[1].count("\n") + 1)

                        $ lines = string.split(msg[1], "\n")
                        for each_line in lines :

                            $ hangul = re.compile('[^가-힣]+')
                            $ KletterFull = len(hangul.sub('',each_line))
                            $ hangul = re.compile('[^ㄱ-ㅣ]+')
                            $ KletterHalf = len(hangul.sub('',each_line))
                            $ letter_without_Kletter = len(each_line) - KletterFull - KletterHalf
                            $ each_line_width = 10 + KletterFull*17 + KletterHalf*15 + letter_without_Kletter*10
                            $ tmp.append(each_line_width)

                        $ tmp_width = max(tmp)

                        if msg[0] == "주인공" :
                            hbox xpos 434 - (tmp_width) ypos 4:
                                vbox :
                                    add im.Scale("phone/ktalk/my_talk.png", tmp_width , tmp_height)

                                    null height -tmp_height
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"

                                    null height -3 - tmp_height
                                    vbox xpos 6 ypos 8 :
                                        $ lines = string.split(msg[1], "\n")
                                        for each_line in lines :
                                            $ tmplist = list(each_line)
                                            if tmplist[0] == " " :
                                                $ del tmplist[0]
                                            $ tmp = ''.join(tmplist)

                                            text "{color=#000}%s" %tmp size 18
                            null height 12

                        else :
                            hbox xpos 4 ypos 4:
                                if msg[0] != "날짜" and msg[0] != "연속" :
                                    add "phone/ktalk/jangjung.png"

                                    null width 3
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}장중" size 18
                                        null height 4
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 67
                                    vbox:
                                        #null height -15
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "날짜":
                                    vbox xsize 440 ysize 30 :
                                        text "{color=#000}%s" %msg[1] size 25 xalign 0.5 yalign 0.5

                            null height 12

            elif talk_with_who == "진일" :
                vbox : #xalign 0.5 yalign 0.5 :
                    null height 66
                    for msg in jinil.message :
                        #tmp_width = len(msg[1])
                        $ tmp_height = 33 + msg[1].count("\n") * 24
                        $ tmp = []
                        $ lines = []

                        #$ tmp_width = len(msg[1]) / (msg[1].count("\n") + 1)

                        $ lines = string.split(msg[1], "\n")
                        for each_line in lines :

                            $ hangul = re.compile('[^가-힣]+')
                            $ KletterFull = len(hangul.sub('',each_line))
                            $ hangul = re.compile('[^ㄱ-ㅣ]+')
                            $ KletterHalf = len(hangul.sub('',each_line))
                            $ letter_without_Kletter = len(each_line) - KletterFull - KletterHalf
                            $ each_line_width = 10 + KletterFull*17 + KletterHalf*15 + letter_without_Kletter*10
                            $ tmp.append(each_line_width)

                        $ tmp_width = max(tmp)

                        if msg[0] == "주인공" :
                            hbox xpos 434 - (tmp_width) ypos 4:
                                vbox :
                                    add im.Scale("phone/ktalk/my_talk.png", tmp_width , tmp_height)

                                    null height -tmp_height
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"

                                    null height -3 - tmp_height
                                    vbox xpos 6 ypos 8 :
                                        $ lines = string.split(msg[1], "\n")
                                        for each_line in lines :
                                            $ tmplist = list(each_line)
                                            if tmplist[0] == " " :
                                                $ del tmplist[0]
                                            $ tmp = ''.join(tmplist)

                                            text "{color=#000}%s" %tmp size 18
                            null height 12

                        else :
                            hbox xpos 4 ypos 4:
                                if msg[0] != "날짜" and msg[0] != "연속" :
                                    add "phone/ktalk/jangjung.png"

                                    null width 3
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}진일" size 18
                                        null height 4
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 67
                                    vbox:
                                        #null height -15
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "날짜":
                                    vbox xsize 440 ysize 30 :
                                        text "{color=#000}%s" %msg[1] size 25 xalign 0.5 yalign 0.5

                            null height 12

            elif talk_with_who == "삼용" :
                vbox : #xalign 0.5 yalign 0.5 :
                    null height 66
                    for msg in samyong.message :
                        #tmp_width = len(msg[1])
                        $ tmp_height = 33 + msg[1].count("\n") * 24
                        $ tmp = []
                        $ lines = []

                        #$ tmp_width = len(msg[1]) / (msg[1].count("\n") + 1)

                        $ lines = string.split(msg[1], "\n")
                        for each_line in lines :

                            $ hangul = re.compile('[^가-힣]+')
                            $ KletterFull = len(hangul.sub('',each_line))
                            $ hangul = re.compile('[^ㄱ-ㅣ]+')
                            $ KletterHalf = len(hangul.sub('',each_line))
                            $ letter_without_Kletter = len(each_line) - KletterFull - KletterHalf
                            $ each_line_width = 10 + KletterFull*17 + KletterHalf*15 + letter_without_Kletter*10
                            $ tmp.append(each_line_width)

                        $ tmp_width = max(tmp)

                        if msg[0] == "주인공" :
                            hbox xpos 434 - (tmp_width) ypos 4:
                                vbox :
                                    add im.Scale("phone/ktalk/my_talk.png", tmp_width , tmp_height)

                                    null height -tmp_height
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"

                                    null height -3 - tmp_height
                                    vbox xpos 6 ypos 8 :
                                        $ lines = string.split(msg[1], "\n")
                                        for each_line in lines :
                                            $ tmplist = list(each_line)
                                            if tmplist[0] == " " :
                                                $ del tmplist[0]
                                            $ tmp = ''.join(tmplist)

                                            text "{color=#000}%s" %tmp size 18
                            null height 12

                        else :
                            hbox xpos 4 ypos 4:
                                if msg[0] != "날짜" and msg[0] != "연속" :
                                    add "phone/ktalk/samyong.png"

                                    null width 3
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}삼용" size 18
                                        null height 4
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 67
                                    vbox:
                                        #null height -15
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "날짜":
                                    vbox xsize 440 ysize 30 :
                                        text "{color=#000}%s" %msg[1] size 25 xalign 0.5 yalign 0.5

                            null height 12

            elif talk_with_who == "동아" :
                vbox : #xalign 0.5 yalign 0.5 :
                    null height 66
                    for msg in dongah.message :
                        #tmp_width = len(msg[1])
                        $ tmp_height = 33 + msg[1].count("\n") * 24
                        $ tmp = []
                        $ lines = []

                        #$ tmp_width = len(msg[1]) / (msg[1].count("\n") + 1)

                        $ lines = string.split(msg[1], "\n")
                        for each_line in lines :

                            $ hangul = re.compile('[^가-힣]+')
                            $ KletterFull = len(hangul.sub('',each_line))
                            $ hangul = re.compile('[^ㄱ-ㅣ]+')
                            $ KletterHalf = len(hangul.sub('',each_line))
                            $ letter_without_Kletter = len(each_line) - KletterFull - KletterHalf
                            $ each_line_width = 10 + KletterFull*17 + KletterHalf*15 + letter_without_Kletter*10
                            $ tmp.append(each_line_width)

                        $ tmp_width = max(tmp)

                        if msg[0] == "주인공" :
                            hbox xpos 434 - (tmp_width) ypos 4:
                                vbox :
                                    add im.Scale("phone/ktalk/my_talk.png", tmp_width , tmp_height)

                                    null height -tmp_height
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add "phone/ktalk/dot.png"
                                        null width tmp_width -8
                                        add "phone/ktalk/dot.png"

                                    null height -3 - tmp_height
                                    vbox xpos 6 ypos 8 :
                                        $ lines = string.split(msg[1], "\n")
                                        for each_line in lines :
                                            $ tmplist = list(each_line)
                                            if tmplist[0] == " " :
                                                $ del tmplist[0]
                                            $ tmp = ''.join(tmplist)

                                            text "{color=#000}%s" %tmp size 18
                            null height 12

                        else :
                            hbox xpos 4 ypos 4:
                                if msg[0] != "날짜" and msg[0] != "연속" :
                                    add "phone/ktalk/dongah.png"

                                    null width 3
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}동아" size 18
                                        null height 4
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 67
                                    vbox:
                                        #null height -15
                                        add im.Scale("phone/ktalk/3.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add "phone/ktalk/dot.png"
                                            null width tmp_width -8
                                            add "phone/ktalk/dot.png"

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "날짜":
                                    vbox xsize 440 ysize 30 :
                                        text "{color=#000}%s" %msg[1] size 25 xalign 0.5 yalign 0.5

                            null height 12

        add "phone/ktalk/0.png" xpos 420 ypos 40
        imagebutton :
            xpos 420 ypos 40
            idle im.Alpha(im.Scale("phone/ktalk/2.png", 40, 50), 0)
            action SetVariable("ktalk_mode", 2)
