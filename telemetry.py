from pymavlink import mavutil
import math

address = '127.0.0.1:14550' 
vehicle= mavutil.mavlink_connection(address,baudrate=57600,autoreconnect= True)
vehicle.wait_heartbeat()
print("Baglanti basarili")

def telemetri():
    msg = vehicle.recv_match(blocking=True)
    if msg.name == 'GLOBAL_POSITION_INT':
        IHA_irtifa = msg.relative_alt/1000
        print(" irtifa = ", IHA_irtifa)
    
    
    msg = vehicle.recv_match(blocking=True)
    if msg.name == 'ATTITUDE':
        IHA_dikilme = math.degrees(msg.pitch)
        IHA_yonelme = math.degrees(msg.yaw)
        IHA_yatis = math.degrees(msg.roll)
        print(" Dikilme = ", IHA_dikilme)
        print(" Yonelme = ", IHA_yonelme)
        print(" Yatis = ", IHA_yatis)
    
    
    msg = vehicle.recv_match(blocking=True)
    if msg.name == 'GPS_RAW_INT':
        IHA_enlem = msg.lat / 1.0e7
        IHA_boylam = msg.lon / 1.0e7
        IHA_hiz = msg.vel/100
        print(" Enlem = ", IHA_enlem)
        print(" Boylam = ", IHA_boylam)
        print(" Hiz = ", IHA_hiz)
    
    
    msg = vehicle.recv_match(blocking=True)
    if msg.name == 'BATTERY_STATUS':
        IHA_batarya = msg.battery_remaining
        print(" Batarya = ", IHA_batarya)

telemetri()