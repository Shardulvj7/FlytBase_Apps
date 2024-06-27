import time
from flyt_python import api
drone = api.navigation(timeout=120000)  
time.sleep(3)

print('taking off')
drone.take_off(10.0)
time.sleep(5)

print('going along the setpoints')

def move_and_print(x, y, z, relative=True):
    drone.position_set(x, y, z, relative=relative)
    for _ in range(6):  
        print('Moving to setpoint: x={}, y={}, z={}'.format(x, y, z))

move_and_print(10, 0, 0)
move_and_print(-5, 8.66, 0)
move_and_print(-5, -8.66, 0)

print('Landing')
drone.land(async=False)
drone.disconnect()
