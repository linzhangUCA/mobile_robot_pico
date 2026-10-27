from upython_scripts.action.motor import Motor
from time import sleep
import json
from platform import platform

print(platform())
from machine import Pin

with open("/upython_scripts/config.json") as f:
    config = json.load(f)

# SETUP
bot = Motor(
    pwm_id=config["right_motor_pins"]["pwm"],
    in1_id=config["right_motor_pins"]["in1"],
    in2_id=config["right_motor_pins"]["in2"],
)
print(f"PWM ID: {config["right_motor_pins"]["pwm"]}")
print(f"IN1 ID: {config["right_motor_pins"]["in1"]}")
print(f"IN2 ID: {config["right_motor_pins"]["in2"]}")

stby_pin = Pin(12, Pin.OUT)
stby_pin.value(1)


# LOOP
bot.forward(duty=0.5)
sleep(2)
bot.stop()
