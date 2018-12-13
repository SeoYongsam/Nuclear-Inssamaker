#이미지 선언
image pcbang = "pcbang/pcbang.jpg"
image leagueoflegends = "pcbang/leagueoflegends.jpeg"
image leagueloss = "pcbang/leagueloss.png"
image kartrider = "pcbang/kartrider.jpg"
image pcbangstreet = "pcbang/pcbangstreet.jpg"

#피시방 이벤트 4월 11일 month4 week2 day3
label pcbang:
    scene black
    "갑자기 대현이가 현재, 미래, 그리고 진일이와 함께 게임을 하러 PC방에 가자고 한다."
    "가게 되면 오늘 오후 스케줄은 계획대로 진행하지 못하는데... 어떡할까?"

    menu:
        "PC방에 같이 가서 게임을 한다":
            show pcbang at truecenter
            "결국 친구들이랑 PC방에 같이 갔다"
            "대현" "얘들아 무슨 게임 할래?"
            "진일" "5명이면 당연히 '리그 오브 전설' 해야 하는 거 아닌가?"
            "현재" "미래랑 나는 '쇼핑카트 라이더' 생각하고 있었는데..."
            "미래" "우리끼리 대전하는게 재밌지 않아? 서로 경쟁하고 내기도 할수 있고!"
            "대현" "난 다 좋아 ㅋㅋ 뻔대야 넌 뭐하고 싶어?"

            menu:
                "'리그 오브 전설'을 한다":
                    show leagueoflegends at truecenter
                    "진일" "좋았으~ 역시 게임은 '리그 오브 전설'이지~
                    내가 특별히 너네들 캐리 해줄게!!"
                    "현재" "ㅋㅋ 알겠어"
                    "대현" "뻔대 넌 처음 하는거지? 내가 옆에서 도와줄게 ㅋㅋ"

                    scene black
                    "30분 뒤..."

                    show leagueloss at truecenter
                    "진일" "아 니네들 진짜 뭐하냐. 뻔대 너는 내가 숟가락을 입에 넣어줘도 못 받아먹네.\n
                    게임 하고 싶은거 맞아?"
                    "미래" "왜 그래 진일아... 그냥 게임 이잖아"
                    "현재" "진정해 ㅋㅋ 다음판 이기면 되지"
                    "대현" "그래 다음판은 꼭 이기자"
                    "진일" "하..."

                    scene black
                    "2시간 뒤"

                    show pcbangstreet at truecenter
                    "대현" "아~ 그래도 피방 오랜만에 가니까 개재밌다"
                    "진일" "내가 캐리 해줬으니까 재밌었던거겠지~
                    뻔대야 게임 잘 못하면 말하지~ 내가 다음번엔 제대로 가르쳐줄게"
                    "현재" "ㅋㅋ"
                    "미래" "... 뻔대야 너무 신경쓰지마!"

                    scene black at truecenter
                    "오늘 내가 게임을 잘 못했지만 친구들이 게임을 잘해서 자주 이긴 것 같다.\n
                    그래도 친구들은 모두 재밌게 게임한 것 같다."
                    "진일이는 오늘 '리그 오브 전설'을 할 수 있어서 전반적으로 행복해했던 것 같다.
                    하지만 나는 게임하는 도중 게속해서 진일이에게 질타를 받고 진일이의 눈치를 봐야해서 힘들었다."
                    #진일이와의 친밀도 UP, 멘탈 DOWN
                    $ jinil.parameter += 20
                    $ mental_point -= 10
                    call parameter_maxmin_check

                "'쇼핑카트 라이더'를 한다":
                    show kartrider at truecenter
                    "현재" "오케이~ '쇼핑카트 라이더' 가즈아~~~!"
                    "미래" "후후후 난 심지어 면허도 있다고 이 무면허들아~"
                    "대현" "너 장롱면허잖아 ㅋㅋㅋㅋ"
                    "미래" "없는것 보단 낫거든~"
                    "진일" "ㅋㅋ"
                    "대현" "진일아 얼른 들어와"

                    scene black
                    "3시간 뒤"

                    scene kartrider_end at truecenter
                    "대현: 아 치사하게 마지막에 아이템 쓰는거 뭐냐"
                    "미래" "ㅋㅋㅋㅋ 이것도 실력이라구~"
                    "현재" "와 미래 뭐야? 엄청 잘하네"
                    "미래" "그럼 뭐해 뻔대가 결국 1등 했는데"
                    "대현" "근데 진일이는 카트 오늘 처음함? 개못하던데 ㅋㅋㅋㅋ"
                    "진일" "..."
                    "미래" "박대현 너도 비슷비슷 하거든? 진일이 괴롭히지 마 ㅋㅋㅋ"

                    scene pcbangstreet at truecenter
                    "대현 : 아~ 그래도 피방 오랜만에 오니까 개재밌다"
                    "미래 : ㅋㅋㅋㅋ 내 운전실력 다시는 무시하지마라~"
                    "대현 : 미래 게임 진짜 잘하구나..."
                    "현재 : 와 근데 뻔대도 진짜 잘하던데?? 오늘 나 한번도 1등 못함 얘 때문에!"
                    "미래 : 맞아맞아 장난 아니더라. 프로 게이머인줄?"
                    "진일 : '쇼핑카트 라이더'도 재밌네. '리그 오브 전설'했으면 더 재밌었겠지만."
                    "대현 : 에이~ 진일이 왜그래 아까 재밌게 하던데~"
                    "진일 : ㅋㅋ"

                    scene black
                    "오늘 카트라이더를 오랜만에 해서 너무 재밌었다. 운이 좋아서 그런지 게임도 잘됐다.
                    친구 여럿과 함께 즐겁게 게임을 하니 더 친해진 것 같다."
                    "하지만 진일이는 오늘 '리그 오브 전설'을 못해서 그런지 기분이 좋지 않은 것 같다."

                    #진일이와의 친밀도 DOWN, 멘탈 UP
                    $ jinil.parameter -= 10
                    $ mental_point += 10
                    call parameter_maxmin_check


        "정중히 거절하고 예정된 계획대로 하루를 보낸다" :
            ""
            #과활동 패러미터 DOWN
            $ gwa_parameter -= 10
            call parameter_maxmin_check

    return
