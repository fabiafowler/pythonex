chem_score = int(input("Please enter your chemistry mark"))
bio_score = int(input("Please enter your physics mark"))
phy_score = int(input("Please enter your biology mark"))

if chem_score <= 40:
    print("fail")
elif bio_score <= 40:
    print("fail")
elif phy_score <= 40:
    print("fail")

elif score = (chem_score + bio_score + phy_score)/3:
    print (chem_score, "+", bio_score, "+", phy_score, "÷ 3 = ", score, "%")

if score >=70: 
    print("1st")
elif score >=60:
    print("2.1")
elif score >=50:
    print("2.2")
elif score >=40:
    print("Pass")
else:
    print("Fail")

