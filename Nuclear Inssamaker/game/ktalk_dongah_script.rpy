# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
label change_dongah_talk :
    if month == 3 :
        if week == 1 :
            if day == 3 :
                $ dongah.add("날짜|3월 4일 수요일")
                $ dongah.add("이동아|마 니 뻔대도 하고 잘나가대? ㅋㅋㅋㅋㅋ")
                $ dongah.add("연속|바빠서 연락도 잘 없고 조금 실망했디?")
                $ dongah.add("주인공|엌ㅋㅋㅋㅋ미안미안 좀 바빴다;;;")
                $ dongah.add("주인공|아 맞다 니 그거 들었나?")
                $ dongah.add("주인공|다음주 월요일날 동소제 한다던데?")
                $ dongah.add("이동아|오~동소제? 이번에도 동아리 함 같이 할까?")
                $ dongah.add("주인공|당연하제~ㅋㅋㅋㅋㅋㅋ 그래도 니랑 내랑 인연이 몇 년인데")
                $ dongah.add("주인공|이 학교에서도 공연 계속 같이해야지!")
                $ dongah.add("이동아|오키오키! 그럼 다음주 월욜날 어디 들어갈지 돌아다녀보면서 정하자.")
                $ dongah.add("이동아|괜찮제?")
                $ dongah.add("주인공|오키도키! 당연하지! ㅋㅋㅋ")
                $ dongah.add("주인공|같이 둘러보고 제일 좋아보이는 곳으로 들어가자.")
                $ dongah.add("이동아|오야~")

        elif week == 2 :
            if day == 0 :
                $ dongah.add("날짜|3월 8일 일요일")
                $ dongah.add("이동아|야~죽었나?ㅋㅋㅋㅋ")
                $ dongah.add("이동아|내일 동소젠거 알제?")
                $ dongah.add("주인공|당연하지ㅋㅋㅋㅋ 설마 내가 까먹었겠냐ㅋㅋㅋㅋ")
                $ dongah.add("이동아|에이 혹시 모른다이가ㅋㅋㅋㅋㅋ")
                $ dongah.add("이동아|그래서 물어봤지")
                $ dongah.add("주인공|당연히 기억하지, 그래 내일 몇 시에 볼까?")
                $ dongah.add("이동아|니 수업 몇 시에 끝나는데?")
                $ dongah.add("이동아|난 12시 반쯤")
                $ dongah.add("주인공|아;; 난 1시 쯤에 끝나는데;;")
                $ dongah.add("이동아|글나..음 그럼 내가 먼저 가서 둘러보고 있을게")
                $ dongah.add("주인공|오옹 그래주면 나야 고맙지ㅋㅋㅋㅋㅋ")
                $ dongah.add("주인공|그럼 내일 수업마치고 톡할게, 그때 보제이~")
                $ dongah.add("이동아|오키도키~")

            elif day == 6 :
                $ grouptalk.add("날짜|3월 14일 토요일")
                $ grouptalk.add("이동아|니 아직도 엠티가?")
                $ grouptalk.add("연속|에? 밥도 묵고")
                $ grouptalk.add("연속|사우나도 하고")

        elif week == 3 :
            if day == 2 :
                $ grouptalk.add("날짜|3월 17일 수요일")
                $ grouptalk.add("이동아|니 동아리 과잠 맞출거가?")
                $ grouptalk.add("연속|맞출거면 이번주까지 알려도")
                $ grouptalk.add("주인공|ㅇㅋㅇㅋ")
                $ grouptalk.add("연속|그리고 이번주에 술 한잔 할래?")
                $ grouptalk.add("연속|오랜만에 둘이 한잔 해야재")
                $ grouptalk.add("주인공|이번 주 과 행사 끝나면 연락할게")

        elif week == 4 :
            if day == 1 :
                $ grouptalk.add("날짜|3월 23일 월요일")
                $ grouptalk.add("이동아|이번에 고향 애들 서울 올라온다는데")
                $ grouptalk.add("연속|한 번 만나야재")
                $ grouptalk.add("주인공|ㅇㅋㅇㅋ 한 번 만나야재")
                $ grouptalk.add("주인공|내가 연락할게")

    elif month == 4 :
        if week == 1 :
            if day == 2 :
                $ grouptalk.add("날짜|4월 3일 화요일")
                $ grouptalk.add("이동아|우리 학기말에 동아리 공연있는거 알재?")
                $ grouptalk.add("연속|해운대 나얼 어디 안가게 목관리 잘해라")
                $ grouptalk.add("연속|선배들이 니 엄청 기대하고 있다")
                $ grouptalk.add("주인공|레알?ㅋㅋㅋ 긴장되네ㅠㅠ")
                $ grouptalk.add("주인공|니가 많이 도와줘 ㅋㅋㅋㅋ")

        elif week == 2 :
            if day == 0:
                $ grouptalk.add("날짜|4월 8일 일요일")
                $ grouptalk.add("이동아|이번 주에 집에 갈래?")
                $ grouptalk.add("연속|시험보기 전에 고등학교 애들 보고 오자 ㅋㅋㅋ")
                $ grouptalk.add("주인공|오... 좋다!")
                $ grouptalk.add("주인공|언제 갈거야?")
                $ grouptalk.add("이동아|금요일 오후에 가자 ㅋㅋㅋ")
                $ grouptalk.add("주인공|나 일정 봐보고 연락할게 ㅋㅋㅋ")

        elif week == 3 :
            if day == 1 :
                $ grouptalk.add("날짜|4월 16일 월요일")
                $ grouptalk.add("주인공|오늘 축제 가? 네가 좋아하는 소란 오던데 ㅋㅋㅋ")
                $ grouptalk.add("주인공|나 과 얘들이랑 가기는 하는데 혹시 너 가면 같이 놀자 ㅋㅋㅋ")
                $ grouptalk.add("이동아|됐다 ㅋㅋㅋ 과 얘들이랑 놀아라")
                $ grouptalk.add("주인공|ㅋㅋㅋㅋ 그래도 혹시 오면 이따 연락해")
                $ grouptalk.add("이동아|ㅇㅋㅇㅋ")

            elif day == 5 :
                $ grouptalk.add("날짜|4월 20일 금요일")
                $ grouptalk.add("이동아|이따 같이 시험공부 할래?")
                $ grouptalk.add("주인공|나는 과 친구들이랑 할 것 같은데 ㅋㅋㅋ")
                $ grouptalk.add("주인공|어디야 ㅋㅋㅋ 글로 갈까?")
                $ grouptalk.add("이동아|아 그럼 그냥 다음에 같이 하자 ㅋㅋㅋ")
                $ grouptalk.add("주인공|ㅋㅋㅋㅋ 이따 야식이나 먹자")
                $ grouptalk.add("이동아|ㅋㅋㅋ 그래그래")

        elif week == 4 :

    elif month == 5 :
        if week == 1 :
            if day == 2 :
                $ grouptalk.add("날짜|5월 3일 화요일")
                $ grouptalk.add("이동아|오늘 장터 하대?")
                $ grouptalk.add("연속|수업 끝나고 갈게 ㅋㅋㅋㅋ")
                $ grouptalk.add("주인공|올... 어떻게 알았냐 ㅋㅋㅋ")
                $ grouptalk.add("이동아|페북 봤다 ㅋㅋㅋ 좋아요도 눌렀다")
                $ grouptalk.add("연속|동아리 애들 데리고 갈게")
                $ grouptalk.add("주인공|와 감사감사!!!")
                $ grouptalk.add("주인공|내가 서비스도 많이 줄게 ㅋㅋㅋㅋ")
                $ grouptalk.add("이동아|적자 볼 각오해라 ㅋㅋㅋㅋ")

        elif week == 2 :
            if day == 2 :
                $ grouptalk.add("날짜|5월 10일 화요일")
                $ grouptalk.add("이동아|이따가 동아리 점모 올거?")
                $ grouptalk.add("주인공|아.. 나 오늘 과 행사 있어 ㅠㅠ")
                $ grouptalk.add("이동아|핵인싸 고향친구 보기 힘드네 ㅋㅋㅋㅋ")
                $ grouptalk.add("주인공|ㅠㅠㅠ 내가 다음에 밥 살게")

        # elif week == 3 :

        elif week == 4 :
            if day == 0 :
                $ grouptalk.add("날짜|5월 22일 일요일")
                $ grouptalk.add("이동아|야 너 잘 들어간거가?")
                $ grouptalk.add("연속|갑자기 전화해서 이상한 소리하던데")
                $ grouptalk.add("연속|어디 장기 털린데는 없나?")
                $ grouptalk.add("주인공|자고 일어났는데 몸이 가벼워...")
                $ grouptalk.add("주인공|다 털린듯 영혼까지")
                $ grouptalk.add("이동아|ㅋㅋㅋㅋㅋ 그래도 살아있네")
                $ grouptalk.add("주인공|먹은거 다 토하니까 그나마 낫다ㅋㅋㅋㅋ")
                $ grouptalk.add("주인공|지금 술병나서 계속 누워있음")
                $ grouptalk.add("이동아|장기 있으면 됐지 ㅋㅋㅋㅋ")
                $ grouptalk.add("연속|몸 조리 잘해라 ㅋㅋㅋ")
                $ grouptalk.add("주인공|ㅇㅋ 감사요")
    elif month == 6 :
        if week == 1 :
            if day == 1 :
                $ dongah.add("날짜|6월 2일 월요일")
                $ dongah.add("이동아|마, 니 연습 잘 되가나?")
                $ dongah.add("연속|오늘도 올꺼제?")
                $ dongah.add("연속|연습 끝나도 동아리 계속 나올꺼가?")

            elif day == 3 :
                $ dongah.add("날짜|6월 4일 수요일")
                $ dongah.add("이동아|니 내일 시간 되나?")
                $ dongah.add("연속|공연 전에 한 잔 하자")
                $ dongah.add("연속|오랜만에 찐한 얘기도 좀 하고")

            elif day == 5 :
                $ dongah.add("날짜|6월 6일 금요일")
                $ dongah.add("이동아|와 니 고생했다")
                $ dongah.add("연속|억수로 잘하대?")
                $ dongah.add("연속|뻔대한다고")
                $ dongah.add("연속|노래 못해졌을줄 알았는데")
                $ dongah.add("연속|해운대 나얼 어디 안갔네")
                $ dongah.add("연속|수고했다")
                $ dongah.add("연속|다음 학기에는")
                $ dongah.add("연속|뻔대 좀 쉬고 동아리 해라")

        elif week == 2 :
            if day == 5 :
                $ dongah.add("날짜|6월 13일 목요일")
                $ dongah.add("이동아|밥먹고 공부 ㄱ?")
                $ dongah.add("연속|다음주에 시험 몇 개 보는데?")

        elif week == 3 :
            if day == 4 :
                $ dongah.add("날짜|6월 19일 목요일")
                $ dongah.add("이동아|시험 끝났나??")
                $ dongah.add("연속|동아리 종파 올꺼가?")
                $ dongah.add("연속|선배들이 니 꼬셔서")
                $ dongah.add("연속|좀 열심히하게 하란다 ㅋㅋ")

    return
