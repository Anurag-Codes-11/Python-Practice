x = int(input("Enter the mark of the student: "))
if (85<=x and x<= 100):
    print("Grade A")
if (60<=x and x<= 85):
    print("Grade B")
if (40<=x and x<= 60):
    print("Grade C")
if (x>100 or x<0):
    print("Invalid mark")