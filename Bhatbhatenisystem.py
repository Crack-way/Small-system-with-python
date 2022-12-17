#  Author:Rupesh Sunuwar
    #  Semester :4th
def initialDisplay():
    display=""" Sunway Bhatbhateni Store  """
    print(display)

#displaying the information
initialDisplay()

#For inputing customer information
def inputInformation():
    name=[]
    address=[]
    email=[]
    itemName=[]
    itemQuantity=[]
    itemPrice=[]
    a=int(input("Enter a number of customer."))
    for x in range(a):
     totalPrice=0
     name.append(input(f"Enter name of [{ x + 1} ] customer"))
     address.append(input(f"Enter address of [{x + 1}] customer"))
     email.append(input(f"Enter email of [{ x+ 1 }] customer"))
     n=int(input("Enter no of item list."))
     for y in range(n):
        itemName.append(input(f"Name of item [{y +1 }]"))
        itemQuantity.append(int(input(f"Quantity of the item [{ y + 1}]")))
        itemPrice.append(int(input(f"Price of item [{ y + 1}]")))
        totalPrice=totalPrice + ( itemQuantity[y]  * itemPrice[y])
        discountAmount,netAmount=calculation(totalPrice)
        displayInformation(name[x],address[x],email[x],totalPrice,discountAmount,netAmount)

#For calculating discount and net Amount
def calculation(totalPrice):
    discountAmount=0
    netAmount=0
    if(totalPrice>10000):
        discountAmount= 15 / 100 * totalPrice 
        netAmount = totalPrice - discountAmount

    elif(totalPrice<=10000 and totalPrice > 70000):
        discountAmount = 10/100 * totalPrice
        netAmount= totalPrice - discountAmount

    elif(totalPrice <=7000 and totalPrice>50000):
        discountAmount= 8 / 100 * totalPrice
        netAmount= totalPrice - discountAmount
    else:
        discountAmount= 5 / 100 * totalPrice
        netAmount = totalPrice - discountAmount

    return discountAmount , netAmount

#For Displaying Customer Information 
def displayInformation(name,address,email,totalPrice,discountAmount,netAmount):
  print("Name: " + name)
  print("Address: "+ address)
  print("Email "+ email)
  print("TotalPrice "+str(totalPrice))
  print("DiscountAmount "+str(discountAmount))
  print("Net Amount "+ str(netAmount)) 
  lines=["Name:"+name,"Address:" + address,"Email:"+email,"Totalprice:" +str(totalPrice),"Discountamount:" + str(discountAmount),"Net Amount:" +str(netAmount)]
  with open('C:/Users/dipes/CustomerInformation.txt','a') as f:
   for line in lines:
    f.write(line)
    f.write('\n')

inputInformation()