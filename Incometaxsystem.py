display="""
           Sunway College Account Department
                MaitiDevi, Kathmandu
           Welcome to Salary& Tax Calculate System (STCS)"""

# For display the name of the system.
def display_Static_Info():
    print(display)

Staff_No=[]
address=[]
panNo=[]
status=[]
fiscalYear=[]
incomePerMonth=[]

#For inputing the information
def Staff_Info():
    n=int(input("Please enter the number of staff you wanted to provide data"))
    for i in range(n):
        print(f"Enter for the staff [{i + 1}]")
        Staff_No.append(input(f"Enter Staff Name [{i+1}]"))
        address.append(input(f"Enter Address [{i+1}] "))
        panNo.append(input(f"Enter Pan No [{i+ 1}]"))
        status.append(input(f"Enter 'Y' for Married and 'N' for Unmarried Status[{i+1}]"))
        fiscalYear.append(input(f"Enter FY[{i + 1 }]"))
        incomePerMonth.append(int(input(f"Enter Staff per month income Rs [{ i + 1}]")))
        display_Static_Info()
        taxPercent,taxAmount,incomeAfterTax=Calculate_Tax_Of_Staff(status,incomePerMonth[i])
        display_Staff_Info(Staff_No[i],address[i],panNo[i],status[i],fiscalYear[i],incomePerMonth[i],taxPercent,taxAmount,incomeAfterTax)

def Calculate_Tax_Of_Staff(status,income):
    flag=None
    if status=='Y':
        flag=1
    
    elif status=='N':
        flag=0
    taxPercent=0
    taxAmount=0
    incomeAfterTax=0
    if(flag):
       taxPercent,taxAmount,incomeAfterTax=Calculate_Tax_Of_Staff_Married(income)
       return taxPercent,taxAmount,incomeAfterTax
    else:
       taxPercent,taxAmount,incomeAfterTax=Calculate_Tax_Of_Staff_Unmarried(income)
       return taxPercent,taxAmount,incomeAfterTax


def Calculate_Tax_Of_Staff_Married(income):
  taxPercent=0
  taxAmount=0
  incomeAfterTax=0
  if(income<=450000):
    taxPercent=1
    taxAmount=1/ 100 *(income)
    incomeAfterTax= income - taxAmount
  
  elif(income> 450000 and income<=550000):
    taxPercent=10
    extra=income - 450000
    taxAmount= 10 / 100 * (extra) + 1 / 100 * 450000
    incomeAfterTax= income - taxAmount

  elif(income>550000 and income <=750000):
    taxPercent=20
    extra=income - 550000
    taxAmount=  (10/100 * (100000)) + (1/100 *(450000)) + (20/100 * (extra))
    incomeAfterTax=income - taxAmount
  
  elif(income>750000 and income<=2000000):
    taxPercent=30
    extra= income - 750000
    taxAmount= (10/100 *(100000)) + (1/100 *(450000))+ (20/100 *(200000)) + (30/100 * (extra))
    incomeAfterTax=income - taxAmount

  elif(income>2000000):
    taxPercent= 36
    extra=income - 2000000
    taxAmount=(10/100 *(100000)) + (1/100 *(450000))+ (20/100 *(200000)) + (30/100 * (1250000)) + (36/100 * (extra))

  return taxPercent,taxAmount, incomeAfterTax

#Finishing later
def Calculate_Tax_Of_Staff_Unmarried(income):
  taxPercent=0
  taxAmount=0
  incomeAfterTax=0
  if(income<=400000):
    taxPercent=1
    taxAmount=1/ 100 *(income)
    incomeAfterTax= income - taxAmount
  
  elif(income> 400000 and income<=500000):
    taxPercent=10
    extra=income - 400000
    taxAmount= 10 / 100 * (extra) + 1 / 100 * 400000
    incomeAfterTax= income - taxAmount

  elif(income>500000 and income <=750000):
    taxPercent=20
    extra=income - 500000
    taxAmount=  (10/100 * (100000)) + (1/100 *(400000)) + (20/100 * (extra))
    incomeAfterTax=income - taxAmount
  
  elif(income>700000 and income<=2000000):
    taxPercent=30
    extra= income - 700000
    taxAmount= (10/100 *(100000)) + (1/100 *(400000))+ (20/100 *(200000)) + (30/100 * (extra))
    incomeAfterTax=income - taxAmount

  elif(income>2000000):
    taxPercent=36
    extra=income - 2000000
    taxAmount=(10/100 *(100000)) + (1/100 *(450000))+ (20/100 *(200000)) + (30/100 * (1250000)) + (36/100 * (extra))

  return taxPercent,taxAmount, incomeAfterTax
   

def display_Staff_Info(name,address,panNo,status,fiscalyear,income,taxPercent,taxAmount,incomeAfterTax):
    print("Staff name:{0}               Address:{1}".format(name,address))
    print("PAN NO: {p}      FY: {q}      Married Status={r}".format(p=panNo,q=fiscalyear,r=status))
    print("Income:"+str(income))
    print("Staff {a} with PAN {b} fall under {c}% Tax salb.".format(a=name,b=panNo,c=taxPercent))
    print("{a}  ({b}) to pay the government is [Rs.]= {c}".format(a=name,b=panNo,c=taxAmount))
    #Writing down in the file
    lines=["Name:"+name,"Address:" +address ,"PanNo" + panNo,"Status"+status,"Fiscalyear"+fiscalyear,"Income before tax:"+
     str(income)+ "Tax Amount:" +str(taxAmount), "Income after tax:"+ str(incomeAfterTax)]
    with open('C:/Users/dipes/Desktop/information.txt','a') as f:
     for line in lines:
      f.write(line)
      f.write('\n')

    print("Sucessfully written on the file")

Staff_Info()
    
