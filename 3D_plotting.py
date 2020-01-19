# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 12:32:58 2020

@author: Dea
"""
#import modules 
import numpy as np
import random
import matplotlib.pyplot as plt
import tkinter as tk


#set equation here
def f(x, y):
    #return np.sin(np.sqrt(x ** 2 + y ** 2))
    #return y*np.exp(-x)
    #return (x-y)/(np.exp(x*y))
    #return (np.sin(x*y))/(x**2 + y**2)
    #return x**2 - y + 3
    return y*np.sin(x*y) + x*(y**2)


x = np.linspace(-10, 10, 30)
y = np.linspace(-10, 10, 30)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

def random_graph(): 
    colors = ['viridis', 'plasma', 'inferno',
                'magma', 'cividis','Greys', 
                'Purples', 'Blues', 'Greens',
                'Oranges', 'Reds',
                'YlOrBr', 'YlOrRd', 'OrRd', 
                'PuRd', 'RdPu', 'BuPu',
                'GnBu', 'PuBu', 'YlGnBu', 
                'PuBuGn', 'BuGn', 'YlGn', 'binary', 
                'gist_yarg', 'gist_gray', 'gray', 'bone', 
                'pink','spring', 'summer', 'autumn', 'winter', 
                'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper']
    color = random.choice(colors)
    return color

#Surface Plot 
def surface_plot(): 
    color = random_graph()
    fig = plt.figure(figsize=(20,10))
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=color, edgecolor='black')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(color)
    
#Contour Plot
def contour_plot():
    color = random_graph()
    fig = plt.figure(figsize=(20,10))
    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap=color)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(color)
    
#GUI component 
if __name__ == '__main__':
    m = tk.Tk() 
    m.configure(background='white')
    
    m.title('MATH 119 Graphing Visualization')
    label = tk.Label(m,bg='white', text="Please make sure that you've inputted" +  
                     " your desired equation under the def(x,y) function!" + 
                     "\nIf not, then exit this window\n").pack()
    button = tk.Button(m, activeforeground='white', 
                       activebackground='cyan', text="Random Surface Plot", 
                       command=surface_plot).pack() 
    button2 = tk.Button(m, activeforeground = 'white',
                        activebackground = 'blue', text="Random Contour Plot", 
                        command=contour_plot).pack()
    l = tk.Label(m, bg='white', text="\n\nNote your graph will appear in a seperate window").pack()
    
    m.mainloop()