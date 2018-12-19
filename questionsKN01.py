#Questions.py - Kaylee
#init variables
q1 = """ Question 1: How old is Drake?
1) 29
2) 32
3) 30
4) 35
"""

a1= int(0)
check1 = bool(False)

#test
print(q1)

while check1 == False:
    try:
        a1 = int(input("Choose the best reponse based on your knowledge on Drake"))
        if a1 == 2:
            print("Okay Cool!") #acceptable
            score = int(score+1)
            check1 = True
        elif 0 < a1 < 5: #acceptable
            print("Got it!")
            check1 = True
        else:
            print("Please enter an integer between 0-5") #non-acceptable
    except ValueError:
        print("Um.. let's think a little harder")
        
        
