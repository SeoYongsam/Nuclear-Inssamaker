#이미지 선언
image big_room = "fun_mt/big_room.jpg"
image gogi_f = "fun_mt/gogi_f.png"
image gogi_s = "fun_mt/gogi_s.jpg"
image gwa = "fun_mt/gwa.jpg"
image gwa_3 = "fun_mt/gwa_3.jpg"
image jangbal_f = "fun_mt/jangbal_f.jpg"
image jangbal_little = "fun_mt/jangbal_little.jpg"
image jangbal_one = "fun_mt/jangbal_one.jpg"
image jangbal_rest = "fun_mt/jangbal_rest.jpg"
image jangbal_s = "fun_mt/jangbal_s.jpg"
image naksung = "fun_mt/naksung.jpg"
image ramyen = "fun_mt/ramyen.jpg"
image small_room = "fun_mt/small_room.jpg"
image subway = "fun_mt/subway.jpg"

# 4월 6일, 7일 금,토 뻔엠
# month4 week 1 day 5
label fun_mt:
    scene black
    "오늘은 드디어 고대하던 뻔엠날이다."
    "우리들끼리 가는 엠티는 처음인만큼, 설렘 반 떨림 반의 마음을 가지고 엠티를 가기 위해 자취방을 나섰다."

    #4/2부터 시작한 장발/후발 투표를 4/3전에 끝낼 경우 1, 그 이후에 끝낼 경우 2의 스크립트
    #1. 장발 투표를 4/3까지 끝냈을 시(4월 2일, 4월 3일에 종료할 경우)
    if fun_mt_vote_day < 32 :
        show jangbal_s at truecenter

        Jangjung "오 뻔대 왔냐? 조금 늦었네?"
        Player "앗..미안미안 내가 조금 늦었네"
        Samyong "뻔대가 이렇게 늦어서 쓰냐... 장발하는 애들 거의 미리 와서 기다리고 있었는데"
        Jinil "그러니까 말이야 벌로 오늘 넌 가자마자 병샷이다."
        Player "으악 그것만은 참아줘..하하하하"
        Ohduck "오이오이~ 동아리 일정까지 미루고 온 와타시도 있다고~"
        Hyunjae "그러니까 말이야 그래도 뻔대 왔으니까 다 도착한 거 맞지?"
        Mirae "그런거 같아~ 그럼 슬슬 출발할까??"
        Player "오키오키~ 출발하자!!"

        #과 파라미터 + / 멘탈 +
        "투표를 적당히 마감해서인지, 장발대에 친구들이 많이 왔다."
        "과 분위기도 좋아진 것 같고 내 마음도 훈훈하다."
        $ gwa_parameter += 3
        $ mental_point += 20
        call parameter_maxmin_check

    #2. 장발 투표를 4/4 이후로 끝냈을 시(4월 4일, 4월 5일에 종료 하였을 경우)
    else :
        show jangbal_f at truecenter
        Player "엥? 나밖에 안 온건가…애들은..?"

        "휴대폰을 꺼내서 확인해보니 장발대 중 1명은 급한일이 생겨서 후발대로 바꾼다는 연락이 와있었다…"

        Player "하...애들 진짜..그래도 첫 뻔엠인데.."
        Samyong "엇 미안 조금 늦었네.."
        Jangjung "죄송 죄송~ 차가 조금 막혀서"
        Jinil "응? 근데 너 밖에 없냐? 다른 애들은??"
        Player "방금 전에 한 명 또 연락 와서 후발대로 바꾼대"
        Jangjung "엑? 진짜? 와 애들 진짜 너무하네…"
        Player "어쩔 수 없지 뭐…그래도 아 저기 남은 애들 온다. \n이 쯤이면 다 모인 것 같으니까 슬슬 출발할까?"
        Jinil "뭐 그래 어쩔 수 없지. 이렇게 된 거 안주 같은거 우리가 먹고 싶은걸로 다 사자!"
        Samyong "나는 통큰팝콘~"

        #과 파라미터 - / 멘탈 -
        "투표를 너무 늦게 마감해서인지, 애들이 전부 후발대로 탈주했다."
        "과 분위기가 이렇게 흉흉했다니... 내 멘탈이 터졌다."
        $ gwa_parameter -= 3
        $ mental_point -= 20
        call parameter_maxmin_check

    #show naksung at truecenter
    #"친구들과 지하철을 타고 엠티 장소와 가까운 마트에 도착해서 장을 보기로 했다."
    #"예산에 맞게 저녁으로 먹을 음식, 안주와 술 등을 사던 도중 낙성대학교 학생들이 과잠을 입고 장을 보고 있는 모습을 보게되었다."

    #과잠 투표에 따라 달라지는 스크립트. 3의 경우 과잠 투표를 3/21까지 마감했을 경우. (3/19-3/21)
    #4의 경우 과잠 투표를 3/22이후로 마감했을 경우. (3/22-3/24)
    #헷갈리지 않게 3,4로 표현했을뿐, 뻔엠 투표와는 관계 없는 스크립트
    #3. (과잠 히든을 달성해 과잠을 받은 경우) (3/19에 시작한 과잠 투표를 3/21전에 마감했을 경우 아래의 스크립트)
    #Jangjung "와 쟤들 과잠 봐봐"
    #Samyong "우리 거보다 디자인 별론거 같은데 안그래?"
    #Player "내 생각도 그런듯!! 우리 그래도 과잠 잘 맞췄다 그치?"
    #Jinil "그럼! 누가 아이디어 냈는데!"
    #Jangjung "하 그래도 일찍 도착해서 다행이다. 어제 안왔으면 못입고 왔을 뻔.."
    #Samyong "진짜 아슬아슬하게 도착했다니까"
    #Player "그래도 도착한 게 어디냐! 뻔엠 때 딱 입고 가는 거 너무 좋구요~"

    #4. (과잠 히든을 달성하지 못한 경우) (21일 이후에 과잠 투표를 마감할 경우 아래의 스크립트)
    #Samyong "와...쟤네 과잠 예쁜 것 같다.."
    #Jangjung "야 우리 과잠 디자인이 더 괜찮거든?"
    #Jinil "그럼 뭐하냐 오지도 않았는데"
    #Jangjung "하 그니까….너무 늦게 시켜서 그런가.."
    #Player "아... 우울하다...얘들아 미안…"
    #Samyong "에이 뻔대가 미안할 건 아니지, 지금 딱 과잠 주문 폭주할 시기라고 들었었기도 했고"
    #Jinil "맞음 애들이 투표에 참가 잘 안 한게 잘못이지 넌 총대 메고 독려한 거 밖에 더 있냐."
    #Jangjung "그래 맞아 아쉽지만 뭐 어쩔 수 없지"

    #"말은 그렇게 하지만 친구들이 아쉬움이 넘치는 눈으로 \n과잠을 입은 낙성대 학생들을 아련히 바라보는 것이 느껴진다…"
    #과 파라미터 -
    #$ gwa_parameter -= 10
    #call parameter_maxmin_check

    "장발대와 힘을 합쳐 장을 본 뒤, 엠티 장소로 이동했다."

    $ day_or_evening = "evening"

    #(장발대가 적을 경우 => 4/4 이후로 투표를 끝냈을 경우 추가 스크립트) (앞의 장발, 후발에서 2번경우)
    if fun_mt_vote_day >= 32 :
        show jangbal_little at truecenter
        "비록 장발대는 적었지만, 각자 원하는 것을 사다보니 짐이 많아졌다."
        "많은 짐을 적은 수의 장발대가 옮기느라 생각보다 많은 힘을 소모했다."
        #체력 파라미터 -
        $ hp -= 40
        call parameter_maxmin_check

    #(여기서부터는 공통 스크립트)
    show big_room at truecenter
    Jangjung "으아아~ 도착했다~!"
    Samyong "하 짐 옮기느라 힘들었어.."
    Jinil "내 말이...그래도 고생했다."

    show jangbal_one at truecenter
    "조금 쉬다가 밖을 보니 진일, 장중이와 몇몇 친구들이 족구를 하고 있었다."

    scene black
    "몇 시간 뒤, 후발대 친구들이 도착했고 다 같이 고기를 구워 먹게 되었다."
    "나는 뻔대의 역할을 다하기 위해 자연스럽게 고기를 굽는 역할을 맡게 되었다."

    #과 파라미터에 따라 달라지는 스크립트. 5, 6
    #5 과 파라미터가 n 이상일 때
    if gwa_parameter >= 20 :
        show gogi_s at truecenter
        Jangjung "와 뻔대 최고다! 고기 진짜 잘 굽네."
        Ohduck "오이시이~ 아리가또 고자이마스. 뻔대쿤"
        Daehyun "진짜 너무 맛있다. 뻔대야 힘들면 바꿔줄까?"
        Player "아녀아녀 괜찮아. 맛있다니 다행이네."
        Hyunjae "아 저기 고기 다 떨어진 것 같은데, 꺼내 줘야겠다. (부스럭부스럭) 여기!"
        Player "오 땡큐~ 일단 앉아있어. 고기 굽는데 조금 더 걸리니까."

        "친구들이 내가 구운 고기를 맛있게 먹고,\n알아서 일을 도와준다. 행복하다."
        #멘탈 +
        $ mental_point += 10
        call parameter_maxmin_check

    #6 과 파라미터가 n 미만일 때
    else :
        scene black
        "굽고 있는 고기를 보면서 새 고기를 꺼내다가 땅에 떨어뜨려버렸다!"

        show gogi_f at truecenter
        Samyong "아~ 뻔대 뭐하냐."
        Hyunjae "아 아까운 고기...뻔대야 정신 차리자~!"
        Geumji "그래 그래 고기는 맛있지만, 돈 아깝게 고기는 왜 떨어뜨리니.."
        Ohduck "큽...아깝다는.."
        Player "으아아 미안 미안...으앗 고기 탄다 탄다!!"

        "구박을 받으면서 고기를 열심히 구웠다. 나름 열심히 하고 있는데, 아무도 알아주지 않는 것 같아 살짝 서러웠다."
        #멘탈 -
        $ mental_point -= 20
        call parameter_maxmin_check

    show gwa at truecenter
    "친구들과 고기를 먹은 후, 레크리에이션을 다들 즐겁게 즐겼다. 준비한 보람이 있었다."
    "어느새 밤이 깊었고, 본격적으로 술자리가 시작되었다."

    show gwa_3 at truecenter
    Player "자 모두 잔 채웠지?"
    Jinil "당연하지!"
    Samyong "오키오키~"
    Ohduck "그렇다는~"
    Jangjung "빨리빨리 마시자! 뻔대야 건배사 해~"
    Player "오키오키! 자 문정과 19학번, 아직 밤은 기니까 신나게 마셔보자! 자 건배!!"
    "친구들" "건배!!!!!!"

    "자연스럽게 친구들 사이를 돌아다니면서 소주 한 병 정도를 마셨다.."

    #두 병째
    scene black
    "아직 좀 더 마실 수 있을 것 같다.\n방의 구석에서 삼용이가 손짓을 하는 게 보인다.\n어떻게 할까??"
    $ rest_point = 3
    menu:
        "과 친구들과 마신다":
            call gwa_2

        "삼용이와 마신다":
            call friend_2

        "방에서 쉰다":
            #체력 파라미터 증가
            jump rest

    #세 병째
    scene black
    "살짝 취했지만, 아직은 좀 더 마실 수 있을 것 같다. \n마당에서 장중이가 나를 부르는 게 들린다. \n어떻게 할까?"
    menu :
        "과 친구들과 마신다":
            call gwa_3

        "장중이와 마신다":
            call friend_3

        "방에서 쉰다":
            #체력 파라미터 변화 없음
            jump rest

    #네 병째
    $ rest_point -= 1
    "술을 마시던 와중 진일이가 안 보인다는 것을 깨달았다."
    "페이스북을 확인헤보니 길을 잃은 듯 하다. 댓글로 위치 정보를 전달받아서 파악한 위치를 바탕으로 진일이를 찾으러 갔다."

    Player "아니 어디까지 간거야.."
    Jinil "어! 우리 뻔대~~"
    Player "휴...찾았다...야! 진일아 어쩌다 여기까지 왔냐;; 아니다 일단 돌아가자."

    "진일이를 찾아 숙소로 돌아왔다. 아이들이 많이 취한 것 같아보인다."

    scene black
    "여기서 술을 더 마시면 내일 많이 못 도와줄 것 같다. \n진일이가 또 자리를 비운 것 같다. \n어떻게 할까?"
    menu :
        "과 친구들과 마신다":
            call gwa_4

        "진일이를 찾으러 간다":
            call friend_4

        "방에서 쉰다":
            #체력 파라미터 변화 없음
            jump rest

    #다섯 병째
    $ rest_point -= 1
    scene black
    "이제 슬슬 버티기 힘들다. 술을 너무 많이 마신 것 같다. \n장중, 진일, 용삼이 한 쪽에서 따로 술을 마시고 있다. \n어떻게 할까?"
    menu :
        "과 친구들과 마신다":
            call gwa_5
            #체력, 과 파라미터 감소
        "장중, 진일, 용삼의 술자리에 합류한다":
            call friend_5
            #체력, 과 파라미터 감소
        "방에서 쉰다":
            jump rest

    jump fun_morning

    return

label rest:
    show big_room at truecenter
    "술을 그만 마시고 방에 들어가 자기로 결정했다."
    Player "으아...나 피곤해서 먼저 자러 들어갈게"
    show small_room at truecenter
    "방에 들어가 쉬었다."
    scene black

    if rest_point == 3 :
        "자는 도중, 진일이가 길을 잃었다는 소리를 듣고 깜짝 놀라 진일이를 찾으러 새벽 거리를 돌아다녔다."
        "다행히도 진일이가 위치정보를 인터넷에 올려줘서 그것을 바탕으로 진일이를 찾을 수 있었다."
        "이후 돌아와서 다시 잠을 청했다."
        jump fun_morning

    else :
        "따로 깨는 일 없이 잠을 잘 수 있었다."
        jump fun_morning
    return

label fun_morning:
    call change_SNS
    $ day += 1
    $ day_or_evening = "day"

    if rest_point == 3 :
        "어제 잠을 빨리 자서 그런가..개운한 느낌이다."
        "밖을 보니 슬슬 첫 차가 다닐 시점이라 몇몇 아이들이 갈 준비를 하는 것 같다."

        show big_room at truecenter
        Player "자! 그럼 슬슬 치워볼까?"
        Hyunjae "오...뻔대~ 일어나자마자 일하네, 거진 워커홀릭"
        Player "ㅋㅋㅋㅋㅋㅋㅋ 그럴 수 있지, 빨리 치우고 해장용 라면 남은 거 있으니까 그거라도 끓여먹자!"
        Daehyun "크~ 뻔대 멋있다~"

        scene black
        "살아 있는 친구들과 열심히 방을 치우고, 라면을 끓여 나눠 먹었다."

        show ramyen at truecenter
        Player "크...속이 풀린다~"
        Daehyun "내말이~ 와 뻔대 라면도 잘끓여~"
        Player "ㅋㅋㅋ 맛있게 먹어줘서 다행이지, 음..이제 슬슬 애들 깨울까?"
        Hyunjae "뭐 슬슬 체크아웃 시간이니까.."

        show small_room at truecenter
        Player "얘들아! 일어나!! 슬슬 집에가자!!"
        Player "다들 짐 챙기고~ 잃어버린 거 없이 다 챙겨서 나가자!"

        show subway at truecenter
        "아이들을 깨워서 다 같이 집으로 향했다. 몸 상태도 생각보다 괜찮고, 친구들과 웃으며 얘기를 하다보니 어느새 집에 거의 도착한 것 같다.."
        #과 파라미터 많이 +
        $ gwa_parameter += 5
        call parameter_maxmin_check

    elif rest_point == 2 :
        "머리가 살짝 아프지만 생각보다 괜찮은 듯하다.."
        "밖을 보니, 첫 차를 타고 간 아이들이 몇 명 정도 있는 것 같다. 남은 아이들은 정리를 거의 끝내둔 것 같다."

        show big_room at truecenter
        Player "으악 미안;; 못 도와줘서..대신 해장용 라면 남아있을 것 같은데 끓여줄게.."
        Mirae "오~ 끓여준다면 당연히 먹지~"
        Daehyun "감사 감사~"
        Player "오키 오키~ 조금만 기다려주삼~"

        scene black
        "라면을 끓여 친구들과 나눠 먹었다."

        show ramyen at truecenter
        Player "크...속이 풀린다~"
        Daehyun "내말이~ 와 뻔대 라면도 잘끓여~"
        Player "ㅋㅋㅋ 맛있게 먹어줘서 다행이지, 음..이제 슬슬 애들 깨울까?"
        Hyunjae "뭐 슬슬 체크아웃 시간이니까.."

        show small_room at truecenter
        Player "얘들아! 일어나!! 슬슬 집에가자!!"
        Player "다들 짐 챙기고~ 잃어버린 거 없이 다 챙겨서 나가자!"

        show subway at truecenter
        "아이들을 깨워서 다 같이 집으로 향했다. 머리는 살짝 아팠지만, 친구들과 웃으며 얘기를 하다보니 어느새 집에 거의 도착한 것 같다.."
        #과 패러미터 보통 +
        $ gwa_parameter += 3
        call parameter_maxmin_check

    elif rest_point == 1 :
        "숙취로 머리가 아프다..눈을 떠보니 대부분의 애들이 잠을 자고 있다."
        "밖을 보니, 친구들끼리 해장용으로 라면을 끓여 먹은 것 같다."
        show big_room at truecenter
        "첫 차를 타고 간 아이들이 그래도 어느 정도 정리는 해둔 것 같다."

        show small_room at truecenter
        Player "으으으..머리야...시간이..? 음..체크아웃 시간까지는 조금 남았지만 슬슬 애들 깨울까..?"
        Player "얘들아! 일어나!! 슬슬 집에가자!!"
        Player "다들 짐 챙기고~ 잃어버린 거 없이 다 챙겨서 나가자!"

        show subway at truecenter
        "아이들을 깨워서 다 같이 집으로 향했다. 술을 많이 마셔서 머리는 살짝 아팠지만, 친구들과 얘기를 하다보니 어느새 집에 거의 도착한 것 같다.."
        #과 파라미터 조금 +
        $ gwa_parameter += 1
        call parameter_maxmin_check

    else :
        "머리가 너무 아프다..눈을 떠보니 대부분의 애들은 집에 간 것 같다."
        "남아 있는 것은 나와 어제 술을 마시다가 완전히 죽은 친구들뿐인 것 같다."
        show big_room at truecenter
        "방은 그래도 먼저 간 친구들이 치워준 모양인지 생각보다 깔끔했다...체크아웃 시간이 가까워졌기 때문에 남은 짐과 애들을 챙겨 엠티 장소에서 출발하였다."
        show subway at truecenter
        "집까지 갈 길이 아주 먼 것 같다.."

    call change_SNS
    $ day_for_show = 7
    $ day += 1
    $ day_or_evening = "evening"
    jump weekday_SNS

    return
