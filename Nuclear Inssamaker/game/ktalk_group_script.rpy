# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label change_group_talk :
    if month == 3 :
        if week == 1 :
            if day == 0 :
                $ grouptalk.add("날짜|2월 27일 금요일")
                $ grouptalk.add("주인공|문화정보학과 OO학번 단톡방입니다!!")
                $ grouptalk.add("장중|오올 뻔대! 술 그렇게 마시고도 일 잘하는데?")
                $ grouptalk.add("현재|캬 단톡방 빠르게 파는 클라스~~")
                $ grouptalk.add("진일|역시 내가 사람 보는 눈은 있지ㅋㅋㅋㅋ")
                $ grouptalk.add("금지|뻔대 뽑힌 거 축하해…!")
                $ grouptalk.add("덕현|후훗...역시 이 내가 인정한 [[리더]]...축하한다구 친구")
                $ grouptalk.add("미래|ㅊㅋㅊㅋ~")
                $ grouptalk.add("삼용|와 내가 다른 과 친구들한테 물어봤는데 신입생끼리만 있는 톡방은 우리과가 제일 빨리 파진것 같은데? 일 처리 속도 실화냐~")
                $ grouptalk.add("대현|뻔대 멋있다~ 열일하자! 뻔대님~~")
                $ grouptalk.add("주인공|와우 얘들아 고마워!!ㅠㅜ 너희가 뻔대로 뽑아준만큼 그 믿음에 최대한 보답할게!! 우리 앞으로 뻔모도 자주하고 동기들끼리도 많이 만나자아!!!!!")

            if day == 1 :
                $ grouptalk.add("날짜|3월 2일 월요일")
                $ grouptalk.add("주인공|와 다들 첫 등교 어땠어? 난 뭔가 쉬는시간이 안 정해져있는 것 자체가 되게 묘하더라")
                $ grouptalk.add("삼용|꿀잼꿀잼")
                $ grouptalk.add("대현|넌 외특인데 그런 말은 어디서 그렇게 배워오는거냐..")
                $ grouptalk.add("삼용|다른과 인싸 친구가 알려줬음! 꿀잼꿀잼~")
                $ grouptalk.add("현재|오 나 15학점 듣는데, 미래랑 15학점 겹강임 신기신기")
                $ grouptalk.add("미래|와 그래도 밥먹을 때 외롭진 않겠다! 수업마치고 밥 같이 먹자 ㅎㅎㅎ")
                $ grouptalk.add("주인공|오옹 뭐냐 둘이 그 정도면 운명인데?")
                $ grouptalk.add("진일|뭐 대학도 별 거 없던데?? ㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add("덕현|5252~ 수업 정도야 이 오레사마에게는 간단한 일이라굿 (퍽)")
                $ grouptalk.add("장중|개강 기념 술팟 구함 (1/34)")
                $ grouptalk.add("삼용|개강 기념 술팟2222")
                $ grouptalk.add("주인공|3333")
                $ grouptalk.add("금지|미안 나는 오늘 다른 일이 있어서 안 될 것 같아..")
                $ grouptalk.add("주인공|ㄱㅊㄱㅊ")

            elif day == 2 :
                $ grouptalk.add("날짜|3월 3일 화요일")
                $ grouptalk.add("장중|와 오늘 9시 수업인데 눈 떠보니 지금 시간임")
                $ grouptalk.add("연속|이게 말로만 듣던 자체 휴강이냐")
                $ grouptalk.add("연속|....으 머리야")
                $ grouptalk.add("진일|오늘 어차피 OT라 출첵 안했음 ㄱㅊㄱㅊ")
                $ grouptalk.add("장중|진일아 너 분명히 나랑 같이 첫 차까지 마셨는데 왜 이렇게 멀쩡하냐...")
                $ grouptalk.add("연속|으으 해장이나 하러가야지..")
                $ grouptalk.add("삼용|나는 오늘 공강이었지롱~ ㄱㅇㄷ~")
                $ grouptalk.add("주인공|와 공강 너무 부럽다. 난 왜 공강이 없냐...")
                $ grouptalk.add("현재|수강신청 망했대요~")
                $ grouptalk.add("미래|그렇대요~")
                $ grouptalk.add("대현|저 두 사람 겹강 많다고 죽 잘맞는거 봐라...")
                $ grouptalk.add("덕현|솔로는..서럽..달..까..?")

            elif day == 3 :
                $ grouptalk.add("날짜|3월 4일 수요일")
                $ grouptalk.add("삼용|내가 아는 다른 과 친구가 다음주 월요일에 동소제라는 걸 한대!")
                $ grouptalk.add("장중|오옹 동소제~ 동아리 소개제~")
                $ grouptalk.add("덕현|후훗, 풍문을 듣자하니 이 학교에는 <감상 클럽>이라는 게 있다고 하던데..")
                $ grouptalk.add("연속|얼마나 잘 운영되고 있는지 보고 싶다..랄까...(먼산)")
                $ grouptalk.add("대현|와 근데 삼용아 넌 진짜 그런 소식들 잘 알아온다. 멋진데?")
                $ grouptalk.add("삼용|하하 내가 이런 소식은 알아서 잘 들고오는 편이지")
                $ grouptalk.add("주인공|오오 동아리 재밌겠다. 너네는 하고 싶은거 없어?")
                $ grouptalk.add("진일|나는 운동 동아리...! 복싱 동아리 같은거 재밌을 것 같은데?")
                $ grouptalk.add("현재|그러는 뻔대야 너는 뭐할건데??")
                $ grouptalk.add("주인공|음...아직 정하진 않았는데")
                $ grouptalk.add("주인공|아마 나랑 같이 입학한 고향 친구랑 같은 동아리 들어갈 것 같은데?")
                $ grouptalk.add("미래|ㅇㅎ 많이 친한가봐")
                $ grouptalk.add("주인공|응 그래도 유치원부터 고등학교까지 같이 다니면서")
                $ grouptalk.add("주인공|중학교 때 부터는 밴드부도 같이 했으니까 많이 친하짘ㅋㅋㅋㅋ")
                $ grouptalk.add("주인공|걔랑 이 학교 같이 붙었을 때 진짜 좋았어")
                $ grouptalk.add("장중|와 그 정도면 ㄹㅇ로 소울메이트네 인정한다")

            elif day == 4 :
                $ grouptalk.add("날짜|3월 5일 목요일")
                $ grouptalk.add("장중|엌ㅋㅋㅋㅋㅋㅋㅋ나 어제 술 마시고 페북에 뭔 짓 한거짘ㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add("대현|너 500 마시다가 맥주는 음료수지!")
                $ grouptalk.add("연속|이러면서 소주 시킬 때부터 뭔가 쎄하더라")
                $ grouptalk.add("진일|장중아 너는 아직 나랑 술 마시기엔 너무 약해. 더 강해져서 와라")
                $ grouptalk.add("장중|받들어 모시겠습니다. 스승님")
                $ grouptalk.add("덕현|지나친 음주는 간을 파.괘.한다네...쿡쿡쿡")
                $ grouptalk.add("연속|너희의 <해독 기관>이 과연 언제까지 버틸 수 있을까..? 후하하하")
                $ grouptalk.add("주인공|맞아 얘들아 조금은 적당히 마셔..그러다 몸 상할라 ㅠㅜ")
                $ grouptalk.add("현재|술자리 있을 때마다 병샷하는 네가 할 말은 아니지 않아?")
                $ grouptalk.add("미래|동의")
                $ grouptalk.add("삼용|동의222222")
                $ grouptalk.add("대현|동의3333333333")
                $ grouptalk.add("주인공|엌ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

            elif day == 5 :
                $ grouptalk.add("날짜|3월 6일 금요일")
                $ grouptalk.add("주인공|맞다 너희들 다음 주 총엠인 건 알지?")
                $ grouptalk.add("삼용|와 총엠~ 재밌겠다~!~!")
                $ grouptalk.add("장중|총엠이면 고~학번 선배님들이 맛있는 양주 사오겠지??")
                $ grouptalk.add("연속|무조건 그 때까지 버틴다...")
                $ grouptalk.add("진일|양주하면 또 나지, 너희 발렌타인 30년산이라고 들어봤냐?")
                $ grouptalk.add("금지|아..엠티는 별로..재미 없을 것 같은데..")
                $ grouptalk.add("덕현|엠티! 그 사건이 바로 다음주란 말인가..")
                $ grouptalk.add("연속|큭..어쩔 수 없지 이 날을 위해 단련한 궁극의 술 게임을..!")
                $ grouptalk.add("연속|바로..지금!!")
                $ grouptalk.add("현재|으음 많이 마실 것 같은데 숙취해소제라도 챙겨놔야겠다..")
                $ grouptalk.add("미래|오옹 좋은 생각이야!")
                $ grouptalk.add("대현|와 첫 엠티..재밌겠지? ㅎㅎㅎ")

            elif day == 6 :
                $ grouptalk.add("날짜|3월 7일 토요일")
                $ grouptalk.add("주인공|입학 후 첫 주말인데 다들 뭐하고 지냈어?")
                $ grouptalk.add("장중|어제 달리고 이제 일어남 ㅎㅎㅎ...")
                $ grouptalk.add("연속|으 속 안좋아 해장하러 가야겠다.")
                $ grouptalk.add("삼용|간단하게 서울 이곳저곳 돌아 다녔어")
                $ grouptalk.add("연속|다른 학교 주변 돌아다녔는데, 그 학교에 있는 아는 애들이 선배들한테 들은 맛집 같은 거 추천해주더라")
                $ grouptalk.add("연속|혹시 다른 학교 갈 일 있으면 물어보면 대답해줄게!")
                $ grouptalk.add("현재|오옹..나 내일 낙성대학교 쪽 놀러갈 것 같은데 주변 맛집 알려주실?")
                $ grouptalk.add("삼용|갠톡 ㄱㄱ")
                $ grouptalk.add("현재|오키~")
                $ grouptalk.add("진일|난 그냥 아는 형님들 만나고 왔지 ㅎㅎ")
                $ grouptalk.add("연속|나중에 힘 쓸일 있으면 말해 다 도와준다 ㅎㅎ")
                $ grouptalk.add("금지|그래;;")
                $ grouptalk.add("덕현|와타시는...밀린 <명작>들을 봤달..까..?")
                $ grouptalk.add("주인공|ㅋㅋㅋㅋ다들 그래도 좋은 주말 보낸 것 같아서 다행이네!")

        elif week == 2 :
            if day == 0 :
                $ grouptalk.add("날짜|3월 8일 일요일")
                $ grouptalk.add("삼용|야~ 현재야 너 어제 낙성대주변 맛집 물어본 게 이것 때문이었냐~ 와~")
                $ grouptalk.add("현재|??? 뭐가?????")
                $ grouptalk.add("삼용|에이 다 알면서~")
                $ grouptalk.add("연속|너 미래랑 내가 알려준 맛집에서 둘이서 오붓하게 밥 먹는거 봤는데?")
                $ grouptalk.add("대현|@노미래")
                $ grouptalk.add("장중|@노미래22")
                $ grouptalk.add("미래|아 너희들이 생각하는 그런거 아니야 ㅠㅜㅜ")
                $ grouptalk.add("현재|ㅇㅇ 그런 거 아니고, 그냥 저번 주에 나 수업 못 갔을 때")
                $ grouptalk.add("연속|수업 내용 알려주고 그래서 그 보답으로 밥 산 것 뿐이야")
                $ grouptalk.add("진일|과연 그럴까? ㅎㅎㅎㅎ")
                $ grouptalk.add("주인공|너희 설마...Hoxy..?")
                $ grouptalk.add("장중|해 명 해 해 명 해")
                $ grouptalk.add("미래|아니야;;")
                $ grouptalk.add("현재|아니야;;")
                $ grouptalk.add("장중|와;; 땀 개수까지 똑같은 것 보소...저 정도면 천생연분이다..")
                $ grouptalk.add("덕현|큿...이래서 인싸들이란..")

            elif day == 1 :
                $ grouptalk.add("날짜|3월 9일 월요일")
                $ grouptalk.add("장중|와 나 동소제 놀러갔다가 우리 뻔대 노래하는 거 들었는데 장난아니던데;;")
                $ grouptalk.add("현재|오~ 그렇게 잘해?")
                $ grouptalk.add("장중|ㄹㅇ 음원 튼 줄, 블루투스 스피커 없나 찾아봤다니까?")
                $ grouptalk.add("주인공|에이 과찬이야...ㅎㅎㅎㅎ")
                $ grouptalk.add("삼용|과찬은 무슨 나도 같이 들었는데 진짜 잘 부르더라~")
                $ grouptalk.add("대현|ㅇㅈㅇㅈ, 옆에서 기타 치던 친구가 전에 말한 고등학교 동창이지?")
                $ grouptalk.add("연속|걔도 엄청 잘 치더라, 둘이 케미  진짜 잘 맞던데? ㅋㅋㅋㅋ")
                $ grouptalk.add("주인공|그 친구가 실력 하나는 끝내주지!")
                $ grouptalk.add("덕현|그래서 그 밴-드-부에는 가입하기로 결정한 걸까나..?")
                $ grouptalk.add("주인공|응, 동아도 맘에 들어하고, 선배들도 다들 괜찮아보여서 바로 가입 신청했어.")
                $ grouptalk.add("미래|오옹 밴드라니 다음에 공연 같은 거 하면 꼭 보러갈게!!")
                $ grouptalk.add("연속|애들 반응 보니까 기대되는데~")
                $ grouptalk.add("주인공|ㅋㅋㅋㅋㅋ 홍보 오지게 할 거니까 많이 오렴 ^^")

            elif day == 2 :
                $ grouptalk.add("삼용|테스트")

            elif day == 3 :
                $ grouptalk.add("장중|테스트")

            elif day == 4 :
                $ grouptalk.add("장중|테스트")

            elif day == 5 :
                $ grouptalk.add("장중|테스트")

            elif day == 6 :
                $ grouptalk.add("장중|테스트")

        elif week == 3 :
            if day == 0 :
                $ grouptalk.add ("현재|아 총엠에서 마신 술 아직도 안깬듯 ㅠㅠ")
                $ grouptalk.add ("미래|그러게 조절하며 마시지 현재야아아아~~~ ㅠㅠㅠ")
                $ grouptalk.add ("금지|얘들아 나 벌써 과제 나왔어…")
                $ grouptalk.add ("삼용|맞아… 근데 총엠에서 선배들 과잠 조녜드라!")
                $ grouptalk.add ("대현|헐 나도 그 생각!!! 우리도 얼른 맞췄으면 좋겠다!!! 과잠 가즈아~")
                $ grouptalk.add ("장중|야 우리는 과잠 안맞추냐 뻔대야")
                $ grouptalk.add ("진일|일해라 노예야 ㅋㅋ")
                $ grouptalk.add ("주인공|와 진짜 총엠 다녀오자마자 부려먹는다고? 하… 도비는 일해야지")

            elif day == 1 :
                $ grouptalk.add ("장중|우리 그래서 과잠은 언제 맞추나여ㅕㅕㅕㅕㅕ")
                $ grouptalk.add ("진일|과잠준비위원회라는 걸 따로 만드는게 좋지 않을까?")
                $ grouptalk.add ("대현|오! 그게 좋을듯")
                $ grouptalk.add ("미래|응응 그래야 뭐라도 진행될것 같아 ㅠㅠ")
                $ grouptalk.add ("삼용|와 심리학과는 벌써 과잠 맞췄다는데??? 이거 봐봐 진짜 잘 맞췄다 ㅠㅠㅠ")
                $ grouptalk.add ("현재|와 진짜 예쁘다… 우리도 그럼 얼른 과준위 만들자. 일단 그럼 XX랑 나 할래 ㅋㅋㅋ 또 하고싶은 분?")
                $ grouptalk.add ("삼용|나나나나나나나나")
                $ grouptalk.add ("진일|과잠 디자인이면 또 내가 나설 차례가 왔군")
                $ grouptalk.add ("장중|오케이~ XX야 너가 톡방 파")

            elif day == 2 :
                $ grouptalk.add ("대현|연대 경영이랑 미팅할 남자분 빠르게 2분 모십니다")
                $ grouptalk.add ("장중|오오…. 자리 있음?")
                $ grouptalk.add ("대현|알콜 중독자 불가능")
                $ grouptalk.add ("삼용|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("주인공|나는 가능?")
                $ grouptalk.add ("대현|뻔대는 노예라서 불가능")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("주인공|와 진짜 너무하닼ㅋㅋㅋㅋㅋㅋ")

            elif day == 3 :
                $ grouptalk.add ("주인공|애들아, 우리가 진짜 개멋있는 과잠 만들듯 ㅋㅋㅋ")
                $ grouptalk.add ("금지|와 진짜 기대된다! 빨리 사고 싶다 ㅋㅋㅋ")
                $ grouptalk.add ("대현|오오 예시 나옴?? 뭐있어 ㅋㅋㅋ")
                $ grouptalk.add ("진일|야 내가 미는게 제일 멋있다 그걸로 하자 ㅋㅋㅋ")
                $ grouptalk.add ("현재|개궁금하다 ㅋㅋㅋ")
                $ grouptalk.add ("주인공|기대해라 ㅋㅋㅋㅋ")

            elif day == 4 :
                $ grouptalk.add ("주인공|우리가 과잠 후보 3개 만들었는데, 올릴게 애들아")
                $ grouptalk.add ("대현|와 대박 진짜 빨리 올려줘 ㅋㅋㅋ")
                $ grouptalk.add ("주인공|이미지 1(), 이미지 2(), 이미지 3()")
                $ grouptalk.add ("장중|아무리 봐도 내게 제일 예쁘다 ㅋㅋㅋ 3번 투표해라 애들아")
                $ grouptalk.add ("진일|멋하면 카모 아니냐 ㅋㅋㅋ 야상과잠 존멋이다 2번 투표해줘 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|누가봐도 1번이 제일 예쁘다 ㅋㅋㅋ")
                $ grouptalk.add ("금지|어, 생각보다 별론데….?나 안사고 싶은데ㅠㅠ")
                $ grouptalk.add ("주인공|애들아 최대한 빨리 투표 해주라!")
                $ grouptalk.add ("미래|ㅇㅋㅇㅋ")
                $ grouptalk.add ("SYSTEM|투표 결과 1안 | 8 /  2안 | 6 / 3안 | 4")
                $ grouptalk.add ("SYSTEM|투표를 더 진행하시겠습니까? 투표 / 선택하기")
                $ grouptalk.add ("SYSTEM|어떤 과잠을 선택하시겠습니까?")

            elif day == 5 :
                # (강제 선택한 경우)
                $ grouptalk.add ("금지|ㅠㅠ 나는 안 살래… 돈이 너무 없어 ㅠ")
                $ grouptalk.add ("현재|음…. 그래도 고생했어 과준위 ㅎㅎㅎ")
                $ grouptalk.add ("미래|맞아맞아 ㅠㅠㅠ")
                $ grouptalk.add ("진일|야 진짜 어떻게 이러지 ㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("대현|에이....금지야ㅠㅠ 그래도 ㅠㅠ 첫 과잠인데 사자")
                # (투표 연장한 경우)
                $ grouptalk.add ("주인공|애들아 그래도 최대한 민주적으로 가려고 의견 수렴하니까 투표 빨리 해줘 ㅠㅠ 부탁할게!")
                $ grouptalk.add ("진일|빨리빨리 하자.")
                $ grouptalk.add ("장중|과잠위 고생했으니까 빨리 해주세요!!")
                $ grouptalk.add ("삼용|하오하오!")
                $ grouptalk.add ("미래|ㅋㅋㅋㅋ 근데 현재야 너 저거 잘 어울리겠는데?")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("대현|아 진짜 나가서 연애질해라 ㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|근데 대현이 모쏠 실화냐??ㅋㅋㅋㅋ")
                $ grouptalk.add ("대현|야 아니야 ㅋㅋㅋㅋ 나 연애해봤어 ㅋㅋㅋㅋ 어이가 없다")
                $ grouptalk.add ("진일|ㅋㅋㅋㅋㅋ 니들이 사랑을 아냐? ")
                $ grouptalk.add ("장중|와 진일이 갬성 빼앰~~~ ")
                $ grouptalk.add ("SYSTEM | 투표 결과 1안 | 11 /  2안 | 8 / 3안 | 5")
                $ grouptalk.add ("SYSTEM | 투표를 연장하시겠습니까? Y/ N ")

            elif day == 6 :
                # 강제 종료
                $ grouptalk.add ("장중|술~ 이 한잔 생각 나~는 밤")
                $ grouptalk.add ("현재|마치~ 있는 것 같아요~")
                $ grouptalk.add ("대현|그~ 좋았던 시~절들")
                $ grouptalk.add ("미래|이젠 모~두 한숨만 되네요~")
                $ grouptalk.add ("진일|??? 다들 갑자기 왜이래… 장중이 술 땡기면 ㄱㄱ?")
                $ grouptalk.add ("장중|이거 노래임 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|오 이거 무슨 노래야???")
                $ grouptalk.add ("주인공|임창정의 소주한잔!!!")

                # 투표 할 시에
                $ grouptalk.add ("주인공|근데 님들아 투표좀~~~~")
                $ grouptalk.add ("삼용|투표 가즈아~!!!!")
                $ grouptalk.add ("진일|아직도 B가 안될거라고 생각하는 흑두루미들 없재?")
                $ grouptalk.add ("대현|자하연 물 온도 몇도냐 ㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋ")

        elif week == 4 :
            if day == 0 :
            # 투표 진행시
                $ grouptalk.add ("진일|역시 내게 제일 멋있네, b안이 제일 높네")
                $ grouptalk.add ("장중|투표 실화냐….")
                $ grouptalk.add ("현재|저걸 어떻게 입냐 ㅠㅠ")
                $ grouptalk.add ("삼용|애들아 a안 밀면 b안 이길 수 있어, 영차영차 외치자!, 영")
                $ grouptalk.add ("대현|차")
                $ grouptalk.add ("대현|영")
                $ grouptalk.add ("장중|차")
                $ grouptalk.add ("진일|영차한다고 되겠다 ㅉㅉ")
                $ grouptalk.add ("주인공|에이 진일아~")
            # 투표 강제 종료시
                $ grouptalk.add ("대현|우리 과잠은 언제 나오지??")
                $ grouptalk.add ("주인공|아마 곧 나올 것 같은데 ㅋㅋㅋ 우리 과잠 진짜 예쁜 것 같아!")
                $ grouptalk.add ("금지|아닌 것 같은데….ㅠ")
                $ grouptalk.add ("진일|에이 입어보면 다르다 진짜 ㅋㅋㅋ")
                $ grouptalk.add ("미래|그래 ㅋㅋㅋ 예뻐도 안 예뻐도 우리가 같이 입는게 의미가 있지")
                $ grouptalk.add ("현재|역시 미래다 ㅋㅋㅋㅋ")
                $ grouptalk.add ("장중|으~ 진짜 너네 적당히해라")
                $ grouptalk.add ("현재|싫은데 싫은데???ㅋㅋㅋㅋ")

            elif day == 1 :
            # 투표 종료시
                $ grouptalk.add ("주인공|애들아 우리 이제 우리끼리도 밥약하자 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|오 또 뻔대가 일한다 ㅋㅋㅋㅋ 나 완전 좋아 ㅋㅋㅋ 나는 이번주 월,화, 수, 목 12시 반 가능해")
                $ grouptalk.add ("장중|나도나도 ㅋㅋㅋㅋ 근데 나는 화, 수만 학교 와서 ㅋㅋㅋ 그때만 될 것 같아")
                $ grouptalk.add ("진일|와 장중이 주2 실화야??? 수요일 저녁에 출국하면 4박 5일로 여행가겠다 ㅋㅋㅋ")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋ 미래랑 나도 갈까? 갈 수 있을 것 같아")
                $ grouptalk.add ("대현|수 ㄱㄱㄱㄱ, 장중이 엄마한테 18학점이라고 하고, 절반 등록금깡한거 아니야?")
                $ grouptalk.add ("장중|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")

            # 투표 지속시
                $ grouptalk.add ("진일|애들아 곧 24일에 투표 마감인데 투표 아직 안한 사람은 해줘!")
                $ grouptalk.add ("주인공|지금까지 투표 안하면 뻔대가 곤란하다는게 학계의 정설")
                $ grouptalk.add ("장중|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("삼용|과준위가 힘빠진다는 것도 유력한 가설")
                $ grouptalk.add ("대현|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("현재|ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|빨리 해주자 애들아 ㅋㅋㅋㅋ")
                $ grouptalk.add ("주인공|저녁까지 안해주시면 갠톡들어갑니다~")


            elif day == 2 :
            #   투표 마감시
                $ grouptalk.add ("현재|우리 과잠은 언제오지 ㅋㅋㅋ 빨리 입고 싶은데")
                $ grouptalk.add ("진일|ㅋㅋㅋ 진짜 간지다 누가 봐도 눈에 띌듯 ㅋㅋㅋㅋ")
                $ grouptalk.add ("금지|그게 문제지….ㅠㅠ")
                $ grouptalk.add ("주인공|에이 아직 안 입어봤는데 그러지 말자 ㅋㅋㅋㅋ")
                $ grouptalk.add ("장중|우리 내일 점모 맞지?")
                $ grouptalk.add ("대현|뭐 먹지?? 중국음식?")
                $ grouptalk.add ("삼용|헐… 개좋아")
                $ grouptalk.add ("주인공|ㅋㅋㅋㅋ 삼용이 배려로 내일은 중식먹자!")
                $ grouptalk.add ("현재|좋아!!")

            # 투표 지속시
                $ grouptalk.add ("주인공|오늘이 투표 마지막 날입니다! 예쁜 과잠을 선택해주세요~")
                $ grouptalk.add ("장중|진짜 과준위 4일동안 회의하고 정한 과잠입니다ㅠ 여러분 투표 부탁드려요!")
                $ grouptalk.add ("진일|그래 애들아 투표 좀 해라")
                $ grouptalk.add ("삼용|지금 투표하면 내가 원하는 걸로 할 수 있어 애들아!!!")
                $ grouptalk.add ("금지|음…..")
                $ grouptalk.add ("대현|나는 했어 과준위 ㅠㅠ 너무 고생한다 애들아 투표하자!!")
                $ grouptalk.add ("주인공| 고마워 다들 ㅋㅋㅋㅋ 다들 후보들이 너무 예뻐서 고민하는거지 뭐 ㅋㅋㅋ 내가 봐도 어렵다 ㅋㅋㅋ 여튼 저녁까지는 투표 마감할게요! ")


            elif day == 3 :
                $ grouptalk.add ("장중|이제 과잠바는 해결됬겠다 뻔엠 ㄱㄱ?")
                $ grouptalk.add ("현재|헐 맞다 우리 뻔엠도 가야되지??")
                $ grouptalk.add ("장중|ㅋㅋㅋㅋ 다들 까먹고 있었나 보네")
                $ grouptalk.add ("진일|에이~ 우리끼리 술마시는 행사인데 어떻게 까먹어 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|와 우리 뻔엠도 가?? 과잠 맞추자마자 뻔엠 계획도 세우고 이번학기 개잼!!!")
                $ grouptalk.add ("대현|가즈아~~!")
                $ grouptalk.add ("미래| 행사가 끊임없닼ㅋㅋㅋㅋ 넘좋아!")

            elif day == 4 :
                $ grouptalk.add ("주인공|그럼 우리 내일 뻔엠 날짜 정할래??")
                $ grouptalk.add ("장중|말 나온김에 지금 어때?!!!")
                $ grouptalk.add ("미래|현재가 오늘 바빠서 카톡을 못볼 것 같아서...ㅠㅠ 오늘 말해놓고 내일 정하는게 좋을 것 같아 ")
                $ grouptalk.add ("장중|아 ㅇㅋㅇㅋ")
                $ grouptalk.add ("삼용|ㅇㅋㅇㅋ가 무슨 뜻이야??")
                $ grouptalk.add ("진일|아 맞다 얘 중국에서 왔지 ㅋㅋㅋㅋㅋㅋ")
                $ grouptalk.add ("미래|ㅋㅋㅋㅋ ㅇㅋㅇㅋ  = 오키오키! 알았다는 말이야 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|아하!")
                $ grouptalk.add ("대현|앞으로도 모르는 말 있으면 물어봐 삼용쓰 ㅋㅋㅋ")
                $ grouptalk.add ("삼용|ㅇㅋㅇㅋ")
                $ grouptalk.add ("주인공|얘들아 뻔엠 날짜 내일 정하는 걸로 한다??")
                $ grouptalk.add ("삼용|ㅇㅋㅇㅋ")
                $ grouptalk.add ("대현|굿굿")


            elif day == 5 :
                $ grouptalk.add ("주인공|얘들아 우리 뻔엠 언제 갈래?!!!!")
                $ grouptalk.add ("장중|뻔엠!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                $ grouptalk.add ("대현|다들 언제가 좋아??")
                $ grouptalk.add ("현재|주중에는 수업이 있으니까 금,토 아니면 토,일??")
                $ grouptalk.add ("미래|져아져아~")
                $ grouptalk.add ("삼용|나도 좋아!!")
                $ grouptalk.add ("주인공|중간고사 전에 가는게 좋으니까 다음주 금,토로 정하는게 어때??")
                $ grouptalk.add ("진일|콜")
                $ grouptalk.add ("삼용|콜")
                $ grouptalk.add ("장중|콜")
                $ grouptalk.add ("대현|쿨")
                $ grouptalk.add ("현재|꿀")
                $ grouptalk.add ("미래|꿀꿀")
                $ grouptalk.add ("진일|그만해라~")

            elif day == 6 :
                $ grouptalk.add ("삼용|우리 근데 뻔엠 전에는 과잠 오겠지??")
                $ grouptalk.add ("장중|으아아아아 과잠 기대된다!!!")
                $ grouptalk.add ("진일|ㅋㅋㅋ 좀 기다려 이 과잠무새들아 어떻게든 되겠지")
                $ grouptalk.add ("금지|난 과잠 주문 안했는데 ㅎㅎ")
                $ grouptalk.add ("미래|응??? 왜 주문 안했어 ㅠㅠㅠㅠ")
                $ grouptalk.add ("금지|그냥 그렇게 됐어 ㅋㅋㅋ")
                $ grouptalk.add ("미래|지금이라도 주문해 ㅠㅠㅠ")
                $ grouptalk.add ("금지|그럴까??")
                $ grouptalk.add ("대현|?")
                $ grouptalk.add ("삼용|이미 주문 들어가서 그건 안될것 같아…")
                $ grouptalk.add ("현재|ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ 까비…")
