from pymavlink import mavutil,mavwp

address = '127.0.0.1:14550' #for simulation 
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("connection successful")
