image gwa_2 = "fun_mt/gwa_2.jpg"
image gwa_3 = "fun_mt/gwa_3.jpg"
image gwa_4 = "fun_mt/gwa_4.jpg"
image gwa_5 = "fun_mt/gwa_5.jpg"

label gwa_2:
    "돌아다니면서 술을 마시기로 결정했다."

    show gwa_2 at truecenter
    "친구들" "술이 들어간다 쭉쭉쭉쭉쭉~ 언제까지 어깨 춤을 추게 할거야~"
    "친구들" "신난다! 재미난다! 더 게임 오브 데스!"
    "왁자지껄"

    scene black
    "친구들과 술을 마시면서 놀았다...\n소주 1병 정도를 더 비운 것 같다.."
    #과 파라미터 +
    return

label gwa_3:
    "돌아다니면서 술을 마시기로 결정했다."

    show gwa_3 at truecenter
    "친구들" "바니바니 바니바니 당근 당근!"
    "친구들" "아 공동묘지에 아싸! 올라갔더니 아싸!"
    "와글와글"

    scene black
    "덕현이가 감정이 북받쳐 울음을 터뜨렸다. \n덕현이를를 최대한 달래주었다...\n소주 1병 정도를 더 비운 것 같다.."
    #과 파라미터 +
    return

label gwa_4:
    "돌아다니면서 술을 마시기로 결정했다."

    show gwa_4 at truecenter
    "친구들" "빰 빠바밤 바바밤 바바밤! 세박자 세박자"
    "친구들" "맛있는건 정말 참을 수 없어~ 누구든 맛을 보면 이!렇!게!"
    "시끌시끌"

    scene black
    "친구 한 명이 방에 토를 했다. \n방을 청소했다...\n이후 소주 1병 정도를 더 비운 것 같다.."
    return

label gwa_5:
    "돌아다니면서 술을 마시기로 결정했다."
    "...시야가 살짝 뿌연것 같다."

    show gwa_5 at truecenter
    "친구들" "공산당 게임~ 공산당 게임~"
    "친구들" "뻔대 마셔라~ 마시고 뒤져라! 어이어이어이!"
    "웅성웅성"

    scene black
    "술을 마시다 토를 한 것 같다 \n애들이 내 몸을 씻겨주는 것 같다..."
    "분위기가 싸해진 것을 느끼면서 정신을 잃었다."

    #과 파라미터 감소
    $ gwa_parameter -= 2
    call parameter_maxmin_check

    $rest_point -= 1
    return
