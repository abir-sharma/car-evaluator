import joblib
model=joblib.load('car_model.joblib')
buying={'high':0,'low':1,'medium':2,'vhigh':3}
maint={'high':0,'low':1,'medium':2,'vhigh':3}
doors={'two':0,'three':1,'four':2,'4+':3}
persons={'two':0,'four':1,'4+':2}
lug_boot={'big':0,'medium':1,'small':2}
saftey={'high':0,'low':1,'medium':2}
classes=['acceptable','good','unacceptable','very good']
mapperlist=[buying,maint,doors,persons,lug_boot,saftey]
features=['buying','maintenence','doors','persons','lug_boot','saftey']
mapped=[]
for i in range(len(features)):
    if features[i] == 'buying':
       print(f'{features[i]} cost of car is :- {list(mapperlist[i].keys())}')
    elif features[i] == 'maintenence':
        print(f'{features[i]} cost of car is :- {list(mapperlist[i].keys())}')
    elif features[i] == 'doors':
        print(f'{features[i]} in the car is :- {list(mapperlist[i].keys())}')
    elif features[i] == 'persons':
        print(f'{features[i]} car can have :- {list(mapperlist[i].keys())}')
    elif features[i] == 'lug_boot':
        print(f'size of {features[i]} of car is :- {list(mapperlist[i].keys())}')
    elif features[i] == 'saftey':
        print(f'{features[i]} of car is :- {list(mapperlist[i].keys())}')
    else:
        print('something went wrong')
    inputs = input(f'{features[i]} :')
    if inputs not in mapperlist[i].keys():
        while True:
            print(f'please enter input from given list {list(mapperlist[i].keys())}')
            inputs = input(f'{features[i]} :')
            if inputs in mapperlist[i].keys():
                break
    mapped.append(mapperlist[i][inputs])
    continue
predictions=model.predict([mapped])
for x in predictions:
    print(f'The car is  {classes[x]}')






