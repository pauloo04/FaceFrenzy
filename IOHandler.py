import time

class IOHandler:
    def __init__(self, base):
        # Use exactly the available LEDs and buttons
        self.leds = [base.leds[0], base.leds[1], base.leds[2], base.leds[3]]
        self.btn0 = base.buttons[0]
        self.btn1 = base.buttons[1]
        self.btn2 = base.buttons[2]
        self.btn3 = base.buttons[3]

    def read_buttons(self):
        return {
            'btn0': self.btn0.read(),
            'btn1': self.btn1.read(),
            'btn2': self.btn2.read(),
            'btn3': self.btn3.read()
        }

    def set_led_countdown(self, remaining, total):
        active = int((remaining / total) * len(self.leds))
        for i, led in enumerate(self.leds):
            if i < active:
                led.on()
            else:
                led.off()

    def show_result(self, success):
        # Flash all LEDs green or red for feedback
        for i in range(3):
            for led in self.leds:
                if success:
                    led.on()
                else:
                    led.off()
            time.sleep(0.2)
            for led in self.leds:
                if success:
                    led.off()
                else:
                    led.on()
            time.sleep(0.2)

    def clear_leds(self):
        for led in self.leds:
            led.off()