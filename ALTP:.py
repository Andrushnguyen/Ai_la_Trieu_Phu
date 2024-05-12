import json
try:
    with open("cau_hoi.json", "r") as f:
        cau_hoi_loaded = json.load(f)
except:
    pass
cau_hoi = cau_hoi_loaded
def cauhoi():
    print("================================")
    print("================================")
    print("Lua chon cau hoi")
    for i in range(1,11):
        print("Cau",i ,end=" ")
    print()
    print("================================")
    print("================================")
def luachon():
    n = int(input("Lua chon cau hoi: "))
    return n
def choncachchoi():
    cachchoi = int(input())
    return cachchoi
def cachchoi1():
    global diem
    quest = cau_hoi['list'][n-1]
    print(quest["cauhoi"])
    print(quest["answer1"])
    print(quest["answer2"])
    print(quest["answer3"])
    print(quest["answer4"])
    answer = input("Chon A/a, B/b, C/c, D/d : " )
    if answer in quest['correct_answer']:
       print("Dung")
       diem = diem + 2
       print("Diem cua ban la: ", diem)
    else:
       diem = diem - 1
       print("Sai", "so diem la", diem)
def cachchoi2():
    global diem
    quest = cau_hoi['list'][n-1]
    print(quest["cauhoi"])
    print(quest["answer1"])
    print(quest["answer2"])
    print(quest["answer3"])
    print(quest["answer4"])
    answer = input("Chon A/a, B/b, C/c, D/d : " )
    if answer in quest['correct_answer']:
       print("Dung")
       diem = diem + 5
       print("Diem cua ban la: ", diem)
    else:
       diem = diem - diem
       print("Sai", "so diem la", diem)
def cachchoi3():
    global diem
    quest = cau_hoi['list'][n-1]
    print(quest["cauhoi"])
    print(quest["answer1"])
    print(quest["answer2"])
    print(quest["answer3"])
    print(quest["answer4"])   
    answer = input("Chon A/a, B/b, C/c, D/d : " )
    if answer in quest['correct_answer']:
       print("Dung")
       diem = diem + 1
       print("Diem cua ban la: ", diem)
    else:
       print("Sai", "so diem la", diem)
list_cauhoi = [
    {
        'cauhoi': ch['cauhoi'],
        'answer1': ch['answer1'],
        'answer2': ch['answer2'],
        'answer3': ch['answer3'],
        'answer4': ch['answer4'],
        'correct_answer': ch['correct_answer']
    }
    for ch in cau_hoi["list"]
]
answered_questions = []
diem = 0
print("welcome to Ai La Trieu")
print("================================")

while len(answered_questions)< 2:
    print("Xin hay lua chon cach choi")
    print("================================")
    print("1. Nhan doi diem nhung bi tru diem khi tra loi sai")
    print("2. Nhan 5 diem nhung sai se mat het diem")
    print("3. Choi binh thuong")
    ncachchoi = choncachchoi()
    cauhoi()
    n = luachon()
    if n in answered_questions:
            print("Ban da tra loi cau hoi nay roi. Vui long chon cau hoi khac.")
            continue
    elif 0 < n <= 10 and ncachchoi == 1:
        cachchoi1()
        answered_questions.append(n)
    elif 0 < n <= 10 and ncachchoi == 2:
        cachchoi2()
        answered_questions.append(n)
    elif 0 < n <= 10 and ncachchoi == 3:
        cachchoi3()
        answered_questions.append(n)
    else:
        print("Khong hop le, chon lai")
        continue 
print("================================")
name = input("Nhap ten cua ban: ")
def update_leaderboard(name, diem):
    try:
        with open("leaderboard.json", "r") as f:
            user_info = json.load(f)
    except FileNotFoundError:
        user_info = {"thongtin": []}

    existing_player = None
    for player in user_info["thongtin"]:
        if player["name"] == name:
            existing_player = player
            break

    if existing_player:
        existing_player["score"] = max(existing_player["score"], score)  
    else:
        user_info["thongtin"].append({"name": name, "diem": diem})

    user_info["thongtin"].sort(key=lambda player: player["diem"], reverse=True)

    with open("leaderboard.json", "w") as f:
        json.dump(user_info, f, indent=4) 

def display_leaderboard(top_n=10):
    try:
        with open("leaderboard.json", "r") as f:
            user_info = json.load(f)
    except FileNotFoundError:
        print("Leaderboard is empty.")
        return

    print("=================== Leaderboard ===================")
    if len(user_info["thongtin"]) == 0:
        print("No players on the leaderboard yet. Play some games!")
    else:
        for i, player in enumerate(user_info["thongtin"][:top_n]):
            print(f"{i+1}. {player['name']}: {player['diem']}")
update_leaderboard(name, diem)
display_leaderboard()
