examscore  = int(input("score of the exam: "))
attended_classes = int(input("Classes attended: "))
total_classes = 40
Z = attended_classes/total_classes * 100
if examscore >= 70 and Z>= 80:
    print("Pass")
else:
    print("Fail")
