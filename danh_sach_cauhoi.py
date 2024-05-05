import json
cau_hoi= {

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
            'answer1':"A. Felis catus (Mèo)",
            'answer2':"B. Canis lupus familiaris",
            'answer3':"C. Equus caballus (Ngựa)",
            'answer4':"D. Panthera leo (Sư tử)",
            'correct_answer': "Bb"
        },
        {
            'cauhoi':'Ý nghĩa của từ viết tắt HTTP là gì?',
            'answer1':"A. Giao thức Chuyển văn bản Siêu liên kết (Hyper Text Transfer Protocol)",
            'answer2':"B. Giao thức Chuyển giao Công nghệ Cao (High Tech Transfer Protocol)",
            'answer3':"C. Giao thức Chuyển văn bản Khổng lồ (Huge Text Transfer Protocol)",
            'answer4':"D. Giao thức Chuyển văn bản Vui vẻ (Happy Text Transfer Protocol)",
            'correct_answer': "Aa"
        },
        {
            'cauhoi':'Tên của đại dương lớn nhất thế giới là gì?',
            'answer1':"A. Thái Bình Dương",
            'answer2':"B. Đại Tây Dương",
            'answer3':"C. Ấn Độ Dương",
            'answer4':"D. Bắc Băng Dương",
            'correct_answer': "Aa"
        },
        {
            'cauhoi':'iPhone đầu tiên được phát hành vào năm nào?',
            'answer1':"A. 2004",
            'answer2':"B. 2007",
            'answer3':"C. 2010",
            'answer4':"D. 2013",
            'correct_answer': "Bb"
        },
        {
            'cauhoi':'Đơn vị tiền tệ của Nhật Bản là gì?',
            'answer1':"A. Euro",
            'answer2':"B. Dollar (Đô la Mỹ)",
            'answer3':"C. Yên",
            'answer4':"D. Bảng Anh (Pound Sterling)",
            'correct_answer': "Cc"
        },
        {
            'cauhoi':'Ai đã viết vở kịch nổi tiếng "Hamlet"?',
            'answer1':"A. William Shakespeare (William Sếch-xpia)",
            'answer2':"B. Charles Dickens (Charles Dicken)",
            'answer3':"C. Jane Austen (Jane Austen)",
            'answer4':"D. J.K. Rowling (J.K. Rô-lăng)",
            'correct_answer': "Aa"
        },
        {
            'cauhoi':'Núi nào là núi cao nhất thế giới?',
            'answer1':"A. Everest (Ê-vơ-rét)",
            'answer2':"B. K2",
            'answer3':"C. Kilimanjaro (Kilimanjaro)",
            'answer4':"D. Phú Sĩ",
            'correct_answer': "Aa"
        }

        

    ]
}

with open("cau_hoi.json", "w") as f:
    json.dump(cau_hoi, f)
