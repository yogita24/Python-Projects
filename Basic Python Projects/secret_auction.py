##import os
##bidcontinue="Yes"
##bidders={}
##def clear():
##    _=os.system('cls')
##    
##while bidcontinue=="Yes":
##      print()
##      name=input("Bidder's Name:").title()
##      bid=int(input("Bid amount"))
##      bidders[name]=bid
##      bidcontinue=input("\nAre there any more bidders?(Yes/No)").title()
##      clear()
##
##s=sorted(bidders.items(),key=lambda x:x[1], reverse=True)
##print("\nWinner is %s with bid amount Rs. %d"%(s[0][0],s[0][1]))
##      
##a='''hi
##preeta
##i missed you'''
##print(a)
journal={
    'travel_log':{
        'country':'France',
        'no-of_visits':2,
        'cities':['Paris','Germany','London']},
    'Po;itics':
    {
        'PM':'Narendra Modi',
        'Plans':["education",'poverty','globalisation'],
        'years':5}}
for i in journal['travel_log']:
    print(f"{i}:{journal['travel_log'][i]}")
