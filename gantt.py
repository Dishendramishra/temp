#%%
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
import numpy as np
plt.style.use('default')

#%%
processes = [21,3,6,2]
# rrb_time = 5

# wait_times = np.zeros(len(processes))
# service_times = np.zeros(len(processes))

# tags = [ "P"+str(i) for i in range(1,len(processes)+1)] 


# timer = 0

# while True:

#     for i,v in enumerate(processes):
#         if v >0:
#             processes[i] -= rrb_time
#             wait_times[i] = timer-service_times[i]


#     print(wait_times)
#     print(processes)
#     print()

#     if sum(processes)<=0:
#         break
         


plt.figure()
currentAxis = plt.gca()
xlim = sum(processes)+2
currentAxis.set_xlim([-1,xlim])
currentAxis.set_ylim([1,4])

ref = 0

xticks = []
for i,x in enumerate(processes):
    currentAxis.add_patch(Rectangle((ref, 1), x, 1, fill=None, alpha=1))
    currentAxis.annotate(tags[i], (ref+x/2.0, 1.5), color='black', weight='bold', 
                fontsize=10, ha='center', va='center')
    xticks.append(ref)
    ref += x
xticks.append(ref)

np.average

plt.xticks(xticks)
plt.yticks([])

plt.show()