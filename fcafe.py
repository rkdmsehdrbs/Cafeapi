def cafe_order_system_full_menu():
    # 전체 메뉴 데이터
    full_menu_data = {
        "메가커피": {
            "커피": {"아메리카노": 2000, "카페 라떼": 2700, "바닐라 라떼": 3200, "메가리카노": 3000},
            "스무디/프라페": {"딸기 스무디": 3900, "초코 프라페": 3900, "쿠키 프라페": 4200},
            "티/에이드": {"레몬 에이드": 3500, "자몽 에이드": 3500, "녹차": 2500, "허브티": 2800}
        },
        "컴포즈 커피": {
            "커피": {"아메리카노": 1500, "카페 라떼": 2700, "카라멜 마끼아또": 3500, "돌체 라떼": 3900},
            "스무디/프라페": {"딸기 요거트 스무디": 3900, "민트초코 프라페": 3900, "플레인 요거트 스무디": 3800},
            "티/에이드": {"청포도 에이드": 3800, "패션후르츠 에이드": 3800, "아이스티 (복숭아)": 2500}
        },
        "이디야 커피": {
            "커피": {"아메리카노": 3200, "카페 라떼": 3700, "토피넛 라떼": 4200, "콜드브루": 3900},
            "스무디/프라페": {"딸기 요거트 플랫치노": 4200, "초코렛 칩 플랫치노": 4200, "녹차 플랫치노": 4200},
            "티/에이드": {"자몽 네이블 오렌지": 4200, "유자차": 3500, "레몬차": 3500}
        },
        "스타벅스": {
            "커피": {"아메리카노": 4500, "카페 라떼": 5000, "돌체 라떼": 6000, "콜드 브루": 5000},
            "프라푸치노": {"자바 칩 프라푸치노": 6300, "카라멜 프라푸치노": 5900, "그린 티 크림 프라푸치노": 6300},
            "티/기타 음료": {"제주 유기농 말차로 만든 라떼": 6100, "자몽 허니 블랙 티": 5700, "쿨 라임 피지오": 5900}
        },
        "투썸플레이스": {
            "커피": {"아메리카노": 4500, "카페 라떼": 5000, "스페니쉬 연유 라떼": 5800, "콜드브루": 5000},
            "프라페/스무디": {"스트로베리 피치 프라페": 6300, "망고 요거트 스무디": 6000, "초콜릿 쉐이크": 6000},
            "티/에이드": {"오렌지 자몽 티": 5300, "복숭아 아이스티": 4500, "레몬 그라스 티": 4500}
        }
    }

    # 1. 카페 선택
    print("--- 카페를 선택해주세요 ---")
    cafes = {i + 1: name for i, name in enumerate(full_menu_data.keys())}
    for num, name in cafes.items():
        print(f"{num}. {name}")

    selected_cafe_num = int(input("번호를 입력해주세요: "))
    selected_cafe_name = cafes.get(selected_cafe_num)

    if not selected_cafe_name:
        print("잘못된 카페 번호입니다. 시스템을 종료합니다.")
        return

    print(f"\n--- {selected_cafe_name}를 선택하셨습니다. ---")
    current_cafe_menu = full_menu_data[selected_cafe_name]

    # 2. 메뉴 카테고리 선택
    print("\n--- 메뉴 카테고리를 선택해주세요 ---")
    categories = {i + 1: name for i, name in enumerate(current_cafe_menu.keys())}
    for num, name in categories.items():
        print(f"{num}. {name}")

    selected_category_num = int(input("번호를 입력해주세요: "))
    selected_category_name = categories.get(selected_category_num)

    if not selected_category_name:
        print("잘못된 카테고리 번호입니다. 시스템을 종료합니다.")
        return

    print(f"\n--- {selected_category_name}를 선택하셨습니다. ---")
    current_category_items = current_cafe_menu[selected_category_name]

    # 3. 상세 메뉴 선택
    print(f"\n--- {selected_category_name} 상세 메뉴를 선택해주세요 ---")
    menu_items_with_price = {i + 1: (item, price) for i, (item, price) in enumerate(current_category_items.items())}
    for num, (item, price) in menu_items_with_price.items():
        print(f"{num}. {item} ({price}원)")

    selected_item_num = int(input("번호를 입력해주세요: "))
    selected_item_info = menu_items_with_price.get(selected_item_num)

    if not selected_item_info:
        print("잘못된 메뉴 번호입니다. 시스템을 종료합니다.")
        return

    selected_item_name, selected_item_price = selected_item_info
    print(f"\n--- '{selected_item_name}'을(를) {selected_item_price}원에 선택하셨습니다. ---")

    # 4. 결제 진행/취소
    print("\n--- 결제를 진행하시겠습니까? ---")
    print("1. 결제 진행")
    print("2. 결제 취소")

    payment_choice = int(input("번호를 입력해주세요: "))

    if payment_choice == 1:
        # 5. 영수증 필요 여부
        print("\n--- 영수증이 필요하세요? ---")
        print("1. 영수증 필요함")
        print("2. 영수증 필요없음")

        receipt_choice = int(input("번호를 입력해주세요: "))

        if receipt_choice == 1:
            print("영수증이 발행됩니다.")
        elif receipt_choice == 2:
            print("영수증이 발행되지 않습니다.")
        else:
            print("잘못된 선택입니다. 영수증은 발행되지 않습니다.")

        print("\n*** 주문이 완료되었습니다. 감사합니다! ***")
        print(f"주문 내역: {selected_cafe_name} - {selected_category_name} - {selected_item_name} ({selected_item_price}원)")

    elif payment_choice == 2:
        print("\n결제가 취소되었습니다. 주문을 다시 진행해주세요.")
    else:
        print("\n잘못된 선택입니다. 결제가 취소되었습니다.")

# 시스템 실행
cafe_order_system_full_menu()