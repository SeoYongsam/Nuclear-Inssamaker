# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.
define Jinil = Character("진일", color="#ffcccc", image="Jinil")#, window_left_padding = -100)
image side Jinil :
    "character/cha1.png"
    xzoom -1

define Player = Character("주인공", color="#ffcccc", image="Player")
image side Player :
    "character/cha2.png"
    xzoom -1

define Jangjung = Character("장중", color="#ffcccc", image="Jangjung")
image side Jangjung :
    "character/cha3.png"
    xzoom -1

define Samyong = Character("삼용", color="#ffcccc", image="Samyong")
image side Samyong :
    "character/cha4.png"
    xzoom -1


label weekday_evening_event :
    if month == 3 :
        if week == 3 :
            if day == 1 :
                call pcbang

            elif day == 2 :
                Player "과잠준비위원회 지원해주셔서 감사합니다!"
                Jangjung "동기가 일하는데 도와줘야지!"
                Jinil "카모로하면 멋있을 것 같다 ㅋㅋㅋㅋ"
                Samyong "나는 빨간색에 용무늬가 들어갔으면 좋겠는데 ㅋㅋㅋ"
                Player "오 독특하고 좋은데? 근데 우리 손목에는 이름 적을거야?"
                Jinil "별명으로 적자 ㅋㅋㅋ"
                Jangjung "아 에바야…."
                Samyong "일단 어떤 디자인으로 할지 예시부터 정해보자!"
                Jangjung "그러면 실제로 원단도 만져보고 업체랑 디자인 회의도 해야할 것 같은데? 내일 업체 가볼래??"
                Jinil "아 무슨 귀찮게 그런걸 하냐.. 너무 멀다 ㅋㅋㅋ 언제 거기까지 가 ㅋ"
                Samyong "나는 찬성! 사진에서 예뻐보이는데 실제로는 별로일 수도 있어 ㅋㅋㅋㅋ"
                Jinil "아니, 그럴 필요가 없다니까… 사진이랑 다르면 업체가 잘 안되지 ㅋㅋㅋ 여기 1위 업체라서 지금 주문도 밀렸다는데"
                Player "그러면 음…. 어떻게 해야되나"
                Player "그래도 빨리 만들어야하니까 내일 업체 방문할지 정할까?"
                "과잠 업체를 방문하시겠습니까?"
                menu :
                    "예" :
                        "흥"
                    "아니오" :
                        "흥"


            elif day == 3 :
                "null"

            elif day == 4 :
                "null"

            elif day == 5 :
                "null"

            elif day == 6 :
                "null"

    return
