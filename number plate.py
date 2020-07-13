print("Enter the last four numbers on you Plate: ")
num = input()
if len(num) == 4:
    nume = " ".join(num)
    a1, a2, a3, a4 = nume.split()
    if a1.isdigit() and a2.isdigit() and a3.isdigit() and a4.isdigit() :
        a1 = int(a1)
        a2 = int(a1)
        a3 = int(a1)
        a4 = int(a1)
        sum = a1+ a2 + a3 + a4
        sum = str(sum)
        if len(sum) == 1:
            print(sum)
        elif len(sum) == 2:
            sume = " ".join(sum)
            b1, b2 = sume.split()
            b1 = int(b1)
            b2 = int(b2)
            answer = b1 + b2
            print(answer)
        else:
            print("Invalid Input")
    else:
        print("Enter only numbers!")
else:
    print("Input the last 4 numbers correctly!")
            
        
