# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

# 4월 16일 축제 이벤트

#이미지 선언
image fest_poong = "festival/fest_poong.jpg"
image fest_food = "festival/fest_food.jpg"
image fest_stage = "festival/fest_stage.jpg"
image cuprice = "festival/cuprice.jpg"
image shrimp = "festival/shrimp.jpg"
image steak = "festival/steak.jpg"
image soran = "festival/soran.jpg"

# week3 day 1
label festival:

    scene black
    "오늘은 축제가 있는 날! 소란 공연을 같이 보기로 한 친구들과 저녁을 같이 먹기로 하였다."

    scene fest_stage at truecenter
    "주인공" "으음 뭐 먹지? 축제니까 주변에 있는 노점상에서 먹을까?"
    "장중" "오오~ 난 그게 좋은 것 같은데?"
    "삼용" "근데 먹을거 파는 곳이 생각보다 많다..우와 푸드트럭?"
    "미래" "오 푸드트럭 괜찮지! 안 그래 현재야?"
    "현재" "미래가 괜찮으면 나도 당연히 괜찮지~"
    "진일" "....야 죽창 어딨냐 죽창!!"
    "미래" "꺄악~"
    "현재" "꺄악~"
    scene fest_food at truecenter
    "주인공" "자자 진정하고~ 그래서 보자 푸드트럭도 종류가 여러 개 있는 것 같은데 어디가 좋을까?"
    "삼용" "난 스테이크!! 저게 제일 맛있어 보이는데?"
    "장중" "난 새우! 새우에 맥주를 딱!"
    "진일" "저 컵밥도 괜찮지 않냐?? 뻔대야 너는 뭐 먹고 싶은데?"
    "주인공" "음...나는..."

    menu:
        "나는 스테이크!!" :
            scene steak at truecenter
            "삼용" "그래 이런 날엔 고기지~"
            "장중" "음...고기도 나쁘지는 않으니까"
            "진일" "뭐 네가 그걸 골라도 난 컵밥 먹으련다~"
            "미래" "오오 스테이크~ 맛있겠다!"

            scene black
            "친구들과 함께 푸드트럭에서 스테이크를 사먹었다."
            #삼용 파라미터 업

        "난 새우~" :
            scene shrimp at truecenter
            "장중" "크~ 역시 뻔대면 새우를 고를 줄 알았어!"
            "삼용" "엥? 고기 안먹고??"
            "진일" "새우 그거 먹고 배가 차겠냐?? 난 컵밥 먹을랜다~"
            "현재" "오오 새우 괜찮지~"
            "장중" "그럼 맥주도 한 캔 사먹자!!"

            scene black
            "친구들과 함께 푸드트럭에서 새우를 사먹었다."
            #장중 파라미터 업

        "오늘은 컵밥이 땡기네~" :
            scene cuprice at truecenter
            "진일" "그렇지! 컵밥이지!! 한국인은 밥심! 아니겠냐~"
            "장중" "컵밥은 평소에도 빨간 코끼리에서 사먹을 수 있잖아;;"
            "삼용" "그니까..난 스테이크 먹을래~"
            "대현" "컵밥 괜찮지!!"

            scene black
            "친구들과 함께 푸드트럭에서 컵밥을 사먹었다."
            #진일 파라미터 업

    scene fest_food at truecenter
    "주인공" "아~ 배부르다~ 그럼 슬슬 공연장으로 갈까?"
    "장중" "음 공연장이 어디더라?"
    "삼용" "여기 페이스북에 나와있어 어디지..? 느티골 풍악마당..?"
    "현재" "힉..풍악마당이면 그 기숙사 있는데까지 올라가야 하지 않냐?"
    "대현" "응 거기 맞을걸..?"
    "미래" "으아..언제 올라가.."
    "진일" "어휴 이 저질체력들! 그럴 시간에 빨리 올라가자"
    "주인공" "맞아 맞아 곧 공연 시작하겠다!!"

    scene black
    "친구들과 이야기를 하면서 오르막길을 올라갔다. 얘기를 하다보니 금방 도착할 수 있었다."

    scene fest_poong at truecenter
    "장중" "와!! 도착!!!"
    "미래" "흐아..힘들었다.."
    "현재" "그래도 생각보다 빨리 도착했네.."
    "삼용" "엥? 근데 진일이는?"
    "진일" "헥..너희..헉..너무..헉...빠른..거..아니..학..냐.."
    "대현" "....저 친구가 제일 저질 체력이었네..."
    "주인공" "진일아 운동하자.."
    "진일" "아니 내가 원래는 튼튼했어! 이게 다 고3때 운동을 안해서 그런거임"
    "진일" "너넨 나처럼 되지 마라.."
    "장중" "엌ㅋㅋㅋㅋ"
    "삼용" "오..앞에 자리 비었다 앞에서 보자!!!"
    "주인공" "좋아좋아!!"
    "미래" "오오!! 저 사람들 아니야??"
    scene soran at truecenter
    "소란" "안녕하세요~! 저희는 소란입니다~!"
    "와아아아"
    "소란" "소리질러~!!"
    "와아아아아~~"

    scene black
    "친구들과 함께 열심히 소리 지르면서 공연을 볼 수 있었다."

    scene donga at truecenter
    return
