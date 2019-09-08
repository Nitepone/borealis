import logging
import time
from typing import List

import _rpi_ws281x as ws

from .model.color import ColorInterface, ColorRGB24
from .model.pixel import Pixel
from .model.position import PositionNormalized3D

logger = logging.getLogger(__name__)


class FollowerInterface(object):
    pass


class SimpleStripFollower(object):
    LED_CHANNEL    = 0
    # Frequency of the LED signal. Should be 800khz or 400khz.
    LED_FREQ_HZ    = 800000     
    # DMA channel to use, can be 0-14.
    LED_DMA_NUM    = 10
    # GPIO connected to the LED signal line.  Must support PWM!
    LED_GPIO       = 18
    # Set to 0 for darkest and 255 for brightest
    LED_BRIGHTNESS = 255
    # Set to 1 to invert the LED signal, good if using NPN transistor as a
    # 3.3V->5V level converter.  Keep at 0 for a normal/non-inverted signal.
    LED_INVERT     = 0          

    def __init__(self, length: int):
        self.length = length

        # Allocate a new ws2811_t c struct on the heap.
        strip = ws.new_ws2811_t()

        # Write the configuration to the newly allocated ws2811_t struct.
        ws.ws2811_t_freq_set(strip, self.LED_FREQ_HZ)
        ws.ws2811_t_dmanum_set(strip, self.LED_DMA_NUM)

        # Allocate a new ws2811_channel_t c struct on the heap. This struct
        # also has a pointer to the colors for each led on the strip.
        channel = ws.ws2811_channel_get(strip, self.LED_CHANNEL)
        
        # Write the configuration to the newly allocated ws2811_channel_t struct.
        ws.ws2811_channel_t_count_set(channel, self.length)
        ws.ws2811_channel_t_gpionum_set(channel, self.LED_GPIO)
        ws.ws2811_channel_t_invert_set(channel, self.LED_INVERT)
        ws.ws2811_channel_t_brightness_set(channel, self.LED_BRIGHTNESS)

        resp = ws.ws2811_init(strip)
        if resp != ws.WS2811_SUCCESS:
            message = ws.ws2811_get_return_t_str(resp)
            raise RuntimeError('ws2811_init failed with code {0} ({1})'.format(resp, message))

        # save references to the newly created c stucts
        self.strip = strip
        self.channel = channel

    def flush(self):
        """Write all changes to strip"""
        resp = ws.ws2811_render(self.strip)
        if resp != ws.WS2811_SUCCESS:
            message = ws.ws2811_get_return_t_str(resp)
            raise RuntimeError('ws2811_render failed with code {0} ({1})'.format(resp, message))

    def update(self, pixel: Pixel, color: ColorInterface):
        ws.ws2811_led_set(self.channel, pixel._id, color.gbr.to_int32())

    def spin_once(self):
        """main loop"""
        for i in range(self.length):
            self.update(i, ColorRGB24(120, 0, 120))
        self.flush()

    def identifier_iter(self):
        return range(self.length)

    def pixel_iter(self):
        for i in range(self.length):
            yield Pixel(i, PositionNormalized3D(i * 1. / self.length,0,0))

    def __del__(self):
        # Ensure ws2811_fini is called before the program quits. It'll make
        # sure that the DMA is finished before program execution stops and
        # cleans up after itself.
        logger.info('Waiting for DMA to finish.')
        ws.ws2811_fini(self.strip)

        # Call delete function to clean up structure memory.
        logger.info('Freeing WS2811 struct from heap.')
        ws.delete_ws2811_t(self.strip)
