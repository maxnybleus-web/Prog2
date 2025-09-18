""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc
import numpy as np

def approximate_pi(n): # Ex1
    #n is the number of points

    points = [(random.uniform(-1,1), random.uniform(-1,1)) for i in range(n)]          

   
    
    
    d = list(map(lambda p: p[0]**2 + p[1]**2, points)) # calcs all distances
    n_c = list(filter(lambda t: t <= 1, d)) # calcs all inside the circle
    pi = 4* len(n_c)/len(points)
    print(f'The approximative value of pi based on {n} points is: {pi}')

    # plotting the elements 
    
    points_circle = list(filter(lambda p: p[0]**2 + p[1]**2 <= 1, points))

    points_circle_x, points_circle_y = map(list,zip(*points_circle)) if points_circle else ([], [])

    points_outside = list(filter(lambda p: p[0]**2 + p[1]**2 >= 1, points))
   
    points_outside_x, points_outside_y = map(list,zip(*points_outside)) if points_circle else ([], [])
    
    #plt.scatter(points_circle_x, points_circle_y, color = 'red', s = 15)
    #plt.scatter(points_outside_x, points_outside_y, color = 'blue', s = 15)

    #plt.xlim(-1,1)
    #plt.ylim(-1,1)
    #plt.gca().set_aspect('equal')
    #plt.show()

    
    return pi

def sphere_volume(n, d): #Ex2, approximation


    
    zero_vector = [np.array([random.uniform(-1,1) for _ in range (d)]) for _ in range(n)]
    #print(type(zero_vector))
    
    points_inside = np.array(list(filter(lambda p: np.sum(p**2) <=1, zero_vector)))
    
    volume_sphere = len(points_inside)/ n * (2**d)

    return(volume_sphere)



     

def hypersphere_exact(d): #Ex2, real value
    
    # d is the number of dimensions of the sphere 
    volume = np.pi**(d/2) / (m.gamma(d/2 +1)) 
    return volume
    
    
    return

#Ex3: parallel code - parallelize for loop

def dummy(args): # can I do this any other way? Was the only way I found to work
    n, d = args
    return sphere_volume(n, d)

def sphere_volume_parallel1(n,d,np=10):

    p = [(n, d) for _ in range(np)]

    with future.ProcessPoolExecutor() as ex:
         
         results = list(ex.map(dummy, p))
    
    
    
    return sum(list(results))/np
    

         
    #n is the number of points
    # d is the number of dimensions of the sphere
    pass
    #np is the number of processes

#Ex4: parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np=10):

    p = [(n//np, d) for _  in range(np)]
    

    with future.ProcessPoolExecutor() as ex:
         total_points = list(ex.map(dummy, p))
    

    return mean(total_points)
    
    
   
   
    #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes


    return 
    
def main():
    #Ex1
    #dots = [1000, 10000]
    #for n in dots:
    #    approximate_pi(n)
    #print(approximate_pi(10))

    #print(sphere_volume(100000,4))
    #print(hypersphere_exact(4))

 #Ex2
 
    #n = 100000
    #d = 2
    #sphere_volume(n,d)
    #print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #n = 100000
    #d = 11
    #sphere_volume(n,d)
    #print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
  """   n = 100000
    d = 11
    start = pc()
    for y in range (10):
        sphere_volume(n,d)
    stop = pc()
    print(f"Ex3: Sequential time of {d} and {n}: {stop-start}s")
    print("What is parallel time?")
    start2 = pc()
    sphere_volume_parallel1(n,d)
    stop2 = pc()
    print(f'Parallell time of {d} and {n}: {stop2-start2}s') """


  start3 = pc()
  print(sphere_volume_parallel2(10**6, 11, 10))
  stop3 = pc()
  print(stop3-start3)


"""     #Ex4
    n = 1000000
    d = 11
    start = pc()
    sphere_volume(n,d)
    stop = pc()
    print(f"Ex4: Sequential time of {d} and {n}: {stop-start}")
    print("What is parallel time?")
 """
    


if __name__ == '__main__':
	main()
