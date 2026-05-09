from utils import type_text, print_line
from player import player_data
import rooms

def main():
    rooms.intro()
    
    while player_data["hp"] > 0:
        if player_data["location"] == "D계급 감방":
            player_data["location"] = rooms.room_d_class()
        elif player_data["location"] == "관리실":
            player_data["location"] = rooms.room_admin()
        elif player_data["location"] == "제1격리구역":
            player_data["location"] = rooms.room_containment_1()
        elif player_data["location"] == "무기고":
            player_data["location"] = rooms.room_armory()
        elif player_data["location"] == "게이트A":
            player_data["location"] = rooms.room_gate_a()
            
        # 게임 종료 조건
        if player_data["location"] == "사망":
            print_line()
            type_text("💀 게임 오버 💀")
            break
        elif player_data["location"] == "엔딩":
            print_line()
            type_text("🎉 축하합니다! 시설 탈출에 성공했습니다. 🎉")
            break

if __name__ == "__main__":
    main()
