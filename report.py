marks = [ ]

for i in range(5):
 mark = int(input(f"Enter marks of student{i+1}: "))
 marks.append(mark)

print("\n^^^^^^^^^^Report Card^^^^^^^^^^")

for i in range(5):
 if marks[i] >= 90:
   grade = "A+"
 elif marks[i] >= 75:
   grade = "A"
 elif marks[i] >= 60:
   grade = "B"
 elif marks[i] >= 33:
   grade = "C"
 else:
  grade = "Fail"

 print ("Student",i+1,":",marks[i],"-",grade)
