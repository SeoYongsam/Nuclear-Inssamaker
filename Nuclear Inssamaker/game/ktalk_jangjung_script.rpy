# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_jangjung_talk :
    if month == 3 :
        if week == 1 :
            if day == 0 :
                $ jangjung.add("핫|핫")

            elif day == 1 :
                $ jangjung.add("날짜|3월 2일 월요일")
                $ jangjung.add("장중|테스트")
                $ jangjung.add("연속|잘 되려나\n되겠지")
                $ jangjung.add("진일|안녕")
                $ jangjung.add("삼용|즐거운 하루가 되길")
                $ jangjung.add("동아|으아악\n테스트")
                $ jangjung.add("연속|잘 되려나\n되겠지")
                $ jangjung.add("미래|난 현재 여친\nㅋㅋ")
                $ jangjung.add("주인공|이것도 테스트")

            elif day == 2 :
                $ jangjung.add("날짜|3월 3일 화요일")
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("날짜|3월 4일 수요일")
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("진일|테스트")

            elif day == 5 :
                $ jangjung.add("미래|테스트")

            elif day == 6 :
                $ jangjung.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("장중|나랑 같이 미팅 갈거??")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                # 투표 진행
                $ jangjung.add("장중|이거 투표로 되면 진짜 할거야? 하…. 걱정되네")

                # 강제 종료
                $ jangjung.add("장중|과잠 만드느라 진짜 고생했어 ㅋㅋㅋ 우리 조만간 술 마시자")
            elif day == 1 :
                # 투표 진행
                $ jangjung.add("장중|와 우리 이렇게 고생하는데 애들 너무한 것 같지 않냐 ㅠㅠ")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|이제 뻔엠 ㄱㄱ?")

            elif day == 4 :
                $ jangjung.add("장중|뻔엠 ㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱㄱ")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")


    elif month == 4 :
        if week == 1 :
            if day == 0 :
                $ jangjung.reset()
                $ jangjung.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ jangjung.add("날짜|3월 2일 월요일")
                $ jangjung.add("장중|테스트")

            elif day == 2 :
                $ jangjung.add("날짜|3월 3일 화요일")
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("날짜|3월 4일 수요일")
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("진일|테스트")

            elif day == 5 :
                $ jangjung.add("미래|테스트")

            elif day == 6 :
                $ jangjung.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

    elif month == 5 :
        if week == 1 :
            if day == 0 :
                $ jangjung.reset()
                $ jangjung.add("날짜|5월 1일 일요일")
            if day == 1 :
                $ jangjung.add("날짜|3월 2일 월요일")
                $ jangjung.add("장중|테스트")

            elif day == 2 :
                $ jangjung.add("날짜|3월 3일 화요일")
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("날짜|3월 4일 수요일")
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("진일|테스트")

            elif day == 5 :
                $ jangjung.add("미래|테스트")

            elif day == 6 :
                $ jangjung.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

    elif month == 6 :
        if week == 1 :
            if day == 0 :
                $ jangjung.reset()
                $ jangjung.add("날짜|4월 1일 일요일")
            if day == 1 :
                $ jangjung.add("날짜|3월 2일 월요일")
                $ jangjung.add("장중|테스트")

            elif day == 2 :
                $ jangjung.add("날짜|3월 3일 화요일")
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("날짜|3월 4일 수요일")
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("진일|테스트")

            elif day == 5 :
                $ jangjung.add("미래|테스트")

            elif day == 6 :
                $ jangjung.add("주인공|테스트")

        elif week == 2 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")

        elif week == 4 :
            if day == 0 :
                $ jangjung.add("장중|이건 실행이 됨")

            elif day == 1 :
                $ jangjung.add("장중|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ jangjung.add("삼용|테스트")

            elif day == 3 :
                $ jangjung.add("장중|테스트")

            elif day == 4 :
                $ jangjung.add("장중|테스트")

            elif day == 5 :
                $ jangjung.add("장중|테스트")

            elif day == 6 :
                $ jangjung.add("장중|테스트")
    return
