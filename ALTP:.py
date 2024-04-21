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
while True:
    cauhoi()
    n = luachon()
    if 0 < n <= 10:
       quest = cau_hoi['list'][n-1]
       print(quest["cauhoi"])
       print(quest["answer1"]+" "+quest["answer2"]+" "+quest["answer3"]+" "+quest["answer4"])
       answer = input("Chon A/a, B/b, C/c, D/d : " )
       if answer in quest['correct_answer']:
        print("Dung")
        cau_hoi['diem'] = cau_hoi['diem'] + 1
        print("Diem cua ban la: ", cau_hoi['diem'])
       else:
        print("Sai")
    else:
        print("Khong hop le, chon lai")
        continue 