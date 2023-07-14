last=eval(input("Enter The Last Limit For Fibonaci :"))
print("Do you want to start fibonacci with 0 [Y/N]c:")
switch=input("Enter :")
series=[]
def fibonaci(last) :
        prev=0
        current=1
        while current <= last :
            series.append(current)
            next=current+prev
            prev=current
            current=next
        print(series,)

if switch == "N" :
    fibonaci(last)
if switch == 'Y' :
    series.append(0)
    fibonaci(last)


    
