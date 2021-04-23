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
    # pwm.set_pwm(channel, (int)(date / 2), date)
    pwm.set_pwm(channel, 0, date)
    # time.sleep(0.1)


def jump():
    set_servo_angle(0, 90 + delta)
    set_servo_angle(1, 90 - delta)
    set_servo_angle(2, 90 - delta)
    set_servo_angle(3, 90 + delta)
    time.sleep(sleep_time)

    # set_servo_angle(0,90)
    # set_servo_angle(1,90)
    # set_servo_angle(2,90)
    # set_servo_angle(3,90)
    # time.sleep(1)


def right_go():
    set_servo_angle(0, 90 - delta)
    set_servo_angle(1, 90 + delta)
    time.sleep(0.2)
    set_servo_angle(0, 90 + delta)
    set_servo_angle(1, 90 - delta)



def left_go():
    set_servo_angle(2, 90 - delta)
    set_servo_angle(3, 90 + delta)
    time.sleep(0.2)
    set_servo_angle(2, 90 + delta)
    set_servo_angle(3, 90 - delta)



def right_default():
    set_servo_angle(0, 90)
    set_servo_angle(1, 90)


def left_default():
    set_servo_angle(2, 90)
    set_servo_angle(3, 90)


def main():
    while True:
        left_go()
        time.sleep(sleep_time)
        right_go()
        time.sleep(sleep_time)


if __name__ == "__main__":
    init()
    time.sleep(0.5)
    main()
