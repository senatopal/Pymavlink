from pymavlink import mavutil

address = '127.0.0.1:14550'
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("connection successful")
def get_alt():
    message = vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking= True)
    alt=message.relative_alt
    alt = alt/1000
    return alt

        
def takeoff(alt):
    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, alt)
    
    while True: 
        current_alt= get_alt()
        if current_alt< alt:
            print(f"Current altitude :{current_alt}")
        elif current_alt >=  alt:
            print("Reached target altitude")
            break 

def move(y,x,z):
    vehicle.mav.send(mavutil.mavlink.MAVLink_set_position_target_local_ned_message(
        10,vehicle.target_system,vehicle.target_component,9,
        int(0b0000011111111000),
        y,x,z,
        0,0,0,
        0,0,0,
        0,0
    ))
def go_to(lat,lon,alt):
    vehicle.mav.mission_item_send(0,0,0,mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT,mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,2,0,0,0,0,0,lat,lon,alt)

vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("The vehicle armed")
takeoff(10)
go_to(-35.36319320, 149.16543250, 25)