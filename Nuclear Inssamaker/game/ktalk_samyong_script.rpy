# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_samyong_talk :
    if month == 3 :
        if week == 2 :
            if day == 1 :
                $ samyong.add("날짜|3월 9일 월요일")
                $ samyong.add("동삼용|문정과 대표 가수! 우리 뻔대님!!!")
                $ samyong.add("연속|ㅠㅜㅠㅜ 진짜 너무 잘 불러서 놀랐음!!")
                $ samyong.add("주인공|허허허 과찬이십니다..")
                $ samyong.add("동삼용|아녀 아녀!! 진짜 잘하더라")
                $ samyong.add("연속|다음에도 기회된다면 다시 노래 듣고 싶다")
                $ samyong.add("연속|단톡에서는 말은 못했지만 공연 꼭 보러 갈게!!")
                $ samyong.add("연속|파이팅 파이팅~~!")
                $ samyong.add("주인공|ㅋㅋㅋㅋ 고마우이~")

        elif week == 4 :
            if day == 0 and gwazam_finished == False :
                # 과잠 투표 진행
                $ samyong.add("날짜|3월 22일 일요일")
                $ samyong.add("동삼용|이거 애들이 좋아할까?? 난 진짜 모르겠어 ㅋㅋㅋ 내가 투표 안한 애들 물어봤는데 지금 별로라서 투표 안하는거라던데")

            elif day == 1 :
                if gwazam_finished == True :
                    # 투표 종료
                    $ samyong.add("동삼용|뻔대야 우리끼리 조만간 같이 놀러 가자 ㅋㅋㅋ")

                else :
                    # 투표 진행
                    $ samyong.add("동삼용|투표 안한 애들이 이거 별로라고 생각한다는데 어떡하지 하…. 다시 만들어야하나?")

            elif day == 2 :
                if gwazam_finished == True :
                    # 투표 종료
                    $ samyong.add("동삼용|내일 점모 중식 너무 좋다 ㅋㅋㅋ 나 배려해줘서 고마워")

                else :
                    # 투표 진행
                    $ samyong.add("동삼용|금지는 갠톡왔는데 돈이 없어서 못살 것 같대… 33개만 주문하자")


    elif month == 4 :
        if week == 1 :
            if day == 1 :
                $ samyong.add("날짜|4월 2일 월요일")
                $ samyong.add("동삼용|엠티는 가까운데가 최고임")
                $ samyong.add("연속|괜히 멀리 갔다가 저번 처럼 너 2호선 한바퀴 돈다니까")
                $ samyong.add("연속|가는데도 오래걸리고, 오는데도 오래걸리고")
                $ samyong.add("연속|빠르게 가까운데로 조지는게 몸도 시간도 아끼는 거임 ㅇㅇ")
                $ samyong.add("연속|답은? 신숲이다~")

            elif day == 4 :
                # 장발 마감 안했을 시
                $ samyong.add("날짜|4월 5일 목요일")
                $ samyong.add("동삼용|와..애들 진짜 너무한 거 아니냐...")
                $ samyong.add("연속|아무리 일이 생겨도 그렇지 장발 저렇게 쉽게 포기해도 되는거냐;;")
                $ samyong.add("주인공|뭐 어쩔 수 없지 ㅠㅜㅠㅜ")
                $ samyong.add("동삼용|그래도 우리라도 있으니까! 힘내고")
                $ samyong.add("연속|많이 도와줄게 ㅋㅋㅋㅋ")
                $ samyong.add("연속|내일 보자! ㅋㅋㅋㅋ")
                $ samyong.add("주인공|ㅠㅜㅠㅜㅠㅜ 진짜 감사함 ㅠㅜㅜ")

                # 장발 마감 했을 시
                $ samyong.add("날짜|4월 5일 목요일")
                $ samyong.add("동삼용|오오오오오 드디어 내일!! 두근두근")
                $ samyong.add("주인공|ㅋㅋㅋㅋㅋㅋㅋㅋ 기대 된다!!")
                $ samyong.add("동삼용|ㅇㅇ 진짜 ㅋㅋㅋ 내일 장발도 있으니까")
                $ samyong.add("연속|오늘 푹쉬고! 내일보자")
                $ samyong.add("주인공|그래그래~")

            elif day == 6 :
                $ samyong.add("주인공|테스트")

        elif week == 2 :
            if day == 3 :
                $ samyong.add("날짜|4월 11일 수요일")
                $ samyong.add("동삼용|음...내가 너무 단톡에서 중간고사 얘기 밖에 안하나..?")
                $ samyong.add("연속|난 애들한테 그냥 일정 알려주려고 하는 것 뿐인데")
                $ samyong.add("연속|너무 과했나...ㅠㅜㅠ")
                $ samyong.add("연속|뻔대야 넌 어떻게 생각해? 내가 괜한 오지랖임?")
                $ samyong.add("주인공|음..ㄴㄴ 그래도 너가 언급 안했으면")
                $ samyong.add("주인공|애들 위기의식도 못느꼈을걸?")
                $ samyong.add("주인공|내가 봤을 때는 괜찮은 것 같음")
                $ samyong.add("동삼용|음..그럼 다행이고")
                $ samyong.add("연속|여튼 오늘 간맥 어디서 함??")
                $ samyong.add("연속|나도 가게 ㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ samyong.add("주인공|엌ㅋㅋㅋㅋㅋㅋㅋㅋ")

        elif week == 3 :
            if day == 0 :
                $ samyong.add("날짜|4월 15일 일요일")
                $ samyong.add("주인공|오~ 소란 아는 사람 처음 본듯")
                $ samyong.add("동삼용|엌ㅋㅋㅋ 난 뻔대 너라면 알 거라고 생각은 했는데")
                $ samyong.add("연속|진짜 알고 있네")
                $ samyong.add("주인공|ㅋㅋㅋㅋㅋ 당연하지")
                $ samyong.add("주인공|라이브 너무 잘하셔서 유툽에서 맨날 보고 있다고")
                $ samyong.add("동삼용|내말이 ㅋㅋㅋㅋㅋㅋ")
                $ samyong.add("연속|진짜 음원 씹어드신 것 같다니까")
                $ samyong.add("연속|세션들도 너무 잘하고")
                $ samyong.add("주인공|오오 내일 직접 볼 수 있다니")
                $ samyong.add("주인공|기대기대")
                $ samyong.add("동삼용|기대기대")

            elif day == 3 :
                $ samyong.add("날짜|4월 18일 수요일")
                $ samyong.add("동삼용|아..공부 귀찮다")
                $ samyong.add("연속|뻔대야 넌 공부 잘 하고 있음??")
                $ samyong.add("주인공|공부 잘 하고 있었으면 단톡에서")
                $ samyong.add("주인공|저런 뻘글은 얘기 안했겠지 ㅋㅋㅋ")
                $ samyong.add("동삼용|엌ㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ samyong.add("연속|하 그래도")
                $ samyong.add("연속|대학 와서 첫 시험인데")
                $ samyong.add("연속|잘 보고 싶긴 하다..")
                $ samyong.add("주인공|허허..우리 존재 파이팅..")

        elif week == 4 :
            if day == 3 :
                $ samyong.add("동삼용|뻔대야 너도 야식 ㄱㄱ??")
                $ samyong.add("연속|치킨 먹는대 ㅋㅋㅋ")

            elif day == 6 :
                $ samyong.add("동삼용|우리 월요일에 장보는거 맞지?")
                $ samyong.add("주인공 |ㅇㅇ 장터가 화요일이니까 그 전날!!")
                $ samyong.add("동삼용|아 ㅇㅋㅇㅋ 잘못알고 있나 해서 ㅋㅋㅋ")
                $ samyong.add("연속|수고한다 ㅋㅋㅋ 조금만 더 힘내자!")

    elif month == 5 :
        if week == 1 :
            if day == 2 :
                $ samyong.add("날짜|5월 3일 화요일")
                $ samyong.add("동삼용|나 수업 끝났다")
                $ samyong.add("연속|지금 갈게!!!")
                $ samyong.add("주인공|엉엉 ㅋㅋㅋ 얼른 와!!!")

            elif day == 3 :
                $ samyong.add("날짜|5월 4일 수요일")
                $ samyong.add("동삼용|우리 돈 어제 뒷풀이에서 진짜 다 썼어??")
                $ samyong.add("주인공|나도 얼마 남았는지 모르겠어 ㅠㅠ 나중에 정확한 금액은 공지로 알려줄게!")

        elif week == 4 :
            if day == 4 :
                $ samyong.add("날짜|5월 26일 목요일")
                $ samyong.add("동삼용|뻔대야")
                $ samyong.add("연속|요즘 분위기 안 좋은데")
                $ samyong.add("연속|과 톡에다가 그런거 올리면")
                $ samyong.add("연속|애들 더 떠나겠다...")
                $ samyong.add("연속|좀만 더 신경써라")
                $ samyong.add("연속|나한테 갠톡와서")
                $ samyong.add("연속|애들이 뭐라하더라...")

    elif month == 6 :
        if week == 1 :
            if day == 1 :
                $ samyong.add("날짜|6월 2일 월요일")
                $ samyong.add("동삼용|너 어제 못와서 아쉽 ㅠ")
                $ samyong.add("연속|동아리 끝나면 한 잔 해")

            elif day == 2 :
                $ samyong.add("날짜|6월 3일 화요일")
                $ samyong.add("동삼용|네 공연 보러가자는 얘들이 없네 ㅠ")
                $ samyong.add("연속|혼자 가기는 좀 뭐한데...")

        elif week == 2 :
            if day == 3 :
                $ samyong.add("날짜|6월 11일 수요일")
                $ samyong.add("동삼용|뻔대야")
                $ samyong.add("연속|공부중임?")
                $ samyong.add("연속|야식 먹으러 올래 ㅋㅋㅋ")
                $ samyong.add("연속|좀 비싸서 N빵하고 싶은데 ㅋㅋㅋㅋ")

            elif day == 5 :
                $ samyong.add("날짜|6월 13일 목요일")
                $ samyong.add("동삼용|뻔대님")
                $ samyong.add("연속|같이 공부하실??")

        elif week == 3 :
            if day == 0 :
                $ samyong.add("날짜|6월 15일 일요일")
                $ samyong.add("동삼용|ㅋㅋㅋㅋㅋ")
                $ samyong.add("연속|시험 끝나고")
                $ samyong.add("연속|방학 삼용투어 기획할래?? ㅋㅋㅋ")
                $ samyong.add("연속|얘들이 좋아할 것 같은데 ㅋㅋㅋㅋ")
                $ samyong.add("연속|나한테 갠톡도 많이오더라")
                $ samyong.add("연속|너도 그때 놀러와 ㅋㅋㅋㅋ")

            elif day == 2 :
                $ samyong.add("날짜|6월 17일 화요일")
                $ samyong.add("동삼용|우리 종파 언제지?")

            elif day == 6 :
                $ samyong.add("날짜|6월 21일 토요일")
                $ samyong.add("동삼용|나는 좀 늦게 갈 것 같아")
                $ samyong.add("연속|부모님이 오셔서")
                $ samyong.add("연속|오늘도 고생해")
                $ samyong.add("연속|다음 학기에도")
                $ samyong.add("연속|과 행사 잘 부탁할게!")
    return
