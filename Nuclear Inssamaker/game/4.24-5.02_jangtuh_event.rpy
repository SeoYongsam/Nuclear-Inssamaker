#저녁 이벤트

# 4월 24,25,26일 + 5월 2일 장터 이벤트
# month4 week4 day2,3,4
# month5 week1 day1

label jangtuh_event:

    #4월 24일 포스터 회의
    scene black
    "오늘은 장터 준비위원회끼리 모여서 포스터 디자인을 하기로 했다."

    "내가 없어도 회의가 잘 돌아갈 것 같지만...\n갈까 말까?"

    menu:
        "회의에 참여한다":

            "회의에 참여했다."

            show poster at truecenter

            "포스터 디자인은 심플하게 가기로 했다."
            "사실 심플 할지는 모르겠지만 포토샵을 다룰 줄 아는 현재가 알아서 하기로 했다."
            "워낙 회의가 잘 진행돼서 내가 안왔어도 됐으려나 싶지만 그래도 마음은 조금 놓인다."


        "계획한 대로 오후를 보낸다":
            ""

    return


    #4월 25일 예산 및 메뉴 정하기
    scene black
    "오늘은 장터 준비위원회끼리 모여서 예산 및 메뉴를 정하기로 했다."

    "내가 없어도 회의가 잘 돌아갈 것 같지만...
    \n 갈까 말까?"

    menu:
        "회의에 참여한다":

            "회의에 참여했다."

            show meeting at truecenter

            "예산은 적당하게 50만원으로 잡았다."
            "메뉴는 다른 장터와 차별을 두고 싶었지만 예산에 맞춰 재료를 준비해야했기
            때문에 파전과 치킨너겟 등 기존 장터들과 비슷하게 메뉴를 정했다."
            "오늘 회의에 와서 다행이라고 생각한다."
            "애들이 열정이 많아서인지 무모해서인지는 모르겠지만 메뉴를 정할때 회의가 산으로 갈 뻔한 적이 많았다."

        "계획한 대로 오후를 보낸다":
            ""

    return


    #4월 26일 메뉴판 만들기
    scene black
    "오늘은 장터 준비위원회끼리 모여서 메뉴판을 만들기로 했다."

    "내가 없어도 메뉴판을 잘 만들 것 같지만...
    \n 갈까 말까?"

    menu:
        "회의에 참여한다":

            "회의에 참여했다."

            show menu_pan at truecenter

            "메뉴판은 정말 쉽게 정했다."
            "이미 메뉴를 정했기 때문에 장터날에 붙일 것만 만들면 됐기 때문이다."
            "오늘은 회의 보다는 메뉴판 디자인을 했디 때문에 내가 안왔어도 됐으려나 싶지만 그래도 마음은 조금 놓인다."


        "계획한 대로 오후를 보낸다":
            ""

    return

    #5월 2일 장보기
    scene black
    "오늘은 장터 준비위원회끼리 장터 전날 모여서 장을 보기로 했다."

    "내가 없어도 장을 잘 볼 수 있을지 의심스럽지만...
    \n 갈까 말까?"

    menu:
        "장을 보러 간다":

            "장을 보러 갔다."

            show shopping at truecenter

            "오늘은 내가 장을 보러 왔어야 했다."
            "애들의 상태가 의심스럽기 때문이다. 중간고사가 끝난지 얼마 안돼서 모든 것을 놓은 것만 같다."
            "장터 재료를 사는 것 보다 애들은 자신이 필요한 것들에 더 눈이 가는 것 같다."
            "다행이 나라도 정신을 차리고 장터에 필요한 도구와 음식을 샀다."


        "계획한 대로 오후를 보낸다":
            ""

    return
