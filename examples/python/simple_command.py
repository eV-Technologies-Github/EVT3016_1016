"""
Example script to control eV-Technologies EVT3016 and EVT1016 Correlators
Date 26/11/2021
Licence MIT
"""

import serial

# First connect the device to the computer
# You can list available ports the the following command: "python -m serial.tools.list_ports"
# The default configuration is: 9600, 8, N, 1,no timeout, we could specify but configuring the baudrate is enough
correlator = serial.Serial('COM9', 100000)

# Send the command "S101" to connect the common port 1 to the input/output port 1
correlator.write(b"\S101")
# Send the command "S101" to connect the common port 1 to the input/output port 15
correlator.write(b"\S115")
# Send the command "S101" to connect the common port 2 to the input/output port 2
correlator.write(b"\S202")
# Send the command "S101" to connect the common port 2 to the input/output port 16
correlator.write(b"\S216")

# Close the connection
fem.close()
