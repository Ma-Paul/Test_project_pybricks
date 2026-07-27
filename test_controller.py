from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Button, Port
from pybricks.messaging import BLERadio

hub = PrimeHub()
s_l = ForceSensor(Port.A)
s_r = ForceSensor(Port.B)
f_b = "n"
ble = BLERadio(broadcast_channel=1)
while True:
    if Button.LEFT in hub.buttons.pressed():
        f_b = "f"
    elif Button.RIGHT in hub.buttons.pressed():
        f_b = "b"
    if f_b == "f":
        if s_l.touched() and s_r.touched():
            ble.broadcast("Gerade")
        elif s_l.touched():
            ble.broadcast("Leftf")
        elif s_r.touched():
            ble.broadcast("Rightf")
    elif f_b == "b":
        if s_l.touched() and s_r.touched():
            ble.broadcast("Zueruc")
        elif s_l.touched():
            ble.broadcast("Leftb")
        elif s_r.touched():
            ble.broadcast("Rightb")
    elif f_b == "b" and (s_l.touched() or s_r.touched()):
        print("You first have to select a direction")
