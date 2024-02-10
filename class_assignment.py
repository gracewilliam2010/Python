class allinone():
    def Subfields():
        print("Sub-fields in AI are:")
        list=['Machine Learning', 'Neural Networks', 'Vision', 'Robotics', 'Speech Processing', 'Natural Language Processing']
        for i in list:
            print(i)
            
           
               
    def elegibility():
        num = int(input("Enter a age: "))
        gender = input("Enter a Gender: ")
        if (num >= 21 and gender=='male'):
            print("Eligible for marriage")
        elif (num >= 18 and gender=='female'):
            print("Eligible for marriage")
        else:  
            print("not eligible")       
            
    def percentage():
        subject1=int(input("subject1="))
        subject2=int(input("subject2="))
        subject3=int(input("subject3="))
        subject4=int(input("subject4="))
        subject5=int(input("subject5="))
    
        Total=int(subject1+subject2+subject3+subject4+subject5)
        Percentage = (Total / 500) * 100
        print("Total",Total)
        print("Percentage:",Percentage)   
        
    def triangle():
        Height=int(input("Height="))
        Breadth=int(input("Breadth="))
        print("Area formula: (Height*Breadth)/2")
        areat =( Height * Breadth ) / 2
        print("Area of Triangle:", areat)
        Height1=int(input("Height1="))
        Height2=int(input("Height2="))
        Breadth=int(input("Breadth="))
        Perimeter=Height1+Height2+Breadth
        print("Perimeter of Triangle:",Perimeter) 
        
    
        
        