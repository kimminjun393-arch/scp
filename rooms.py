import time
from utils import type_text, print_line
from player import player_data

def intro():
    print_line()
    type_text("⚠️ [시스템 경고] 제19기지 다중 격리 파기 발생.")
    type_text("⚠️ 모든 보안 인원은 즉시 지정된 구역으로 대피하십시오.")
    print_line()
    time.sleep(1)
    type_text("당신은 D계급 인원입니다. 철문이 부서지는 소리가 들렸고, 당신의 감방 문이 열려 있습니다.")
    type_text("살아남으려면 시설을 빠져나가야 합니다.")

def room_d_class():
    print_line()
    type_text("📍 현재 위치: D계급 감방 복도")
    type_text("어둡고 음산합니다. 바닥에 피자국이 있습니다.")
    print("1. 관리실로 간다.")
    print("2. 제1격리구역으로 간다.")
    
    choice = input(">> 선택 (1/2): ")
    if choice == '1':
        return "관리실"
    elif choice == '2':
        return "제1격리구역"
    else:
        type_text("잘못된 선택입니다. 다시 생각해보세요.")
        return "D계급 감방"

def room_admin():
    print_line()
    type_text("📍 현재 위치: 관리실")
    if "3등급 키카드" not in player_data["inventory"]:
        type_text("책상 위에 신분증이 떨어져 있습니다.")
        print("1. 신분증을 챙긴다.")
        print("2. 무시하고 돌아간다.")
        choice = input(">> 선택 (1/2): ")
        if choice == '1':
            type_text("[+] '3등급 키카드'를 획득했습니다!", 0.05)
            player_data["inventory"].append("3등급 키카드")
    else:
        type_text("더 이상 이곳에서 챙길 것은 없어 보입니다.")
    
    type_text("복도로 돌아갑니다.")
    time.sleep(1)
    return "D계급 감방"

def room_containment_1():
    print_line()
    type_text("📍 현재 위치: 제1격리구역")
    type_text("문을 열자마자 콘크리트로 된 기괴한 조각상, [SCP-173]이 당신을 바라보고 있습니다!")
    type_text("깜빡이는 조명... 조명이 꺼지기 전에 행동해야 합니다!")
    
    print("1. 시선을 고정하고 뒷걸음질로 빠져나간다.")
    print("2. 뒤돌아서 전력으로 도망친다.")
    
    choice = input(">> 선택 (1/2): ")
    if choice == '1':
        type_text("눈물이 날 정도로 눈을 부릅뜨고 시선을 고정했습니다.")
        type_text("무사히 방을 빠져나와 문을 닫았습니다. 생존했습니다.")
        time.sleep(1)
        return "무기고"
    else:
        type_text("뒤를 돌아 뛰려는 순간, '콰직!' 하는 소리와 함께 목이 꺾였습니다.")
        player_data["hp"] = 0
        return "사망"

def room_armory():
    print_line()
    type_text("📍 현재 위치: 무기고 앞 복도")
    type_text("검은 망토를 두르고 새 부리 가면을 쓴 자, [SCP-049]가 다가옵니다.")
    type_text("'당신에게서... 역병의 냄새가 나는군요. 치료해 드리겠습니다.'")
    
    print("1. 근처에 있는 쇠파이프를 집어 던진다.")
    print("2. 바닥에 납작 엎드려 죽은 척한다.")
    
    choice = input(">> 선택 (1/2): ")
    if choice == '1':
        type_text("쇠파이프가 벽에 부딪히며 큰 소리를 냈습니다.")
        type_text("SCP-049가 소리가 난 쪽으로 고개를 돌린 틈을 타 게이트로 도망쳤습니다!")
        time.sleep(1)
        return "게이트A"
    else:
        type_text("SCP-049가 당신을 내려다보며 손을 뻗습니다. 그의 손이 닿자마자 의식을 잃었습니다...")
        player_data["hp"] = 0
        return "사망"

def room_gate_a():
    print_line()
    type_text("📍 현재 위치: 게이트 A (출구)")
    type_text("거대한 방폭문이 당신의 탈출을 막고 있습니다. 카드 리더기가 붉은 빛을 냅니다.")
    
    if "3등급 키카드" in player_data["inventory"]:
        type_text("인벤토리에서 '3등급 키카드'를 꺼내 리더기에 긁습니다.")
        time.sleep(1)
        type_text("삐빅- [접근 승인]")
        type_text("방폭문이 열리며 바깥의 햇살이 들어옵니다. 당신은 무사히 살아남았습니다!")
        return "엔딩"
    else:
        type_text("단말기에 [3등급 권한 필요]라고 적혀 있습니다. 문을 열 수 없습니다.")
        type_text("어디선가 끔찍한 괴성이 들려옵니다... 결국 시설 안에 갇히고 말았습니다.")
        player_data["hp"] = 0
        return "사망"
