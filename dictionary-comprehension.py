#just like list comprehension, to filter out some values we can use dictionary comprehension

#funny name incoming
myDict = {"Shy":21,"Mith":50,"Cler":21,"Lest":20,"Rith":-10,"Fai":18}


filtered = {key:val for key,val in myDict.items() if val>=18}
#dont forget that this is a dictionary so instead of [] for list, we use {} and instead of n which takes
#only one for lists, we use key:val first and key,val second. Make sure to use.items() to get the key:val.



print (filtered)