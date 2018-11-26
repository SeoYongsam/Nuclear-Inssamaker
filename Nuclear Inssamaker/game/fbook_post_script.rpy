# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_fbook_post :
    if month == 3 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("그림자")
                $ fbook_post_add("본문|캐릭터이름|날짜|포스트 내용")
                $ fbook_post_add("그림자")

            elif day == 1 :
                $ fbook_post_add("본문|캐릭터이름|날짜|포스트 내용")

            elif day == 2 :
                $ fbook_post_add("본문|캐릭터이름|날짜|포스트 내용")

            elif day == 3 :
                $ fbook_post_add("본문|캐릭터이름|날짜|포스트 내용")

            elif day == 4 :
                $ fbook_post_add("본문|진일|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|미래|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|주인공|날짜|테스트")

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

        elif week == 3 :
            if day == 0 :
                $ fbook_post_add("본문|테스트|2018년 2월 28일|가가가가가가가가가가\n가가몇글자가가가가가가19글자")
                $ fbook_post_add("그림자")
                $ fbook_post_add("본문|동삼용|2018년 3월 15일|어제 총엠 존잼!!!!!1111222\n근데 어제 선배랑 손잡고 산책가던\n사람 보기 좋더라~ ㅋㅋㅋㅋ")
                $ fbook_post_add("그림자")

            elif day == 1 :
                $ fbook_post_add("본문|김진일|2018년 3월 16일|아~ XX학번 형 누나들 별거아니네 ㅋㅋ\n다들 술 왜 이렇게 못마시지....:P\n총엠 후 2라운드 ㄱㄱ 하실분?")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|술은 역시 해장술이지ㅎ'")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")

            elif day == 2 :
                $ fbook_post_add("본문|해장중|2018년 3월 17일|오늘 밤에 술 마실사람?")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|진일|ㄱㄱㄱㄱ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")

            elif day == 3 :
                $ fbook_post_add("본문|해장중|2018년 3월 18일|과잠 Coming Soon!!")
                $ fbook_post_add("그림자")

            elif day == 4 :
                $ fbook_post_add("본문|안금지|2018년 3월 19일|우리 과잠 더 예뻤으면 좋겠다...")
                $ fbook_post_add("그림자")

            elif day == 5 :
                $ fbook_post_add("본문|유현재|2018년 3월 20일| {color=#808080}유현재님이 노미래님과 {color=#ff0000}연애중{color=#808080}입니다.")
                $ fbook_post_add("그림자")

            elif day == 6 :
                $ fbook_post_add("본문|유현재|2018년 3월 21일|날씨가 아직 춥다...\n하지만 미래 덕분에 마음은 따뜻따뜻~~~ <3{color=#808080}-현재님은 {color=ff0000}사랑{/color}에 빠져있습니다")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|미래|ㅋㅋㅋㅋ과잠 나오면 따뜻하게\n그거 입고 다니자~~~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")

        elif week == 4 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")


    elif month == 4 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("본문|날짜|날짜|4월 1일 일요일")
            if day == 1 :
                $ fbook_post_add("본문|날짜|날짜|3월 2일 월요일")
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 2 :
                $ fbook_post_add("본문|날짜|날짜|3월 3일 화요일")
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|날짜|날짜|3월 4일 수요일")
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|진일|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|미래|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|주인공|날짜|테스트")

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

        elif week == 3 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

        elif week == 4 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

    elif month == 5 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("본문|날짜|날짜|5월 1일 일요일")
            if day == 1 :
                $ fbook_post_add("본문|날짜|날짜|3월 2일 월요일")
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 2 :
                $ fbook_post_add("본문|날짜|날짜|3월 3일 화요일")
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|날짜|날짜|3월 4일 수요일")
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|진일|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|미래|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|주인공|날짜|테스트")

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

        elif week == 3 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

        elif week == 4 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

    elif month == 6 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("본문|날짜|날짜|4월 1일 일요일")
            if day == 1 :
                $ fbook_post_add("본문|날짜|날짜|3월 2일 월요일")
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 2 :
                $ fbook_post_add("본문|날짜|날짜|3월 3일 화요일")
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|날짜|날짜|3월 4일 수요일")
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|진일|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|미래|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|주인공|날짜|테스트")

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

        elif week == 3 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")

        elif week == 4 :
            if day == 0 :
                $ fbook_post_add("본문|장중|날짜|이건 실행이 됨")

            elif day == 1 :
                $ fbook_post_add("본문|장중|날짜|캐릭터이름과 메시지를 변경하세요")

            elif day == 2 :
                $ fbook_post_add("본문|삼용|날짜|테스트")

            elif day == 3 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 4 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 5 :
                $ fbook_post_add("본문|장중|날짜|테스트")

            elif day == 6 :
                $ fbook_post_add("본문|장중|날짜|테스트")
    return
