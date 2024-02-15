## 10. Skriv ett program som beräknar medelvärde och standardavvikelse hos en numerisk lista:

import numpy as np 
#import pandas as pd
#import pyarrow
import random 
import trigo

num_list = [8.95, 7.82, 9.25, 8.62, 7.03, 8.77, 8.69, 6.49, 6.38, 6.01, 8.92, 9.64, 5.76, 8.84, 6.92, 6.2]

"""for i in range(0, 16):
    num_list.append(round(random.uniform(5.56, 9.72), 2))
    i+=1"""

print("Datamängd: ", num_list)

print("Varians för datamängd: ", round(np.var(num_list), 2))
print("Standardavvikelse för datamängd: ", round(np.std(num_list), 2))
print("Medelvärde: ", round(np.mean(num_list), 2))

x_2bar = np.mean(num_list)

print(trigo.area_square(3, 4))
print(trigo.circumference_circle(3.7))
print(trigo.area_triangle(5, 7))