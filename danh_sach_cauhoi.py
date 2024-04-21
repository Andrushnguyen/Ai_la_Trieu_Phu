import json
cau_hoi= {
    'diem': 0,

    'list': [
        {
            'cauhoi':'Cái nào SAU ĐÂY KHÔNG PHẢI là một màu cơ bản?',
            'answer1':"A. Đỏ",
            'answer2':"B. Vàng",
            'answer3':"C. Xanh lá cây ",
            'answer4':"D. Tím",
            'correct_answer': "Dd"
        },
        {
            'cauhoi':'Thủ đô của nước Pháp là gì?',
            'answer1':"A. London (Luân Đôn)",
            'answer2':"B. Berlin (Béc-lin)",
            'answer3':"C. Paris (Pa-ri)",
            'answer4':"D. Rome (Rô-ma)",
            'correct_answer': "Cc"
        },
        {
            'cauhoi':'Hành tinh nào SAU ĐÂY là hành tinh lớn nhất trong hệ mặt trời của chúng ta?',
            'answer1':"A. Trái Đất",
            'answer2':"B. Sao Hỏa",
            'answer3':"C. Sao Mộc",
            'answer4':"D. Sao Kim",
            'correct_answer': "Cc"
        },
        {
            'cauhoi':'Tên khoa học của chó là gì?',
            'answer1':"AA. Felis catus (Mèo)",
            'answer2':"B. Canis lupus familiaris",
            'answer3':"C. Equus caballus (Ngựa)",
            'answer4':"D. Panthera leo (Sư tử)",
            'correct_answer': "Bb"
        }
        

    ]
}

with open("cau_hoi.json", "w") as f:
    json.dump(cau_hoi, f)