from math import sin , cos
import numpy as np
import matplotlib.pyplot as plt
angle_set=np.linspace(0,89,10)
us=0.60
uk=0.40
g=9.81
m=10.0
force=m*g*np.sin(np.radians(angle_set))
#angle=30

friction1=m*g*us*np.cos(np.radians(angle_set))
yatayforce = m * g * np.sin(np.radians(angle_set))
friction_kinetic = m * g * uk * np.cos(np.radians(angle_set))



final_friction=np.where(force<friction1,force,friction_kinetic)

print(yatayforce)
print(final_friction)

if np.any(yatayforce>final_friction):   #burada cismin hareket edip etmeyeceğini kontrol ediyoruz
    print("The object will move.", np.where(yatayforce>final_friction)[0])

plt.plot( yatayforce,final_friction)
plt.show()
