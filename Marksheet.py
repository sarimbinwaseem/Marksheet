maths = int(input("Enter Mathamatics marks: "))
phy = int(input("Enter Physics marks: "))
comp = int(input("Enter Computer marks: "))
urdu = int(input("Enter Urdu marks: "))
eng = int(input("Enter English marks: "))

per = ((maths + phy + comp + urdu + eng)/500)*100
print("============================================")

print("Your percentage is:", per)
print("--------------------------------------------")
if per < 60:
	print("You are fail..!!")
elif per <= 70:
	print("Grade: \"B\"")
elif per < 80:
	print("Grade: \"A\"")
elif per < 90:
	print("Grade: \"A+\"")
print("")
print("")
print("End of Result..")
