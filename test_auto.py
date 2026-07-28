from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Direction, Port
from pybricks.messaging import BLERadio
from pybricks.tools import wait

hub = PrimeHub()
m_r = Motor(Port.E, positive_direction=Direction.COUNTERCLOCKWISE)
m_l = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
m_lenk = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
initial_rot_m_lenk = m_lenk.angle()


def turn_leftf(speed_s=500):
    m_lenk.run_target(500, initial_rot_m_lenk + 50)
    m_l.run(speed_s)
    m_r.run(speed_s)


def turn_rightf(speed_s=500):
    m_lenk.run_target(500, initial_rot_m_lenk - 50)
    m_l.run(speed_s)
    m_r.run(speed_s)


def turn_leftb(speed_s=500):
    m_lenk.run_target(500, initial_rot_m_lenk - 50)
    m_l.run(-speed_s)
    m_r.run(-speed_s)


def turn_rightb(speed_s=500):
    m_lenk.run_target(500, initial_rot_m_lenk + 50)
    m_l.run(-speed_s)
    m_r.run(-speed_s)


def faaahr(speed_s=500):
    m_l.run(speed_s)
    m_r.run(speed_s)


ble = BLERadio(observe_channels=[1])
while True:
    wait(100)
    data = ble.observe(1)

    if data:
        if data == "Leftf":
            turn_leftf()
            print("leftf called")
        elif data == "Rightf":
            turn_rightf()
            print("rightf called")

        elif data == "Leftb":
            turn_leftb()
            print("leftb called")

        elif data == "Rightb":
            turn_rightb()
            print("rightb called")

        elif data == "Gerade":
            m_lenk.run_target(500, initial_rot_m_lenk)
            faaahr()
            print("Gerade called")
        elif data == "Zueruc":
            m_lenk.run_target(500, initial_rot_m_lenk)
            faaahr(-500)
            print("back called")
        elif data != "Leftf" or data != "Leftb" or data != "Rightf" or data != "Rightb":
            m_lenk.run_target(500, initial_rot_m_lenk)
            print("reset to initial")
    else:
        m_l.brake()
        m_r.brake()
        print("breaking")
