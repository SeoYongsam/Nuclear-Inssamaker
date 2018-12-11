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
                $ dongah.add("주인공|옼돜! 당연하지! ㅋㅋㅋ")
                $ dongah.add("주인공|같이 둘러보고 제일 좋아보이는 곳으로 들어가자.")
                $ dongah.add("이동아|오야~")

        elif week == 2 :
            if day == 0 :
                $ dongah.add("날짜|3월 8일 일요일")
                $ dongah.add("이동아|야~죽었나?ㅋㅋㅋㅋ")
                $ dongah.add("이동아|내일 동소젠거 알제?")
                $ dongah.add("주인공|당연하짘ㅋㅋㅋㅋ 설마 내가 까먹었겠냨ㅋㅋㅋㅋ")
                $ dongah.add("이동아|에이 혹시 모른다이갘ㅋㅋㅋㅋㅋ")
                $ dongah.add("이동아|그래서 물어봤지")
                $ dongah.add("주인공|당연히 기억하지, 그래 내일 몇 시에 볼까?")
                $ dongah.add("이동아|니 수업 몇 시에 끝나는데?")
                $ dongah.add("이동아|난 12시 반쯤")
                $ dongah.add("주인공|아;; 난 1시 쯤에 끝나는데;;")
                $ dongah.add("이동아|글나..음 그럼 내가 먼저 가서 둘러보고 있을게")
                $ dongah.add("주인공|오옹 그래주면 나야 고맙짘ㅋㅋㅋㅋㅋ")
                $ dongah.add("주인공|그럼 내일 수업마치고 톡할게, 그때 보제이~")
                $ dongah.add("이동아|오키도키~")

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
