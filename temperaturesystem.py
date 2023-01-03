display= """ 
                Sunway Temperature Record Management System
                       Kathmandu Nepal
                      11 April 2022"""

def initialDisplay():
    print(display)

initialDisplay()

temperature=[]
def inputInfo():
   n=int(input("How many days to record?"))
   for i in range(n):
     temperature.append(int(input(f"Temperature day [{i+1}]")))
   
   average,hotCount,coldCount,pleasantCount=calculateTemperatureState(temperature,n)
   displayInfo(n,temperature,average,hotCount,coldCount,pleasantCount)
      
def calculateTemperatureState(temperature,n):
   
    average=0
    hotCount=0
    pleasantCount=0
    coldCount=0
    for i in range(n):
        average=temperature[i]+ average
        if(temperature[i] >85):
            hotCount = hotCount + 1

        elif(temperature[i]>=60 and temperature[i] <=85):
            pleasantCount= pleasantCount + 1
        elif(temperature[i]<60):
            coldCount = coldCount + 1
    average=average/n
    return average,hotCount,pleasantCount,coldCount

def displayInfo(n,temperature,average,hotCount,coldCount,pleasantCount):
    for i in range(n):
        if(temperature[i] >85):
            print(f"{temperature[i]} very hot.")

        elif(temperature[i]>=60 and temperature[i] <=85):
             print(f"{temperature[i]} very pleasant.")
        elif(temperature[i]<60):
             print(f"{temperature[i]} very cold.")
    print("The average Temp for 5 days={0}".format(average))
    print("The number of hot days= {0} day/s".format(hotCount))
    print("The number of pleasant days= {0} day/s".format(pleasantCount))
    print("Number of cold days={0} day/s".format(coldCount))
    

inputInfo()
    
        



