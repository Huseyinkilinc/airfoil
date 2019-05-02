# -*- coding: utf-8 -*-
"""
Created on Thu May  2 12:40:31 2019

@author: s140121038
"""

def open_airfoil_file(filename):
    
    data=np.loadtxt(filename,skiprows=1)
    x = data[:,0] 
    y= data[:,1] 

    plt.plot(x,y,'-')
    plt.axes().set_aspect(1,'datalim')
    plt.title('Airfoil '+ filename)

    return x,y

x,y=open_airfoil_file('a18.dat')
def plot_chordline(x,y):
    lp = len(x)//2 #leading edge x point
    tep = len(x) # trailing edge x point
    clx=x[lp:tep]
    slope=(y[lp]-y[tep-1])/len(clx) #slope of leading and trailing edge
    cly=[y[lp]]*len(clx)
        
    for i in range (1,len(cly)):
        cly[i]=cly[i]-i*slope
        
    
    plt.plot(clx,cly,'--',color='black')
    return slope

plot_chordline(x,y)

def plot_meanline():
        
        t=(len(x)//2)
        x_upper=x[:t] #upper surface x points
        x_lower=x[t+1:] #lower surface x points
        y_upper=y[:t] #upper surface y points
        y_lower=y[t+1:] #lower surface y points
        ml=[]  #mean line
        x_point = []  
        thickness=[] 
        for i in range (t):    
            ml =ml + [(y_upper[i]+y_lower[-i-1])/2]
        
        plt.plot(x[:t],ml,'-',color='black')
        k=0
        for i in range(t):
            if ml[i-1]<ml[i]:
        
                k=k+1
        x_point=[x_upper[k]]*2
        thickness = thickness + [y_upper[k]] +[y_lower[-k-1]]
        plt.plot(x_point,thickness,'-',color='blue') #maximum thickness
        return ml
plot_meanline()