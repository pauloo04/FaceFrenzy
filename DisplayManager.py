from pynq.overlays.base import BaseOverlay
from pynq.lib.video import *
import numpy as np
import cv2

class DisplayManager:
    def __init__(self, resolution=(640, 480)):
        self.base = BaseOverlay("base.bit")
        self.hdmi_out = self.base.video.hdmi_out
        self.width, self.height = resolution
        self.hdmi_out.configure(VideoMode(self.width, self.height, 24))
        self.hdmi_out.start()
        self.overlay_text = ""

    def set_overlay_text(self, text):
        self.overlay_text = text

    def clear_overlay_text(self):
        self.overlay_text = ""

    def show_frame(self, frame_bgr):
        frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)

        if self.overlay_text:
            for i, line in enumerate(self.overlay_text.split('\n')):
                y = 50 + i * 40
                cv2.putText(
                    frame_rgb,
                    line,
                    (10, y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.0,
                    (0, 255, 0),
                    2
                )

        out_frame = self.hdmi_out.newframe()
        out_frame[:, :, :] = frame_rgb
        self.hdmi_out.writeframe(out_frame)

    def white_screen(self):
        frame = np.ones((self.height, self.width, 3), dtype=np.uint8) * 255
        self.show_frame(frame)

    def stop(self):
        self.hdmi_out.stop()