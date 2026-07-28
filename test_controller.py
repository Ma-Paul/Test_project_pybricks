from pybricks.hubs import PrimeHub
from pybricks.pupdevices import ForceSensor
from pybricks.parameters import Button, Port
from pybricks.messaging import BLERadio

hub = PrimeHub()
s_l = ForceSensor(Port.F)
s_r = ForceSensor(Port.B)
f_b = "n"
ble = BLERadio(broadcast_channel=1)
while True:
    if Button.LEFT in hub.buttons.pressed():
        f_b = "f"
    elif Button.RIGHT in hub.buttons.pressed():
        f_b = "b"
    if f_b == "f":
        if s_l.pressed() and s_r.pressed():
            ble.broadcast("Gerade")
        elif s_l.pressed():
            ble.broadcast("Leftf")
        elif s_r.pressed():
            ble.broadcast("Rightf")
        elif not s_l.pressed() or not s_r.pressed():
            ble.broadcast("nothing")
    elif f_b == "b":
        if s_l.pressed() and s_r.pressed():
            ble.broadcast("Zueruc")
        elif s_l.pressed():
            ble.broadcast("Leftb")
        elif s_r.pressed():
            ble.broadcast("Rightb")
        elif not s_l.pressed() or not s_r.pressed():
            ble.broadcast("nothing")
    elif f_b == "b" and (s_l.pressed() or s_r.pressed()):
        print("You first have to select a direction")
