from functools import reduce
def findPetit(tab):
    petit=tab[0]
    for i in range(len(tab)):
        if tab[i]<petit:
            petit=tab[i]
    return petit

def sort(tab):
    def findPetit(tab):
        petit=tab[0]
        for i in range(len(tab)):
            if tab[i]<petit:
                petit=tab[i]
        return petit
    tabsort=[]
    n=len(tab)
    for i in range(n):
        petit=findPetit(tab)
        tabsort.append(petit)
        tab.remove(petit)
    return tabsort

tab=[3,2,5,1,4,6]
"""print(tab)
print(sort(tab))"""


"""def printReduce(x,y):
    print(x,y)
    return 100
reduce(printReduce,[1,2,3,4,5,6])"""

def bubbleSort(tab):
    n=len(tab)
    for j in reversed(range(n)):  
        for i in range(len(tab[:j])-1):
            if(tab[i]>tab[i+1]):
                tab[i], tab[i+1] = tab[i+1],tab[i]
    print(tab)
    return tab

#bubbleSort(tab)

def insertionSort(tab):
    n=len(tab)
    print(tab)
    for i in range (1,n):
        for j in reversed(range(i)):
            print(tab[j],tab[i])
            if tab[j]>tab[i]:
                print("oui")
                insert=tab[j]
                tab[j+1:i]=tab[j:i-1]
                tab[j]=insert
            print(tab)
    print(tab)
    return tab

insertionSort(tab)
    
