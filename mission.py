from pymavlink import mavutil,mavwp

address = '127.0.0.1:14550'  
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("connection successful")
msg=vehicle.recv_match()
wp=mavwp.MAVWPLoader()

def get_alt():
    message = vehicle.recv_match(type='GLOBAL_POSITION_INT', blocking= True)
    alt=message.relative_alt
    alt = alt/1000
    return alt

        
def takeoff(alt):
    vehicle.mav.command_long_send(vehicle.target_system, vehicle.target_component,mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0, 0, 0, 0, alt)
    vehicle.set_mode("TAKEOFF")
    while True: 
        current_alt= get_alt()
        if current_alt< alt:
            print(f"Current altitude :{current_alt}")
        elif current_alt >=  alt:
            print("Reached target altitude")
            break 
def add_mission(seq,lat,lon,alt):
        frame= mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT
        vehicle.set_mode("TAKEOFF")
        wp.add(mavutil.mavlink.MAVLink_mission_item_message(vehicle.target_system, vehicle.target_component,
        seq,
        frame,
        mavutil.mavlink.MAV_CMD_NAV_WAYPOINT,0,0,0,0,0,0,lat,lon,alt))

        vehicle.waypoint_clear_all_send()
        vehicle.waypoint_count_send(wp.count())
        for i in range (wp.count()):
            msg= vehicle.recv_match(type=["MISSION_REQUEST"], blocking= True)
            vehicle.mav.send(wp.wp(msg.seq))
            print("Sending waypoints {0}".format(msg.seq))


vehicle.set_mode("GUIDED")
vehicle.arducopter_arm()
print("The vehicle armed")
takeoff(10)

add_mission(0, -35.36319320, 149.16543250, 25)
add_mission(1, -35.36296790, 149.16540030, 35)
add_mission(2, -35.36292410, 149.16519640, 40)
add_mission(3, -35.36306190, 149.16500060, 20)
add_mission(4, -35.36319970, 149.16513470, 10)

vehicle.set_mode("AUTO")
