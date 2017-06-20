# -*- coding: utf-8 -*-
"""
rangefindingSimulations1.py
Created on Wed Jun 21 10:16:18 2017

@author: DLM

Simulates laser distance measurements using laser pulses and measuring the 
received power of the pulses.
All times in us. All frequencies in MHz
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn

""" Constants """
LIGHT_SPEED = 3e2; # m/us

"""
A function that creates a square pulse based on the start_time, pulse_length,
and total time_vector. 
Returns an numpy array containing the intensity of the pulse over the time 
contained in time_vector.
The pulse must fit within the time_vector.
"""
def top_hat_pulse(start_time, pulse_length, time_vector):
    number_samples = len(time_vector)   # the number of samples in the measurement time
    pulse_vector = np.zeros((number_samples,1)) # numpy array to hold the pulse
    end_time = start_time + pulse_length    # the end time of the pulse
    # Create the pulse
    for n in range(number_samples):
        if time_vector[n] >= start_time and time_vector[n] <= end_time:
            pulse_vector[n] = 1
    return pulse_vector

"""
Function to calculate the actual pulse that is measured at the detector, assuming
that pulse measurement does not being until the pulse has finished sending.
"""
def measure_pulse(detected_pulse, measurement_start_time, time_vector):
    measured_pulse = detected_pulse.copy()
    for n in range(len(time_vector)):
        if time_vector[n] < measurement_start_time:
            measured_pulse[n] = 0
    return measured_pulse

"""
Calculates the output pulse from the laser, the detected_pulse that arrives
at the detector and the measured_pulse that is measured assuming measurement
does not begin until the output pules has finished sending
"""    
def calculate_pulses(start_time, pulse_width, delay, time_vector):
    pulse = top_hat_pulse(start_time, pulse_width, time_vector)  # output pulse
    detected_pulse = top_hat_pulse(delay, pulse_width, time_vector) # pulse that arrives at detector
    measured_pulse = measure_pulse(detected_pulse, start_time + pulse_width, time_vector) # pulse that is actually measured
    return pulse, detected_pulse, measured_pulse        

clock_speed = 20        # MHz - the speed of the clock
start_time = 0;
pulse_width_A = 1/clock_speed     # us - width of the first test pulse
pulse_width_B = 2/clock_speed     # us - width of the second test pulse
pulse_width_C = 3/clock_speed     # us - width of the second test pulse
distance = 10;  # m - the distance to be measured
time_vector = np.linspace(0, 6/clock_speed, 500)   # vector that is used for simulating the pulses and time of flight
delay = distance/LIGHT_SPEED    # the delay between emission and measurement based on the distance.


pulse_A, detected_pulse_A, measured_pulse_A =  calculate_pulses(start_time, pulse_width_A, delay, time_vector) # First pulse for testing
pulse_B, detected_pulse_B, measured_pulse_B =  calculate_pulses(start_time, pulse_width_B, delay, time_vector) # First pulse for testing
pulse_C, detected_pulse_C, measured_pulse_C =  calculate_pulses(start_time, pulse_width_C, delay, time_vector) # First pulse for testing



# Plot data
plt.close()
fig = plt.figure(num = 1, figsize=(13, 10.5), dpi=80)

ax = fig.add_subplot(311)
ax.plot(time_vector, pulse_A)
ax.plot(time_vector, detected_pulse_A)
ax.plot(time_vector, measured_pulse_A)
ax = fig.add_subplot(312)
ax.plot(time_vector, pulse_B)
ax.plot(time_vector, detected_pulse_B)
ax.plot(time_vector, measured_pulse_B)
ax = fig.add_subplot(313)
ax.plot(time_vector, pulse_C)
ax.plot(time_vector, detected_pulse_C)
ax.plot(time_vector, measured_pulse_C)
#plt.ylabel("Signal (arb. units)", fontsize = 12)
plt.xlabel("Time (us)", fontsize = 14)
#plt.xlim((0,128))
plt.show()