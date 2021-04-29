import joblib
class Carevaluator:
    def __init__(self):
        '''initialising constructor'''
        self.mapperlist=[] # it will store mapping dictionaries
        self.mapped=[] # it will store inputs after mapping
    def map(self):

     '''maps categorical variable to numeric values'''

     buying={'high':0,'low':1,'medium':2,'vhigh':3}
     maint={'high':0,'low':1,'medium':2,'vhigh':3}
     doors={'two':0,'three':1,'four':2,'4+':3}
     persons={'two':0,'four':1,'4+':2}
     lug_boot={'big':0,'medium':1,'small':2}
     saftey={'high':0,'low':1,'medium':2}
     self.mapperlist=[buying,maint,doors,persons,lug_boot,saftey]

    def inputs(self):
        '''take inputs from user'''
        features=['buying','maintenence','doors','persons','lug_boot','saftey']
        for i in range(len(features)):
           if features[i] == 'buying':
               print(f'{features[i]} cost of car is :- {list(self.mapperlist[i].keys())}')
           elif features[i] == 'maintenence':
               print(f'{features[i]} cost of car is :- {list(self.mapperlist[i].keys())}')
           elif features[i] == 'doors':
               print(f'{features[i]} in the car is :- {list(self.mapperlist[i].keys())}')
           elif features[i] == 'persons':
               print(f'{features[i]} car can have :- {list(self.mapperlist[i].keys())}')
           elif features[i] == 'lug_boot':
               print(f'size of {features[i]} of car is :- {list(self.mapperlist[i].keys())}')
           elif features[i] == 'saftey':
               print(f'{features[i]} of car is :- {list(self.mapperlist[i].keys())}')
           else:
               print('something went wrong')
           inputs = input(f'{features[i]} :')
           if inputs not in self.mapperlist[i].keys():
              while True:
               print(f'please enter input from given list {list(self.mapperlist[i].keys())}')
               inputs = input(f'{features[i]} :')
               if inputs in self.mapperlist[i].keys():
                break
           self.mapped.append(self.mapperlist[i][inputs])
           continue

    def result(self):
        '''evaluate and show predicted result'''
        model=joblib.load('car_model.joblib') #importing ML model
        classes=['acceptable','good','unacceptable','very good']
        predictions=model.predict([self.mapped])
        for x in predictions:
            print(f'The car is  {classes[x]}')
        exit()


if __name__ == '__main__':
    evaluation=Carevaluator() # creating object of a class
    evaluation.map()
    evaluation.inputs()
    evaluation.result()

        
        








