from machine import Pin, PWM

class Motor:
    """Controls a DC motor connected through an H-bridge driver in MicroPython.

    Manages direction via two digital GPIO pins and speed using a PWM pin set to a 
    default frequency of 1 kHz.
    """

    def __init__(self, pwm_id: int, in1_id: int, in2_id: int):
        """Initializes the motor pins and configures the default PWM frequency.

        Args:
            pwm_id (int): GPIO pin number used for PWM speed control.
            in1_id (int): GPIO pin number for direction control line 1.
            in2_id (int): GPIO pin number for direction control line 2.
        """
        self.pwm_pin = PWM(Pin(pwm_id))
        self.pwm_pin.freq(1000)
        self.in1_pin = Pin(in1_id, Pin.OUT)
        self.in2_pin = Pin(in2_id, Pin.OUT)

    def forward(self, duty: float = 0.0):
        """Drives the motor in the forward direction at the specified duty cycle.

        Args:
            duty (float, optional): Speed ratio normalized between 0.0 (off) 
                and 1.0 (full speed). Defaults to 0.0.
        """
        dc16 = int(65_535 * duty)
        self.in1_pin.value(1)
        self.in2_pin.value(0)
        self.pwm_pin.duty_u16(dc16)

    def backward(self, duty: float = 0.0):
        """Drives the motor in the reverse direction at the specified duty cycle.

        Args:
            duty (float, optional): Speed ratio normalized between 0.0 (off) 
                and 1.0 (full speed). Defaults to 0.0.
        """
        dc16 = int(65_535 * duty)
        self.in1_pin.value(0)
        self.in2_pin.value(1)
        self.pwm_pin.duty_u16(dc16)

    def stop(self):
        """Stops the motor using active braking.

        Sets both direction pins HIGH and drops the PWM duty cycle to 0.
        """
        self.in1_pin.value(1)
        self.in2_pin.value(1)
        self.pwm_pin.duty_u16(0)
        
        
if __name__ == "__main__":
    from time import sleep
    
    # SETUP
    STBY = Pin(12, Pin.OUT)
    STBY.value(1)
#     m1 = Motor(9, 10, 11)
    m2 = Motor(15, 13 ,14)
    dc = 0.0
    inc = 1 / 200
    
    # LOOP
    for _ in range(200):
        dc += inc
        m2.forward(dc)
        sleep(4 / 200)
    for _ in range(200):
        dc -= inc
        m2.forward(dc)
        sleep(4 / 200)
    
    STBY.value(0)

