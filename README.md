CHWS Edge Server 

This repository contains the file that simulates the edge server in my CHWS system.

Files in this repo. 
./test_files/edge_server_test.py
./edge_server.py
./mosquitto.sh

Required installation 
for connection mosquitto

Required imports 
for Python paho

edge_server_test.py - test if your device as an edge server works with vehicle_a_test.py and vehicle_b_test.py
edge_server.py - main edge server code
mosquitto.sh - runs mosquitto -c ./mosquitto/mosquitto.conf -v

You must configure mosquitto before you start for remote connections. 

The CHWS connections must established by following the procedure below.

Start a mosquitto process on your edge device.
Start your Python edge server. Wait for connection establishment.
Start vehicle_b.py. Wait for connection establishment.
Start vehicle_a.py.