# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_fbook_post :
    if month == 3 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("본문|동삼용|2019년 3월 1일|학기 시작도 전에 뻔모 하는 클라스~~ 문정과 OO학번 화이팅~! 뻔대 친구 어제 병샷하고 분위기 띄우느라 고생많았어! ㅋㅋㅋㅋㅋ #뻔대 #인싸 #문정과 #신입생 #클라스")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|유현재|크 너무 재밌었구요~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 1 :
                $ fbook_post_add("본문|안금지|2019년 3월 2일|오늘은 모꼬지 친구들과 재밌게 놀았다 ^^ 얘들아 우리 오래가자~ #모꼬지 #OO학번 #개강 첫날 #입학")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|해장중|2019년 3월 4일|오늘은 간맥~ 나라고 언제나 죽을 때까지 마시는 건 아니다~ 이 말이야!! #간맥 #절주 #간파이팅")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|박대현|이 분 500잔에 소주 반 병 타고 마시고 있답니다. 글 내려주시죠")
                $ fbook_post_add("댓글|해장중|으에ㅋㅋ 나 아지ㅋㅋㅋ ㅓㄷ 마실ㄹㄹ거ㅇㅁㅣㅋㅌㅋㅋㅋㅌㅋㅌㅋㄱㅋㅌㅌㅋ ㅡㅏㅏㅏ깁ㅜㄴㄴ 좋타ㅋㅋㅋㅌㅌㅋㄱㅋㄱㄲㅋ")
                $ fbook_post_add("댓글|김진일|아 얘도 나랑 마시기엔 많이 약하네;; 나랑 대작할 사람 없냐...;;")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 4 :
                $ fbook_post_add("본문|김진일|2019년 3월 5일|앞으로는 스승이라 불러라 제자야. @해장중 #대작 #소주 #술술 #노컨디션 #노여명")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|받들어 모시겠습니다. 스승님")
                $ fbook_post_add("댓글|오덕현|센세~ 와타시에게도 그 비법을~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|유현재|2019년 3월 8일|수업에 항상 도움을 주는 친구에게 식사 보답 후 간단하게 맥주 조지기~ @노미래 앞으로도 가끔씩 잘 부탁할게~ ^^")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|노미래|ㅎㅎ 아냐 수업 많이 겹치는데 서로 돕고 살아야지 : ) 나도 잘 부탁해~")
                $ fbook_post_add("댓글|김진일|ㅗㅜㅑ 둘이 밥먹고 술약까지 간 거 실화냐??")
                $ fbook_post_add("댓글|해장중|ㅗㅜㅑㅗㅜㅑ 님들 Hoxy???")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 1 :
                $ fbook_post_add("본문|박대현|2019년 3월 9일|동소제 직캠! 세상 사람들 많이많이 보세요! 이 사람이 저희 뻔대에요~ #버스킹 #라이브 #잘한다잘한다내새끼 #최고존엄보컬")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|와 ㄹㅇ 개 잘해 진짜")
                $ fbook_post_add("댓글|김진일|오 진짜 잘부르네ㅋㅋ 기분이다 담에 코노한번 같이가자")
                $ fbook_post_add("댓글|동삼용|오옹 나도나도 갈래")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|동삼용|2019년 3월 10일|문정과 19학번 대학생활 로망조지기~ 함께 마셔주는 친구들이 있어 행복하다~ #그리고 #당연하게 #존재하는 #뻔대님 #파이팅")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|유현재|아니ㅋㅋㅋㅋㅋ결국 저깄네ㅋㅋㅋㅋ 예상에서 벗어나질 않앜ㅋㅋ")
                $ fbook_post_add("댓글|해장중|내 말잌ㅋㅋ 이럴 거면 단톡에서 한숨 쉬지를 말던가ㅋㅋㅋ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 4 :
                $ fbook_post_add("본문|이동아|2019년 3월 12일|오랜만의 합주. 고향 친구와 함께 해서 재밌었다. 앞으로도 계속 같이 연습하제이~ #밴드 #죽마고우 #파이팅")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 6 :
                $ fbook_post_add("본문|해장중|2019년 3월 14일|<총엠 후기> *장문 주의, TMI주의 선배들과 친해질 수 있었던 총엠이었다~ 물론 머리가 너무 아프고, 죽은 뻔대 친구 챙기느라 조금 힘들긴 했지만(2호선 한바퀴 실화냐~)..그래도 많은 사람들과 친해져서 좋았다~ 문정과 1819학번 앞으로도 화이팅~ #새내기 #정든내기 #우린모두문정과 #위아더원")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|점심 해장 너무 좋았구요~")
                $ fbook_post_add("댓글|해장중|@김진일 ㄹㅇㅋㅋㅋㅋ개꿀맛~")
                $ fbook_post_add("댓글|오덕현|세 줄 요약 부탁한다는...")
                $ fbook_post_add("댓글|해장중|@오덕현 ㅂㄷㅂㄷ 그냥 읽어..")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 3 :
            if day == 0 :
                $ fbook_post_add("본문|동삼용|2019년 3월 15일|어제 총엠 존잼!!!!!!11122222 근데 어제 선배랑 손잡고 산책가던 사람 보기 좋더라~ㅋㅋㅋㅋㅋ #삼용패치 #속보 #나만믿으라구~")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|박대현|와 실화냐... 누구냐 빨리 자수하자~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 1 :
                $ fbook_post_add("본문|동삼용|2019년 3월 16일|동삼용님이 게시글을 공유하였습니다.심리학과 19학번 과잠 맞췄어요~~ 학교에서 한 장~~심리학과는 벌써 과잠 맞췄다 ㅠㅜㅠㅜ 문정과 친구들아 분발하자 ㅠㅜㅠㅜ @주인공 #뻔대야 #분발하자 #우리도 #과잠!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|우리도 과준위 만들었잖어 ㅋㅋㅋ 노력해서 빨리 맞추자")
                $ fbook_post_add("댓글|김진일|ㅇㅇㅇ 디자인 ㄱㄱㄱ")
                $ fbook_post_add("댓글|유현재|빠르게 가즈아~!")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|김진일|2019년 3월 17일|아~ 17학번 형 누나들 별거 아니네 ㅋㅋ 다들 술 왤케 못마시지... :P 총엠 후 술대전 2라운드 ㄱㄱ 하실분?")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|술은 역시 해장술이지 ㅎㅎ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|해장중|2019년 3월 18일|과잠 Coming Soon!!")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 4 :
                $ fbook_post_add("본문|안금지|2019년 3월 19일|우리 과잠 더 예뻤으면 좋겠다...")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 6 :
                $ fbook_post_add("본문|유현재|2019년 3월 21일|날씨가 아직 춥다... 하지만 마음은 따뜻따뜻 ~~~ <3 - 현재님은 지금 매우 행복해요")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|오덕현|우우 뭔가 불안한데...?")
                $ fbook_post_add("댓글|박대현|죽창각?")
                $ fbook_post_add("댓글|해장중|In-side Men 소환각?")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 4 :
            if day == 0 :
                $ fbook_post_add("본문|해장중|2019년 3월 22일|우리도 과잠 맞췄다!! 뻔대가 너무 고생했다. 뻔대야 미안해! 많이 못 도와줘서 미안해! #장미손 #복면협찬 #오덕현")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|동삼용|너도 과준위 하느라 고생했슈!")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|동삼용|2019년 3월 24일|과잠 얼른 입어보고 싶다~~ 기대된다~~ ㅎㅎ")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|과 잠 과 잠 과 잠")
                $ fbook_post_add("댓글|박대현|저 과잠무새진짜ㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|유현재|2019년 3월 25일|{color=#808080}유현재님이 노미래님과 {color=#ff0000}연애중{color=#808080}입니다.")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|미친ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ 뭐냨ㅋㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|박대현|와 대박.. 축하해 ㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|동삼용|나는 다 알고 있었지 ㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|김진일|실화냐........... @노미래")
                $ fbook_post_add("댓글|노미래|그렇게 됐어 ㅎ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 4 :
                $ fbook_post_add("본문|해장중|2019년 3월 26일|해장중님이 게시글을 공유했습니다.서울 근처 엠티가기 좋은 장소 TOP 5!!뻔대야 참고해라~ 물론 투표로 하겠지만 참고해~ ^^")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|동삼용|오오오오 좋아좋아")
                $ fbook_post_add("댓글|유현재|ㅋㅋㅋㅋㅋㅋ행동력 실화냐?")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 5 :
                $ fbook_post_add("본문|김진일|2019년 3월 27일|공략건다 얘들아. 나 뻔엠가서 소주 3병 못마시면 다 형 누나라고 불러드림")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|오케이 박제한다 딴말하면 애슐리 퀸즈 ㄱ")
                $ fbook_post_add("댓글|김진일|@해장중 ㅋㅋㅋㅋㅋㅋㅋ 어디서 제자녀석이 스승한테 덤비냐ㅋㅋ")
                $ fbook_post_add("댓글|해장중|@김진일 청출어람이란 말 못들어보셨습니까 스승님? 이 제자 뻔엠에서는 이겨드리겠습니다")
                $ fbook_post_add("댓글|동삼용|ㅋㅋㅋ 지켜봐야지~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

    elif month == 4 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("본문|박대현|2019년 4월 1일|박대현님은 자유로운 연애 중입니다")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|응~ 만우절")
                $ fbook_post_add("댓글|노미래|...대현아 내 친구라도 소개해줄까?")
                $ fbook_post_add("댓글|동삼용|>:O")
                $ fbook_post_add("댓글|유현재|대현아 그러고 싶니...?")
                $ fbook_post_add("댓글|박대현|...미안 얘들아 내가 잘못했어...")
                $ fbook_post_add("댓글|박대현|@노미래 그리고 해주면 고맙지 *^^*")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|동삼용|2019년 4월 3일|동삼용님이 게시물을 공유하였습니다.엠티때 하면 당신도 인싸! 친구들에게 사랑받는 술게임 TOP 5!!엠준위 님들 이거 참고 해서 프로그램 만들자 ㄱㄱㄱ @해장중 @김진일")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|오 좋은 정보 감사")
                $ fbook_post_add("댓글|김진일|감사")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|해장중|2019년 4월 4일|엠준위 뒤풀이~ 진짜 부르면 와서 같이 술마셔주는 이런 친구들이 있다는 게 너무 고맙다~ #문정과 #술이술술 #우리우정 #오래가자")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|누가 술자리에서 폰하냐?")
                $ fbook_post_add("댓글|동삼용|인정 22222 빨리 잔들자 장중아")
                $ fbook_post_add("댓글|박대현|와..저 친구들 장난아니네;;")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 5 :
                $ fbook_post_add("본문|김진일|2019년 4월 6일|여기가 어딘지 알 수 없네~")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|주인공|엌ㅋㅋㅋㅋ 야 너 어디냐 좌표 찍어봐")
                $ fbook_post_add("댓글|김진일|김진일 님이 위치정보를 공유했습니다")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|동삼용|2019년 4월 8일|어째서 내가...알콜 중독 위험군이냐..이거 뭔가 잘못된거 아닌가?알코올 중독 검사 이미지를 공유하였습니다.님들도 해보삼!!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|위험군 인정합니다...")
                $ fbook_post_add("댓글|김진일|?? 이거 너무 에반데?")
                $ fbook_post_add("댓글|동삼용|@해장중 @김진일 다들 어마어마한 점수를 받았구만..")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|해장중|2019년 4월 10일|DROP LUX MEA~!!!!! #드랍은 #나의 #빛 #빠드익선 #수행중")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|이 배신자 자식...")
                $ fbook_post_add("댓글|박대현|예에~ 드랍은 나의 빛~!!!")
                $ fbook_post_add("댓글|유현재|ㅎㅎ 난 미래랑 같이 들어서 드랍 안 할건데~")
                $ fbook_post_add("댓글|노미래|@유현재 ㅎㅎ 나도 ㅎㅎ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|김진일|2019년 4월 11일|스승 : 제자야 간맥의 뜻이 무엇인지 아느냐? 제자 : 간단히 맥주의 준말이 아닙니까? 스승 : 어허 제자야 그러니 너가 아직까지 이 스승을 이기지 못하는 것이니라. 제자 : 그럼 스승님 간맥의 뜻이 무엇입니까? 스승 : 당연히 간에 맥주를 들이 붓는다는 뜻 아니겠느냐. 자 어서 잔을 들고 이 500cc의 보리차를 원샷해보거라!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|박대현|그러니까 스승이 너고 제자가 장중이란 뜻이지?")
                $ fbook_post_add("댓글|오덕현|덜덜 코와이네~")
                $ fbook_post_add("댓글|유현재|진짜 도른자들... 술에 도른자들..")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 5 :
                $ fbook_post_add("본문|박대현|2019년 4월 13일|문정과 친구들과 불금 야식~ 치킨엔 소맥이지~ #낙대 #맛집 #글로벌하우스")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|유현재|예에이~~맛집맛집")
                $ fbook_post_add("댓글|해장중|최고다~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 3 :
            if day == 1 :
                $ fbook_post_add("본문|해장중|2019년 4월 16일|밴드하는 뻔대의 추천으로 보게 된 축제 게스트 소란! 엉엉 영배님 절 가져요 ㅠㅜ 노래 정말 잘하신다..전집 들어야지")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|유현재|진짜 노래 너무 잘부르셔 ㅠㅜㅠㅜ")
                $ fbook_post_add("댓글|노미래|가사도 너무 달달해 ㅎㅎㅎ")
                $ fbook_post_add("댓글|유현재|@노미래 너랑 나처럼??")
                $ fbook_post_add("댓글|노미래|@유현재 ㅎㅎㅎㅎ *^^*")
                $ fbook_post_add("댓글|해장중|@노미래 @유현재 둘 다 죽창에 찔리기 전에 사라져라..")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|김진일|2019년 4월 18일|벚꽃의 꽃 말은......중간 고사")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|악 악 으악")
                $ fbook_post_add("댓글|박대현|그..만.....")
                $ fbook_post_add("댓글|오덕현|다메다~!!")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 5 :
                $ fbook_post_add("본문|동삼용|2019년 4월 20일|시험 기간이라 금요일에도 못 노는거 너무 아쉽다 ㅠㅜㅠ 시험 끝나고 나랑 같이 놀러갈 사람 손!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|저요!")
                $ fbook_post_add("댓글|동삼용|@해장중 ...게시글 올린지 5초만에 반응하는 거 실화야?")
                $ fbook_post_add("댓글|해장중|ㅋㅋ..ㅈㅅ..ㅎㅎㅎ;;")
                $ fbook_post_add("댓글|김진일|나도~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 4 :
            if day == 0 :
                $ fbook_post_add("본문|해장중|2019년 4월 22일|ㄴr는 ㄱr끔 눈물을 흘린ㄷr..☆★ ㄴrl 감정을 control할 수 없는 ㄴrl ㅈr신ㅇl밉ㄷr..T.T ㅎrㅈl만 ㅇl또한 Gㄴrㄱr rira... 오늘 밤도 no sound로 cryingㅎrㄷr 잠들겠ㅈㅣ...")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|ㅋㅋㅋ 털림?")
                $ fbook_post_add("댓글|노미래|앜ㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|유현재|뭐함 ㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|동삼용|무슨말이야 이게?")
                $ fbook_post_add("댓글|해장중|아 ㅋㅋㅋㅋ 누구냐")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 1 :
                $ fbook_post_add("본문|동삼용|2019년 4월 23일|5월 3일 문정과 장터합니다~~~ 많이 와주세요!!!포스터 coming soon~")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|장중|문정과 좋아 랄랄라라~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|박대현|2019년 4월 24일|야식 드실분 선착순 3명 구함. 특별히 2만원은 내가 지원한다")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|동삼용|1빠")
                $ fbook_post_add("댓글|해장중|2빠")
                $ fbook_post_add("댓글|박대현|또 없으려나~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|김진일|2019년 4월 25일|Gray 새끼야 우리반장터한Die새키야딴 장터Monday새키야가지My새키야우리꺼나팔아Joy새키야술 막걸리 까러 와LIE새키야5월 3일 문정과 장터에 좀 먹으러와요 굽신굽신")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|뭐냐 ㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|유현재|ㅋㅋㅋㅋㅋㅋ 이거 좀 웃겼다")
                $ fbook_post_add("댓글|김진일|장난 아니지?")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 5 :
                $ fbook_post_add("본문|해장중|2019년 4월 27일|와~  문정과 장터한대~~~!메뉴도 다양하고 가격은 혜자!!!이런 역대급 장터는 처음이자 마지막이다!!!(가능하다면 여기에 사진 추가)")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|와 내가 가서 먹어도 되냐")
                $ fbook_post_add("댓글|노미래|돈만 내면 다 가능~")
                $ fbook_post_add("댓글|해장중|@동삼용 @유현재 @박대현 진일이가 5만원 쓴대 얘들아!!!")
                $ fbook_post_add("댓글|박대현|진일아 잘먹을게~")
                $ fbook_post_add("댓글|동삼용|개이득~~~")
                $ fbook_post_add("댓글|유현재|오 5만원 쓰면 일 안해도 ㅇㅈ")
                $ fbook_post_add("댓글|김진일|ㅡㅡ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

    elif month == 5 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("본문|유현재|2019년 5월 1일|문정과 장터까지 이제 이틀밖에 안남았다!!!놓치지 마세요 여러분~장소는 윌프리드 자하연 앞시간은 하루종일~ (하지만 역대급이라 재고가 빨리 소진될수도 있으니 얼른 오세요~)")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|노미래|ㅎㅎㅎㅎㅎㅎ 문정과 장터 흥해라~")
                $ fbook_post_add("댓글|김진일|ㅋ")
                $ fbook_post_add("댓글|해장중|ㅋㅋ")
                $ fbook_post_add("댓글|동삼용|ㅋㅋㅋ")
                $ fbook_post_add("댓글|박대현|ㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|유현재|그만해 이넘드라~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|동삼용|2019년 5월 4일|문정과 장터도 드디어 끝~~~!!!!함께 해주신 문정과 여러분 진짜 너무 수고했고 하면서도 너무 재밌었다어제 열심히 일한만큼 번 돈으로 재밌게 놀자~!!!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|우리 영원 우정히~")
                $ fbook_post_add("댓글|동삼용|그게 무슨말이야??")
                $ fbook_post_add("댓글|유현재|우리 우정 영원히~")
                $ fbook_post_add("댓글|김진일|비싼 술 ㄱㄱ~")
                $ fbook_post_add("댓글|박대현|진짜 수고했어 얘들아!!!!!! 문정과 최고~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|노미래|2019년 5월 8일|뭐했다고 벌써 일요일이냐 ㅠㅠㅠㅠㅠ뭐했다고 내일 월요일이냐 ㅠㅠㅠㅠㅠ")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|술 ㄱ?")
                $ fbook_post_add("댓글|노미래|아니 ㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|유현재|?")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 1 :
                $ fbook_post_add("본문|유현재|2019년 5월 9일|화요일 휴강 진심 dog꿀~~~  내일 놀러가실분~")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|동삼용|오 어디 갈거야??")
                $ fbook_post_add("댓글|유현재|모르겠다 ㅋㅋㅋ 근데 좀 학교 근처말고 나가서 놀려고")
                $ fbook_post_add("댓글|해장중|스리슬쩍 참여해볼까 합니다...")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|유현재|2019년 5월 10일|문정 19 한강 뻔모!!!휴강해주셔서 정말 감사합니다 교수님 ㅠㅠㅠㅠ하마터면 이렇게 좋은 날씨에 강의실에 있을뻔 했네한걸음에 달려와준 동기들 스릉흔드....!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|ㅋㅋㅋㅋ 한강 또 가자")
                $ fbook_post_add("댓글|노미래|다 같이 가니까 또 색다른 재미구만~ ㅎㅎㅎㅎ")
                $ fbook_post_add("댓글|유현재|다음엔 우리 둘만...? 히힛")
                $ fbook_post_add("댓글|김진일|으휴 꼴값을 떨어라 아주")
                $ fbook_post_add("댓글|해장중|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|박대현|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 5 :
                $ fbook_post_add("본문|동삼용|2019년 5월 13일|오늘부터 운동 특훈 들어간다...!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|김진일|무.조.건.이.긴.다!")
                $ fbook_post_add("댓글|유현재|무슨 운동??")
                $ fbook_post_add("댓글|동삼용|숨쉬기 운동 헤헷")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 6 :
                $ fbook_post_add("본문|박대현|2019년 5월 14일|학교에서 농구하실분~~~")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|너 농구도 하냐 ㅋㅋㅋ")
                $ fbook_post_add("댓글|박대현|ㅇㅇ ㅋㅋㅋㅋ 농구 개잼!!! ㄱㄱ?")
                $ fbook_post_add("댓글|해장중|ㅎ")
                $ fbook_post_add("댓글|동삼용|오! 어디서 해?? 나도 할래")
                $ fbook_post_add("댓글|박대현|과방에서 보자 ㅋㅋㅋ")
                $ fbook_post_add("댓글|김진일|농구가 뭔지 가르쳐주러 간다")
                $ fbook_post_add("댓글|박대현|ㅋㅋㅋㅋ 굿~")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 3 :
            if day == 1 :
                $ fbook_post_add("본문|김진일|2019년 5월 16일|다른 과 애들 운동회 때 복싱으로 부숴버린다!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|ㅋㅋㅋㅋ 진일이 못하는 싸움이 뭐임")
                $ fbook_post_add("댓글|동삼용|노래")
                $ fbook_post_add("댓글|박대현|운동회 때 복면가왕하자ㅋㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|유현재|ㄴㄴ 진일이 나오면 우리가 짐")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|동삼용|2019년 5월 17일|와... 몇 달 만에 집간다! 힐링하고 와야지")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 4 :
                $ fbook_post_add("본문|김진일|2019년 5월 19일|오랜만에 간지나는 우리 과잠 입고 한 컷 ㅋㅋㅋ#문정과과잠  #남자 #포스ㄷㄷ")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|유현재|잘입고 다니네 ㅋㅋㅋㅋ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 6 :
                $ fbook_post_add("본문|해장중|2019년 5월 21일|과 대항 운동회 뒷풀이 중 ㅋㅋㅋ운동하고 술 마시기 개꿀잼 ㅋㅋㅋㅋ옆에 술찌 뻔대 꼴아있음 ㅋㅋㅋㅋ")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 4 :
            if day == 0 :
                $ fbook_post_add("본문|해장중|2019년 5월 22일|어제 운동회 뒷풀이는 역대급이었다다양한 종목들로 다른 과와 경쟁하고, 뒷풀이에서 화합의 장까지!또 했으면 좋겠다 ㅋㅋㅋ뻔대 꼴아서 쓰러진 모습 사진 올릴까 고민하다 참음ㅋㅋㅋ다음엔 여명 마시고 오자 ㅋㅋㅋ")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 3 :
                $ fbook_post_add("본문|유현재|2019년 5월 25일|관악 최고 테니스 동아리 임팩트사람들하고 대회 끝나고 뒷풀이 중 ㅋㅋㅋ이번에 종합체육대회 우리가 종합우승!다음엔 나도 열심히 해서 A팀 멤버로 뛰어야지~")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 4 :
                $ fbook_post_add("본문|주인공|2019년 5월 26일|5월 6일, 저녁 7시 낙성대 사운드 마인드에서 공연합니다많이 와주세요!")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|유현재|가면 술 사주냐 ㅋㅋㅋ")
                $ fbook_post_add("댓글|노미래|뻔대 노래 잘했나? 나는 모르겠던데")
                $ fbook_post_add("댓글|박대현|그래서 지금부터 연습하는거야")
                $ fbook_count += 1

    elif month == 6 :
        if week == 1 :
            if day == 0 :
                $ fbook_post_add("본문|해장중|2019년 6월 1일|기말고사 앞두고급 뻔모 추진~소주 40병 실화냐 ㄷㄷㄷ;;문정과 19학번 정말 최고인듯기말 끝나고 또 달리자 ㅋㅋㅋ")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            if day == 1 :
                $ fbook_post_add("본문|유현재|2019년 6월 2일|시험기간이라 마음놓고 놀지는 못했지만너만 만나면 나는 마음이 편해져고마워♥100일, 200일, 300일 계속 행복하자-노미래님과 함께")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 2 :
                $ fbook_post_add("본문|주인공|2019년 6월 3일|6월 6일 금요일, 낙성대 사운드 마인드에서 공연합니다!저는 세 곡 부르는데, 많이 와서 즐겨주시고 응원도 해주시면 감사하겠습니다!!그때 뵙겠습니다!!!공연까지 퐈이야~~~~")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|동삼용|ㄱㄱㄱㄱㄱ")
                $ fbook_post_add("댓글|김진일|왜 하필 시험기간")
                $ fbook_post_add("댓글|해장중|욜....")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 2 :
            if day == 0 :
                $ fbook_post_add("본문|해장중|2019년 6월 8일|기말고사 공부 집중안되서 중도간다~~~ 같이 공부할사람 여기여기 모여라~  - @김진일님과 함께 있습니다")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|유현재|어지간히도 공부 되겠다 ㅋㅋㅋㅋㅋㅋ ㄱㄷ 좀있다 감")
                $ fbook_post_add("댓글|노미래|@유현재 뭐냐 ㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

            elif day == 4 :
                $ fbook_post_add("본문|김진일|2019년 6월 12일|누구인가? 지금 누가 종강소리를 내었어? 누가 종강소리를 내었는가 말이야!! /n 참으로 딱하구나! 저 자의 머릿속에는 마구니가 가득하다! 과제로 때려 죽여라.")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|해장중|엌ㅋㅋㅋㅋㅋㅋ 미친ㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|박대현|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ시험기간 드립 오지네ㅋㅌㅋㅋㅋ")
                $ fbook_post_add("댓글|유현재|ㄹㅇㅋㅋㅋㅋㅋㅋㅋ")
                $ fbook_post_add("댓글종료")
                $ fbook_post_add("그림자")
                $ fbook_count += 1

        elif week == 3 :
            if day == 0 :
                $ fbook_post_add("본문|해장중|2019년 6월 15일|다음 주 시험인데 공부 하나도 안했다 ㅋㅋㅋㅋㅋ 내일 금메달 각이다 ㅠㅠ")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|동삼용|나도 ㅋㅋㅋㅋㅋㅋ 시험 끝나고 중국 갈 생각밖에 없어 ㅋㅋㅋ")
                $ fbook_post_add("댓글|김진일|아... 진짜 노답이다")
                $ fbook_post_add("댓글|해장중|@진일 군대가자 싸나이면 해병대 ㄱㄱ")
                $ fbook_post_add("댓글종료")
                $ fbook_count += 1

            elif day == 5 :
                $ fbook_post_add("본문|주인공|2019년 6월 20일|드디어 시험 끝!!! 내일 종파 달린다 ㅋㅋㅋ @동삼용 @김진일 @해장중 가즈아~")
                $ fbook_post_add("댓글시작")
                $ fbook_post_add("댓글|동삼용|나는 늦참 ㅠㅠ")
                $ fbook_post_add("댓글|김진일|내일 의리주 하냐 ㅋㅋㅋㅋ")
                $ fbook_post_add("댓글|해장중|내일은 뻗어서 나한테 업히면 버리고 간다")
                $ fbook_post_add("댓글종료")
                $ fbook_count += 1
    return
