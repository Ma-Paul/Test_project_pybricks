from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.messaging import BLERadio

hub = PrimeHub()
m_r = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
m_l = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE)
m_lenk = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
initial_rot_m_lenk = m_lenk.angle()


def turn_leftf(speed_s=50):
    m_lenk.run_angle(50, 35)
    m_l.run(speed_s)
    m_r.run(speed_s)


def turn_rightf(speed_s=50):
    m_lenk.run_angle(50, -35)
    m_l.run(speed_s)
    m_r.run(speed_s)


def turn_leftb(speed_s=50):
    m_lenk.run_angle(50, 35)
    m_l.run(-speed_s)
    m_r.run(-speed_s)


def turn_rightb(speed_s=50):
    m_lenk.run_angle(50, -35)
    m_l.run(-speed_s)
    m_r.run(-speed_s)


def faaahr(speed_s=50):
    m_l.run(speed_s)
    m_r.run(speed_s)


ble = BLERadio(observe_channels=[1])
while True:

    data = ble.observe(1)

    if data:
        if data == "Leftf":
            turn_leftf()
        elif data == "Rightf":
            turn_rightf()
        elif data == "Leftb":
            turn_leftb()
        elif data == "Rightb":
            turn_rightb()
        elif data == "Gerade":
            faaahr()
        elif data == "Zueruc":
            faaahr(-50)
        elif data != "Leftf" or data != "Leftb" or data != "Rightf" or data != "Rightb":
            m_lenk.run_target(50, initial_rot_m_lenk)
    else:
        m_l.brake()
        m_r.brake()
