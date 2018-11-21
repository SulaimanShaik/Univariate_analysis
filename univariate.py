
# coding: utf-8

# In[ ]:


def Uni_plot(file,name,columns=[]):
    import pandas as pd
    import numpy as np
    import os
    import matplotlib.pyplot as plt
    import seaborn as sb
    file=pd.read_csv(file,index_col=0)
    
    
    if len(columns)==0:
        columns=list(file.columns)
 
    os.mkdir(name)
    os.chdir(name)
    numeric=[]
    categorical=[]
    
    
    for i in columns:
        if((np.array(file[i].unique().shape[0]>30) and file[i].dtype in ['float64','int64'])):
            numeric.append(i)
        else:
            categorical.append(i)
    
           
    for j in numeric:
        file.hist(column=j,grid=False,figsize=(8,6))
        plt.savefig(str(j)+'_hist.png')
        plt.show()   
           
           #boxplot
        file.boxplot(column=j,grid=False,figsize=(8,6))
        plt.savefig(str(j)+'_boxplot.png')
    for k in categorical:
        sb.countplot(file[k])
        plt.savefig(str(k)+'_barplot.png')
           
    os.chdir(r'C:\Users\Sulaiman\Downloads\datasets')       

