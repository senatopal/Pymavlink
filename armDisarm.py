from pymavlink import mavutil
import time

address = '127.0.0.1:14550' #for simulation 
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()

vehicle.mav.command_long_send(
    vehicle.target_system,
    vehicle.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    1, 0, 0, 0, 0, 0, 0)

time.sleep(2)

vehicle.mav.command_long_send(
    vehicle.target_system,
    vehicle.target_component,
    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM,
    0,
    0, 0, 0, 0, 0, 0, 0)