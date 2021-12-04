"""
Test script for ordering the correlator to do a sweep with specified parameters
Date 04/12/2021
"""

import serial
import time

nb_common_ports = 4
nb_ports = 16
time_interval = 10 # in milliseconds

def select_port(common, port):
    common_str = str(common)
    port_str = str(port)
    # Check if we must add a '0'
    if port < 10:
        return('S' + common_str + '0' + port_str)
    else:
        return('S' + common_str + port_str)

# We can't use the sleep function because it rely on the OS clock which is not precise enough in Windows environments (approx. 16ms)
# Instead we create a Delay_ms function which use time.perf_counter() which use the most precise clock available on the system (less than 1ms)
def Delay_ms(ms):
    t1 = time.perf_counter()
    t2 = t1
    while (((t2-t1)*10**3) < ms):
        t2 = time.perf_counter()
    print("Elapsed time: ", ((t2-t1)*10**3), " ms")
    return ((t2-t1)*10**3)

def sweep_port(start, stop, common_port, time_interval):
    if (type(start) != int or type(stop) != int):
        return ("start and sopt values must be integers.")
    if (start > stop):
        return ("Start port must be inferior to stop port.")
    if (type(common_port) != int):
        return ("common_port value must be an integer.")
    if (time_interval < 0.4):
        return ("Baudrate limit exeeded, increase the time interval.")

    print("Parameters :")
    print("Common port :", common_port)
    print("sweep start port :", start)
    print("sweep stop port :", stop)
    print("time interval :", time_interval, " ms")

    for i in range(start, stop+1):
        data_to_send = select_port(common_port, i)
        correlator.write(data_to_send.encode('ascii'))
        print("Command sent: ", data_to_send)
        Delay_ms(time_interval)

def sweep_dual(start, stop, common_port_1, common_port_2, time_interval):
    sweep_port(start, stop, common_port_1, time_interval)
    Delay_ms(time_interval)
    sweep_port(start, stop, common_port_2, time_interval)

# First connect the device to the computer
# You can list available ports the the following command: "python -m serial.tools.list_ports"
# The default configuration is: 9600, 8, N, 1,no timeout, we could specify but configuring the baudrate is enough
correlator = serial.Serial('COM3', 100000)

# Do a sweep from port 1 to 16 with the common port 1 and a delay of 10 ms between each switch
sweep_port(1, 16, 1, time_interval)

correlator.close()
