#tính can chi

"""phân tích đề
nhập năm theo bàn phím
tính can theo công thức
tính chi theo công thức
trả kết qủa bằng print (can + chi)

Option 1: viết thủ công nhất"""

cal_can_chi = int(input())
if type(cal_can_chi) != int:
    print ("Mời nhập số:")

# tính Can
cal_can = cal_can_chi % 10
if cal_can == 0:
    Can = "Canh"
elif cal_can == 1:
    Can = "Tân"
elif cal_can == 2:
    Can = "Nhâm"
elif cal_can == 3:
    Can = "Quý"
elif cal_can == 4:
    Can = "Giáp"
elif cal_can == 5:
    Can = "Ất"
elif cal_can == 6:
    Can = "Bính"
elif cal_can == 7:
    Can = "Đinh"
elif cal_can == 8:
    Can = "Mậu"
elif cal_can == 9:
    Can = "Kỷ"

# tính Chi
cal_chi = cal_can_chi % 12
if cal_chi == 0:
    Chi = "Thân"
elif cal_chi == 1:
    Chi = "Dậu"
elif cal_chi == 2:
    Chi = "Tuất"
elif cal_chi == 3:
    Chi = "Hợi"
elif cal_chi == 4:
    Chi = "Tý"
elif cal_chi == 5:
    Chi = "Sửu"
elif cal_chi == 6:
    Chi = "Dần"
elif cal_chi == 7:
    Chi = "Ngọ"
elif cal_chi == 8:
    Chi = "Mẹo"
elif cal_chi == 9:
    Chi = "Thìn"
elif cal_chi == 10:
    Chi = "Tỵ"
elif cal_chi == 11:
    Chi = "Mùi"


print ("Can Chi năm", cal_can_chi, "là:", Can + " "+ Chi)