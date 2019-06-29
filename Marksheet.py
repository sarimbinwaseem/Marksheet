import csv

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
	grade = "You are fail..!!"
elif per <= 70:
	grade = "\"B\""
elif per < 80:
	grade = "\"A\""
elif per < 90:
	grade = "\"A+\""
print("")
print("")
print("End of Result..")

marksheet = open("marksheet.txt","w") 
 
marksheet.write("Marks of Mathematics:")
marksheet.write(str(maths) + "\n") 
marksheet.write("Marks of Physics:") 
marksheet.write(str(phy) + "\n")
marksheet.write("Marks of Computer:") 
marksheet.write(str(comp) + "\n")
marksheet.write("Marks of Urdu:") 
marksheet.write(str(urdu) + "\n")
marksheet.write("Marks of English:")
marksheet.write(str(eng) + "\n \n")
marksheet.write("Percentage:")
marksheet.write(str(per) + "%"+ "\n \n")
marksheet.write("Grade:")
marksheet.write(str(grade) + "\n")

marksheet.close() 

