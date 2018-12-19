# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_jinil_talk :
    if month == 3 :
        if week == 2 :
            if day == 2 :
                $ jinil.add("날짜|3월 10일 화요일")
                $ jinil.add("김진일|어디서 술자린데 빠지려고")
                $ jinil.add("연속|빨리 안오냐?? ㅡㅡ;;")
                $ jinil.add("주인공|엥? 너도 같이 마시고 있었냐?")
                $ jinil.add("김진일|그럼 술 마시는데 내가 빠질 것 같냐? ㅋㅋㅋㅋㅋ")
                $ jinil.add("연속|빨리 와라 애들 기다린다")
                $ jinil.add("주인공|엌ㅋㅋㅋㅋㅋㅋㅋ 오키오키 곧 갈게")
                $ jinil.add("김진일|오자마자 로그인샷 각오하고~")

            elif day == 4 :
                $ jinil.add("날짜|3월 12일 목요일")
                $ jinil.add("김진일|와라와라")
                $ jinil.add("주인공|? 엌ㅋㅋㅋㅋㅋㅋㅋ")
                $ jinil.add("김진일|주량은 마실수록 는다.")
                $ jinil.add("연속|그리고 나는 뻔대를 약하게 키우지 않았다.")
                $ jinil.add("연속|그러니까 청두거리 임꺽정으로 와라.")
                $ jinil.add("주인공|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ ㅇㅋㅇㅋ")
                $ jinil.add("주인공|뒤풀이 어느정도 마무리되면 감")
                $ jinil.add("김진일|안 오면 실망할거다...")

        elif week == 4 :
            if day == 0 :
                $ jinil.add("날짜|3월 22일 일요일")
                if gwazam_finished == False :
                    # 투표 진행
                    $ jinil.add("김진일| ㅋㅋㅋㅋㅋ 내가 애들이 이거 좋아할거라고 했지? 아.. 근데 혹시 내가 단톡방에서 좀 오버했나??	")

                else :
                    # 강제 종료
                    $ jinil.add("김진일|과잠 예쁜 것 같아 빨리 입고 싶다ㅋㅋㅋㅋ")


    elif month == 4 :
        if week == 1 :
            if day == 1 :
                $ jinil.add("날짜|4월 2일 월요일")
                $ jinil.add("김진일|엠티는 당연히 대별리지~")
                $ jinil.add("연속|신숲은 무슨 거기로 하면 술마시다가 애들 다 도망간다니까?")
                $ jinil.add("연속|뻔대야 너도 대별리가 좋지??")
                $ jinil.add("연속|대별리 뽑아줘ㅋㅋㅋㅋ")

            elif day == 6 :
                $ jinil.add("날짜|4월 7일 토요일")
                $ jinil.add("김진일|야 어제는 찾아줘서 고맙다")
                $ jinil.add("연속|답례로 다음에 술이나 한 번 살게")
                $ jinil.add("주인공|엌ㅋㅋㅋㅋㅋ 그래서 왜 거기까지 간 건진 기억안나고?")
                $ jinil.add("김진일|ㅁㄹ 눈 떠보니까 거기던데")
                $ jinil.add("연속|ㅋㅋㅋ여튼 진짜 고맙다")
                $ jinil.add("연속|너 아니었음 ㄹㅇ로 미아됐을 뻔")
                $ jinil.add("주인공|ㄴㄴ 뻔대로 당연히 할 일을 했을 뿐임 ㅇㅇ")
                $ jinil.add("김진일|ㅋㅋㅋㅋㅋㅋ 그래 여튼 너도 고생했고")
                $ jinil.add("연속|내일 일요일이니까 푹 쉬삼")

        elif week == 2 :
            if day == 2 :
                $ jinil.add("날짜|4월 10일 화요일")
                $ jinil.add("김진일|와 해장중 실화냐..")
                $ jinil.add("연속|자기가 먼저 같이 듣자고 해서 같이 넣었는데")
                $ jinil.add("연속|이렇게 드랍으로 빠져나간다고??")
                $ jinil.add("주인공|뭐...매일 아침마다 숙취로 고생하니까 그럴 수 있지")
                $ jinil.add("주인공|너도 드랍해도 괜찮지 않음?")
                $ jinil.add("김진일|근데 생각보다 재밌는 수업이라")
                $ jinil.add("연속|야 근데 넌 독강 많지 않냐?")
                $ jinil.add("연속|어떻게 근데 그렇게 잘버티냐")
                $ jinil.add("연속|신기하네 ㅋㅋㅋㅋㅋㅋ")
                $ jinil.add("주인공|뭐.. 어쩌다 보니? ㅋㅋㅋㅋ")

            elif day == 4 :
                $ jinil.add("날짜|4월 12일 금요일")
                $ jinil.add("김진일|아 영화보니까 괜히 코노 가고 싶네")
                $ jinil.add("연속|시험 끝나고 함 가실??")
                $ jinil.add("주인공|엌ㅋㅋㅋㅋㅋㅋ 나야 좋지")
                $ jinil.add("주인공|날 잡아!!")
                $ jinil.add("김진일|무슨 코노에 날까지 잡냐ㅋㅋ 그냥 땡기면")
                $ jinil.add("연속|가면 되는거지 뭐ㅋㅋㅋ")
                $ jinil.add("주인공|ㅇㅈㅇㅈ~ 담에 갠톡하삼")

        elif week == 3 :
            if day == 4 :
                $ jinil.add("날짜|4월 19일 목요일")
                $ jinil.add("김진일|아 공부 하기 진짜 싫다")
                $ jinil.add("연속|그냥 술이나 마시고 싶다")
                $ jinil.add("주인공|ㅠㅜ 시험 끝나고 같이 마시러 가자")
                $ jinil.add("김진일|뭐 그거야 당연한거고")
                $ jinil.add("연속|넌 공부 잘하고 있냐")
                $ jinil.add("주인공|아니..")
                $ jinil.add("김진일|ㅎ...")
                $ jinil.add("주인공|ㅎ...")
                $ jinil.add("김진일|여튼 파이팅..")
                $ jinil.add("주인공|너도..")

    elif month == 5 :
        if week == 1 :
            if day == 2 :
                $ jinil.add("날짜|5월 3일 화요일")
                $ jinil.add("김진일|애들 왤케 안오냐...")
                $ jinil.add("주인공|나도 모르겠다...")

            elif day == 3 :
                $ jinil.add("날짜|5월 4일 수요일")
                $ jinil.add("김진일|어제 너무 많이 마셨다 ㅋㅋㅋㅋ")
                $ jinil.add("연속|죽을것 같다")
                $ jinil.add("주인공|ㅋㅋㅋ 어제 수고했다")

        elif week == 2 :
            if day == 4 :
                $ jinil.add("날짜|5월 12일 목요일")
                $ jinil.add("김진일|애들 왜이렇게 투표 안하냐")
                $ jinil.add("연속|쪼아봐 ㅋㅋ")

            elif day == 6 :
                $ jinil.add("날짜|5월 14일 토요일")
                $ jinil.add("김진일|밤에 장중이랑 술 ㄱㄱ?")
                $ jinil.add("연속|운동회 얘기도 조금 해야할 것 같은데")

        elif week == 3 :
            if day == 1 :
                $ jinil.add("날짜|5월 16일 월요일")
                $ jinil.add("김진일|야")
                $ jinil.add("연속|너는 거기서 나를 놀리는데")
                $ jinil.add("연속|보고만 있냐?")
                $ jinil.add("연속|뻔대가 말려야지")

            elif day == 3 :
                $ jinil.add("날짜|5월 18일 수요일")
                $ jinil.add("김진일|야 내가 그래도")
                $ jinil.add("연속|너 생각해서 준비위 해준다 ")
                $ jinil.add("연속|너도 내 편이지??")

        elif week == 4 :
            if day == 1 :
                $ jinil.add("날짜|5월 23일 월요일")
                $ jinil.add("김진일|야야")
                $ jinil.add("연속|다 너 공연 홍보하느라고 그런거야")
                $ jinil.add("연속|나 능청스럽게 잘하지 않냐 ㅋㅋㅋ")

            elif day == 6 :
                $ jinil.add("날짜|5월 28일 토요일")
                $ jinil.add("김진일|동아리 가서 잘하고 있어 ㅋㅋㅋ")
                $ jinil.add("연속|내가 애들하고 놀다가")
                $ jinil.add("연속|네 공연 가자고 해봄 ㅋㅋㅋ")

    elif month == 6 :
        if week == 1 :
            if day == 4 :
                $ jinil.add("날짜|6월 5일 목요일")
                $ jinil.add("김진일|나는 공연 보러 못 갈 것 같다")
                $ jinil.add("연속|미안미안")

        elif week == 2 :
            if day == 0 :
                $ jinil.add("날짜|6월 8일 일요일")
                $ jinil.add("김진일|뻔대야")
                $ jinil.add("연속|너 혹시 경원 족보있냐?")
                $ jinil.add("연속|공부 하나도 안했네 ㅋㅋㅋ")

            elif day == 5 :
                $ jinil.add("날짜|6월 13일 목요일")
                $ jinil.add("김진일|경원 족보 아직도 못구했다...")

        elif week == 3 :
            if day == 0 :
                $ jinil.add("날짜|6월 15일 일요일")
                $ jinil.add("김진일|뻔대야")
                $ jinil.add("연속|공부 안되지 ㅋㅋㅋㅋ")
                $ jinil.add("연속|방학때 삼용이 집 가는거 기획해볼래 ㅋㅋㅋ")

            elif day == 4 :
                $ jinil.add("날짜|6월 19일 목요일")
                $ jinil.add("김진일|오덕현 개웃기지 않냐 ㅋㅋㅋ")
                $ jinil.add("연속|나도 저 말투 빠지겠닼ㅋㅋㅋㅋ")
                $ jinil.add("연속|오이오이라닠ㅋㅋㅋㅋㅋ")
                $ jinil.add("연속|미친거 아니냐 진짜 ㅋㅋㅋㅋㅋ")

            elif day == 5 :
                $ jinil.add("날짜|6월 20일 금요일")
                $ jinil.add("김진일|뻔대야")
                $ jinil.add("연속|근데 진짜 우리냐 동아리냐 ㅋㅋㅋㅋ")
    return
