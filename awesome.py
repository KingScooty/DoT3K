#!/usr/bin/env python
import dot3k.lcd as lcd
import dot3k.backlight as backlight
import time, datetime, copy, math, psutil

cpu_sample_count = 200
cpu_samples = [0] * cpu_sample_count

hue = 0.0

while True:
        hue += 0.001
        backlight.sweep(hue)

        cpu_samples.append(psutil.cpu_percent() / 100.0)
        cpu_samples.pop(0)

        cpu_avg = sum(cpu_samples) / cpu_sample_count
        backlight.set_graph(cpu_avg)


        #cpu = psutil.cpu_percent(interval=0, percpu=False)
        cake = int(cpu_avg)
        #backlight.rgb(0,125,200)

        if hue > 1.0:
                hue = 0.0

        lcd.set_cursor_position(0,0)
        useage = str(cpu_avg * 100)
        lcd.write('CPU: '+ useage)

        lcd.set_cursor_position(0,1)

        t = datetime.datetime.now().strftime("%H:%M:%S")
        lcd.write('Time: ' + t)

        #shiz = psutil.cpu_temperature()
        #lcd.set_cursor_position(0,2)
        #lcd.write('CPU Temp: '+ str(shiz))
        time.sleep(0.05)