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

## 일요일 방과 일정 실행 중에 핸드폰 아이콘
screen phone_icon():
    vbox :
        if day == 0 :
            xpos 428 ypos 360
        else :
            xpos 160 ypos 360

        imagebutton:
            idle "phone_icon.png"
            # 마우스를 갖다 댈 시에 뒤에 그림자가 생김
            hover "phone_icon_sel.png"
            # 클릭시 phone label을 실행함
            action Hide("phone_icon"), Hide("planner_icon"), Call("phone")

            #at shake

    if day == 0 :
        # 카톡이 하나라도 있다면
        if grouptalk.new_message_count + jangjung.new_message_count + jinil.new_message_count + samyong.new_message_count + dongah.new_message_count != 0 :
            add "phone/red_dot.png" xpos 460 ypos 356 at shake
            vbox xpos 460 ypos 356 xsize 20 ysize 20:
                text "N" size 18 xalign .6 yalign .5 at shake

    else :
        if grouptalk.new_message_count + jangjung.new_message_count + jinil.new_message_count + samyong.new_message_count + dongah.new_message_count != 0 :
            add "phone/red_dot.png" xpos 192 ypos 356 at shake
            vbox xpos 192 ypos 356 xsize 20 ysize 20:
                text "N" size 18 xalign .6 yalign .5 at shake

transform shake:
    linear 0.045 xoffset 2 #yoffset -6
    linear 0.045 xoffset -2.8 #yoffset -2
    linear 0.045 xoffset 2.8 #yoffset -2
    linear 0.045 xoffset -2 #yoffset -6
    linear 0.045 xoffset +0 #yoffset +0
    repeat

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

                        add im.Scale("white.png", 440, tmp_height)
                        null height -tmp_height
                        hbox xsize 440 ysize tmp_height xpos 8 ypos 8:
                            if msg[1] == "해장중" :
                                add "character/profile_jangjung.png"
                            elif msg[1] == "안금지" :
                                add "fbook_profile"
                            elif msg[1] == "동삼용" :
                                add "character/profile_drummer.png"
                            elif msg[1] == "김진일" :
                                add "character/profile_jinil.png"
                            elif msg[1] == "유현재" :
                                add "character/profile_hyunjae.png"
                            elif msg[1] == "박대현" :
                                add "character/profile_daehyun.png"

                            null width 6

                            vbox xsize 374 :
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
                            if msg[1] == "해장중" :
                                add "character/profile_jangjung.png"
                            elif msg[1] == "안금지" :
                                add "fbook_profile"
                            elif msg[1] == "동삼용" :
                                add "character/profile_drummer.png"
                            elif msg[1] == "김진일" :
                                add "character/profile_jinil.png"
                            elif msg[1] == "유현재" :
                                add "character/profile_hyunjae.png"
                            elif msg[1] == "박대현" :
                                add "character/profile_daehyun.png"
                            elif msg[1] == "오덕현" :
                                add "character/profile_ohduck.png"
                            elif msg[1] == "노미래" :
                                add "character/profile_mirae.png"
                            else :
                                add "phone/fbook/comment_profile.png"
                            vbox :
                                add im.Scale("phone/fbook/comment_message_topbot.png", 356 - 20, 4)
                                add im.Scale("white.png", 356 - 20, tmp_height-15)
                                null height - (tmp_height-15)
                                vbox ysize tmp_height-15:
                                    text "{color=#000}%s" %(msg[1]) xpos 12 yalign 0.5 size 17
                                    text "{color=#505050}%s" %(msg[2]) xpos 12 yalign 0.5 size 17
                                add im.Scale("phone/fbook/comment_message_topbot.png", 356 - 20, 4)

                    elif msg[0] == "댓글종료" :
                        add "phone/fbook/comment_bottom.png"

                    elif msg[0] == "그림자" :
                        add "phone/fbook/fbook_post_shadow.png"

    add "fbook_screen_tab" xpos 420 ypos 40

screen ktalk:
    if ktalk_mode == 1 :
        add "phone/ktalk/ktalk_friends.png" xpos 420 ypos 40

        add "character/profile_player.png" xpos 420 + 8 ypos 40 + 108
        text "{color=#000}주인공{/color}" size 20 xpos 520 ypos 40 + 108 + 20
#        hbox :
#            xpos 420 + 624 - 172 - 172 - 16 ypos 40 + 108 + 20
#            for i in range(1,6) :
#                add "phone/ktalk/heart_full.png"
#                null width 4

        #김진일
        add "character/profile_jinil.png" xpos 420 + 8 ypos 40 + 236
        text "{color=#000}김진일{/color}" size 20 xpos 520 ypos 40 + 236 + 20
        hbox :
            xpos 420 + 624 - 172 - 172 - 16 ypos 40 + 236 + 20
            for i in range(1,6) :
                if i*20 <= jinil.parameter :
                    add "phone/ktalk/heart_full.png"
                else :
                    add "phone/ktalk/heart_empty.png"
                null width 4

        #동삼용
        add "character/profile_drummer.png" xpos 420 + 8 ypos 40 + 320
        text "{color=#000}동삼용{/color}" size 20 xpos 520 ypos 40 + 320 + 20
        hbox :
            xpos 420 + 624 - 172 - 172 - 16 ypos 40 + 320 + 20
            for i in range(1,6) :
                if i*20 <= samyong.parameter :
                    add "phone/ktalk/heart_full.png"
                else :
                    add "phone/ktalk/heart_empty.png"
                null width 4

        #해장중
        add "character/profile_jangjung.png" xpos 420 + 8 ypos 40 + 404
        text "{color=#000}해장중{/color}" size 20 xpos 520 ypos 40 + 404 + 20
        hbox :
            xpos 420 + 624 - 172 - 172 - 16 ypos 40 + 404 + 20
            for i in range(1,6) :
                if i*20 <= jangjung.parameter :
                    add "phone/ktalk/heart_full.png"
                else :
                    add "phone/ktalk/heart_empty.png"
                null width 4


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
                add im.Scale("white.png", 440, 548) #xalign 0.5 #ypos 40
                null height -548
                vbox xsize 440 ysize 60 :
                    text "{color=#000}채팅{/color}" size 24 xpos 20 yalign 0.6
                for i in rand_list_for_katlk_list :
                    if i == 1 and grouptalk.new_message_count != 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "그룹"), SetVariable("grouptalk.new_message_count", 0)
                        null height -92
                        add "character/profile_jangjung.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            hbox xsize 440 ysize 92 :
                                text "{color=#000}단톡" xalign 0.5 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                add im.Scale("phone/red_rectanguler.png",75,50) xalign 0.9 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                text "[grouptalk.new_message_count]" size 20 xalign 0.84 yalign 0.5
                        null height -5

                    elif i == 2 and jangjung.new_message_count != 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "장중"), SetVariable("jangjung.new_message_count", 0)
                        null height -92
                        add "character/profile_jangjung.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            hbox xsize 440 ysize 92 :
                                text "{color=#000}장중" xalign 0.5 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                add im.Scale("phone/red_rectanguler.png",75,50) xalign 0.9 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                text "[jangjung.new_message_count]" size 20 xalign 0.84 yalign 0.5
                        null height -5

                    elif i == 3 and jinil.new_message_count != 0:
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "진일"), SetVariable("jinil.new_message_count", 0)
                        null height -92
                        add "character/profile_jinil.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            hbox xsize 440 ysize 92 :
                                text "{color=#000}진일" xalign 0.5 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                add im.Scale("phone/red_rectanguler.png",75,50) xalign 0.9 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                text "[jinil.new_message_count]" size 20 xalign 0.84 yalign 0.5
                        null height -5

                    elif i == 4 and samyong.new_message_count != 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "삼용"), SetVariable("samyong.new_message_count", 0)
                        null height -92
                        add "character/profile_drummer.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            hbox xsize 440 ysize 92 :
                                text "{color=#000}삼용" xalign 0.5 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                add im.Scale("phone/red_rectanguler.png",75,50) xalign 0.9 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                text "[samyong.new_message_count]" size 20 xalign 0.84 yalign 0.5
                        null height -5

                    elif i == 5 and dongah.new_message_count != 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "동아"), SetVariable("dongah.new_message_count", 0)
                        null height -92
                        add "character/profile_dongah.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            hbox xsize 440 ysize 92 :
                                text "{color=#000}동아" xalign 0.5 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                add im.Scale("phone/red_rectanguler.png",75,50) xalign 0.9 yalign 0.5
                            null width -440
                            hbox xsize 440 ysize 92 :
                                text "[dongah.new_message_count]" size 20 xalign 0.84 yalign 0.5
                        null height -5


                for i in rand_list_for_katlk_list :
                    if i == 1 and grouptalk.new_message_count == 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "그룹"), SetVariable("grouptalk.new_message_count", 0)
                        null height -92
                        add "character/profile_jangjung.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            text "{color=#000}단톡" xalign 0.5 yalign 0.5
                        null height -5

                    elif i == 2 and jangjung.new_message_count == 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "장중"), SetVariable("jangjung.new_message_count", 0)
                        null height -92
                        add "character/profile_jangjung.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            text "{color=#000}장중" xalign 0.5 yalign 0.5
                        null height -5

                    elif i == 3 and jinil.new_message_count == 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "진일"), SetVariable("jinil.new_message_count", 0)
                        null height -92
                        add "character/profile_jinil.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            text "{color=#000}진일" xalign 0.5 yalign 0.5
                        null height -5

                    elif i == 4 and samyong.new_message_count == 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "삼용"), SetVariable("samyong.new_message_count", 0)
                        null height -92
                        add "character/profile_drummer.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            text "{color=#000}삼용" xalign 0.5 yalign 0.5
                        null height -5

                    elif i == 5 and dongah.new_message_count == 0 :
                        imagebutton :
                            idle "phone/ktalk/talklist.png"
                            hover "phone/ktalk/talklist_on.png"
                            action SetVariable("ktalk_mode", 3), SetVariable("talk_with_who", "동아"), SetVariable("dongah.new_message_count", 0)
                        null height -92
                        add "character/profile_dongah.png" xpos 8 + 2 ypos 12 + 2
                        null height - 64
                        hbox xsize 440 ysize 92 :
                            text "{color=#000}동아" xalign 0.5 yalign 0.5
                        null height -5

        imagebutton :
                xpos 420 ypos 588
                idle "phone/button_friends.png"
                hover "phone/button_friends_on.png"
                action SetVariable("ktalk_mode", 1)

        add "phone/button_talk_sel.png" xpos 640 ypos 588

    # 원래 3, 친구 대화 목록
    elif ktalk_mode == 3 :
        add "phone/ktalk/ktalk_background.png" xpos 420 ypos 40
        viewport:
            xpos 420 ypos 40
            xsize 440 ysize 624
            yinitial 1.0
            draggable True
            mousewheel True
            arrowkeys True

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
                                    add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                    null width tmp_width -8
                                    add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                null height tmp_height - 8
                                hbox xsize tmp_width :
                                    add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                    null width tmp_width -8
                                    add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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
                                    if msg[0] == "해장중" :
                                        add "character/profile_jangjung.png" xpos 2 ypos 2

                                    elif msg[0] == "김진일" :
                                        add "character/profile_jinil.png" xpos 2 ypos 2

                                    elif msg[0] == "동삼용" :
                                        add "character/profile_drummer.png" xpos 2 ypos 2

                                    elif msg[0] == "유현재" :
                                        add "character/profile_hyunjae.png" xpos 2 ypos 2

                                    elif msg[0] == "노미래" :
                                        add "character/profile_mirae.png" xpos 2 ypos 2

                                    elif msg[0] == "이동아" :
                                        add "character/profile_dongah.png" xpos 2 ypos 2

                                    elif msg[0] == "박대현" :
                                        add "character/profile_daehyun.png" xpos 2 ypos 2

                                    elif msg[0] == "오덕현" :
                                        add "character/profile_ohduck.png" xpos 2 ypos 2

                                    else :
                                        add "phone/ktalk/1.png"

                                    null width 7
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}%s" %msg[0] size 18
                                        null height 4
                                        add im.Scale("white.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 71
                                    vbox:
                                        #null height -15
                                        add im.Scale("white.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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

                            $ hangul = re.compile('[^~가-힣]+')
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
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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
                                    add "character/profile_jangjung.png" xpos 2 ypos 2

                                    null width 7
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}장중" size 18
                                        null height 4
                                        add im.Scale("white.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 71
                                    vbox:
                                        #null height -15
                                        add im.Scale("white.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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

                            $ hangul = re.compile('[^~가-힣]+')
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
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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
                                    add "character/profile_jinil.png" xpos 2 ypos 2

                                    null width 7
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}진일" size 18
                                        null height 4
                                        add im.Scale("white.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 71
                                    vbox:
                                        #null height -15
                                        add im.Scale("white.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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

                            $ hangul = re.compile('[^~가-힣]+')
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
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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
                                    add "character/profile_drummer.png" xpos 2 ypos 2

                                    null width 7
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}삼용" size 18
                                        null height 4
                                        add im.Scale("white.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 71
                                    vbox:
                                        #null height -15
                                        add im.Scale("white.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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

                            $ hangul = re.compile('[^~가-힣]+')
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
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                    null height tmp_height - 8
                                    hbox xsize tmp_width :
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null width tmp_width -8
                                        add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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
                                    add "character/profile_dongah.png" xpos 2 ypos 2

                                    null width 7
                                    vbox :
                                        null height 3
                                        hbox xpos 6:
                                            text "{color=#000}동아" size 18
                                        null height 4
                                        add im.Scale("white.png", tmp_width, tmp_height) # 33+24x

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

                                        null height -tmp_height
                                        hbox xpos 6 ypos 6 :
                                            text "{color=#000}%s" %msg[1] size 18

                                elif msg[0] == "연속":
                                    null width 71
                                    vbox:
                                        #null height -15
                                        add im.Scale("white.png", tmp_width, tmp_height)

                                        null height -tmp_height
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                        null height tmp_height - 8
                                        hbox xsize tmp_width :
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)
                                            null width tmp_width -8
                                            add im.Scale("phone/ktalk/ktalk_background.png", 4, 4)

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
            idle im.Alpha(im.Scale("white.png", 40, 50), 0)
            action SetVariable("ktalk_mode", 2)
