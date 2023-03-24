Username = input("Please input your Username : ") 
Password = input("Please input your Password : ")
productprice1 = 10 
productprice2 = 35
productprice3  = 50
productprice4  = 45
if Username == "Customer" and Password == "12345" :
   print("Welcome to Happy shop product selection system")
   print("----------------------")
   print("1 . Apple     10 THB")
   print("2 . Bread     35 THB")
   print("3 . Cake      50 THB")
   print("4 . Fish      45 THB")
   print("----------------------")
   select = input("Please specify the desired product : ")
   if  select == "Apple":
        total1 = int(input("Please specify the number of products required : "))
        print("Total : ", total1*productprice1 , "THB")
        print("-------------Thank You-------------")
   elif select == "Bread":
        total2 = int(input("Please specify the number of products required : "))
        print("Total : ", total2*productprice2 , "THB")
        print("-------------Thank You-------------")
   elif select == "Cake":
        total3 = int(input("Please specify the number of products required : "))
        print("Total : ", total3*productprice3 , "THB")
        print("-------------Thank You-------------")
   elif select == "Fish":
        total4 = int(input("Please specify the number of products required : "))
        print("Total : ", total4*productprice4 , "THB")
        print("-------------Thank You-------------")
else:
    print("sorry please try again ") 
