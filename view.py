def fractue(request):
    if(request.method=="POST"):
        data=request.POST
        pclass=data.get('textpclass')
        age=data.get('textage')
        sex=data.get('textsex')
        weight=data.get('textweight')
        height=data.get('textweight')
        medication=data.get('textmedication')
        waitingtime=data.get('textwaiting')
        bmd=data.get('textbmd')
        if('buttonpredict' in request.POST):
            import pandas as pd
            path="C:\\Users\\Sakshi\\Desktop\\Machine Learning\\Data\\Data\\bmd.csv"
            data=pd.read_csv(path)
            #print(data)
            #print(data.info())

            data['sex']=data['sex'].map({'M':1,'F':0})
            #print(data)

            data['medication']=data['medication'].map({'Anticonvulsant':1,'No medication':2,'Glucocorticoids':3})
            #print(data)

            #data['fracture']=data['fracture'].map({'fracture':1,'no fracture':0})
            #print(data)


            inputs=data.drop(['fracture'],'columns')
            output=data.drop(['id','age','sex','weight_kg','height_cm','medication','waiting_time','bmd'],'columns')

            import sklearn
            from sklearn.model_selection import train_test_split
            x_train,x_test,y_train,y_test=train_test_split(inputs,output,train_size=0.8)
            #print(x_train)
            #print(x_test)
            #print(y_train)
            #print(y_test)

            from sklearn.naive_bayes import GaussianNB
            model=GaussianNB()
            model.fit(x_train,y_train)
            y_pred=model.predict(x_test)
            #print(y_pred)
            #print(y_test)

            
            result=model.predict([[int(pclass),float(age),int(sex),int(weight),float(height),int(medication),int(waitingtime),float(bmd)]])
            print(result)


            if result==1:
             
               print("The person have Fracture")
            else:
                print("The person have no fracture")
            return render(request,'fractue.html',context={'result':result})
        
    return render(request,'fractue.html')