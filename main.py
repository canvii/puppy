import time

import Adafruit_PCA9685

delta = 20
sleep_time = 0.5
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)


def init():
    set_servo_angle(0, 90)
    set_servo_angle(1, 90)
    set_servo_angle(2, 90)
    set_servo_angle(3, 90)


def set_servo_angle(channel, angle):
    date = int(4096 * ((angle * 11) + 500) / 20000 + 0.5)
    pwm.set_pwm(channel, 0, date)
    # time.sleep(0.1)


def jump():
    set_servo_angle(0, 90 + delta)
    set_servo_angle(1, 90 - delta)
    set_servo_angle(2, 90 - delta)
    set_servo_angle(3, 90 + delta)
    time.sleep(sleep_time)



def l1():
    set_servo_angle(0, 90 - delta)
    set_servo_angle(1, 90 + delta)

def l2():
    set_servo_angle(0, 90)
    set_servo_angle(1, 90)

def l3():
    set_servo_angle(0, 90 + delta)
    set_servo_angle(1, 90 - delta)

def r1():
    set_servo_angle(2, 90 - delta)
    set_servo_angle(3, 90 + delta)

def r2():
    set_servo_angle(2, 90 )
    set_servo_angle(3, 90 )
def r3():
    set_servo_angle(2, 90 + delta)
    set_servo_angle(3, 90 - delta)





def main():
    while True:
        l1()
        time.sleep(0.5)
        l2()
        r1()

        r2()
        l3()
        time.sleep(0.5)
        r3()
        time.sleep(0.5)


if __name__ == "__main__":
    init()
    time.sleep(0.5)
    main()
