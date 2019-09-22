#%%
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
import numpy as np
plt.style.use('default')

#%%
processes = [21,3,6,2]
rrb_time = 5

# =========================================================
#              vars for calculating avg wait time
# =========================================================
wait_times = np.zeros(len(processes))
service_times = np.zeros(len(processes))
tags = [ "P"+str(i) for i in range(1,len(processes)+1)] 
timer = 0
# =========================================================


# =========================================================
#              ploting setup
# =========================================================
plt.figure()
currentAxis = plt.gca()
xlim = sum(processes)+2
currentAxis.set_xlim([-1,xlim])
currentAxis.set_ylim([1,4])
ref = 0
xticks = []
# =========================================================


while True:
    for i,time in enumerate(processes):
    
        if time >0:

            current_run_time = None

            if processes[i] >= rrb_time:
                current_run_time = rrb_time
                service_times[i] += rrb_time
                processes[i] -= rrb_time
                timer += rrb_time

                

            else:
                current_run_time = rrb_time - (rrb_time-processes[i])
                service_times[i] += rrb_time - (rrb_time-processes[i])
                timer += rrb_time - (rrb_time-processes[i])
                processes[i] -= rrb_time - (rrb_time-processes[i])

                

            wait_times[i] = timer-service_times[i]

            # =============================================================================
            #                                 ploting processes
            # =============================================================================
            currentAxis.add_patch(Rectangle((ref, 1),current_run_time, 1, fill=None, alpha=1))
            currentAxis.annotate(tags[i], (ref+current_run_time/2.0, 1.5), color='black', weight='bold', 
                fontsize=6  , ha='center', va='center')
            xticks.append(ref)
            ref += current_run_time
            # =============================================================================
            
    if all(i <= 0 for i in processes):
        break

avg_wait_time = "Avg Wait Time: "+str(np.average(wait_times))

currentAxis.annotate(avg_wait_time, (xlim/2, 3), color='red', weight='bold', 
                fontsize=6  , ha='center', va='center')

xticks.append(ref)
plt.xticks(xticks,fontsize=7)
plt.yticks([])
currentAxis.set_aspect(2)
plt.show()
