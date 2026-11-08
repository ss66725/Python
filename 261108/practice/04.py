def waterCharges(waterType,waterAmount):
    charge = 0
    single = 0

    if waterType == 1 :
        if waterAmount <= 22 :
            single = 2.12
            charge = single * waterAmount
        elif 22 < waterAmount < 31:
            single = 4.27
            charge = (22 * 2.12) + (single * (waterAmount - 22))
        else:
            single = 4.42
            charge = (22 * 2.12) + (8 * 4.27) + (single* (waterAmount - 30))
        
    elif waterType == 2 :
        if waterAmount <=5:
            single = 2.12
            charge = single * waterAmount
        elif 5 < waterAmount <8:
            single = 3.27
            charge = (5 * 2.12) + single * ((waterAmount - 5))
        else:
            single = 4.42
            charge = (5 * 2.12) + (2 * 3.27) + (single * (waterAmount - 7))

    else:
        print("False")
        
    return charge

waterType_string = input("请输入用水类别：1-家庭户，2-集体户（输入1或2）：")
waterType = int(waterType_string)
waterAmount_string = input("请输入如用水量（吨）：")
waterAmount = float(waterAmount_string)
fee = waterCharges(waterType,waterAmount)
print(f"请交水费{fee}元")