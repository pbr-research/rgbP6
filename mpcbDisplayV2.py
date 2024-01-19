#!/usr/bin/env python
# Display a runtext with double-buffering.
from samplebase import SampleBase
from rgbmatrix import graphics
from dypatil_fetch import getData_forbs, param

import threading
import time

units = ["mg/Nm2", "Kg/Hr", "mg/Nm2", "mg/L", "mg/L", "mg/L", " ", "M3/Hr"]
paramNum = [0,1,3,4,5,6,7,8]
par = ["PM","Mass Flow","PM","COD","BOD","TSS", "PH","flow"]
line = ["PM : --","Mass Flow: --","PM:--","COD: --","BOD: --","TSS: --", "PH: --","flow: --"]



def read():
	while True:
		print(getData)
		time.sleep(10)

line1 = ""
line2 = ""


def dataPro():
	global line1
	global line2
	print("in dataPro")
	data = getData_forbs()
	for i in range(len(paramNum)):
		if data[param[paramNum[i]]] is not None:
			s = par[i] + ' ' + data[param[paramNum[i]]]+ ' '+ units[i]
			line[i] = s
			print(s)
	line1 = ",".join(line[0:4])
	line2 = ",".join(line[4:])
	print(line)
	print(line1)
	print(line2)

class RunText(SampleBase):
    def __init__(self, *args, **kwargs):
        super(RunText, self).__init__(*args, **kwargs)
        self.parser.add_argument("-t", "--text", help="The text to scroll on the RGB LED panel", default="Hello world!")

    def run(self):
        offscreen_canvas = self.matrix.CreateFrameCanvas()
        font = graphics.Font()
        font.LoadFont("../../../fonts/9x18B.bdf")
        textColor = graphics.Color(50, 255, 100)
        pos = offscreen_canvas.width
        #my_text = test #self.args.text
        count = 0
        while True:
            offscreen_canvas.Clear()
            len1 = graphics.DrawText(offscreen_canvas, font, pos, 20, textColor, line1)
            len2 = graphics.DrawText(offscreen_canvas, font, pos, 20+31, textColor, line2)
            pos -= 1
            if (pos + len1 < 0):
                count += 1
                print(count)
                pos = offscreen_canvas.width
                if(count > 1):
                    count = 0
                    try:
                        dataPro()
                    except:
                        print("NO INTERNET CONNECTION ..!")

            time.sleep(0.05)
            offscreen_canvas = self.matrix.SwapOnVSync(offscreen_canvas)

#t1 = threading.Thread(read)

# Main function
if __name__ == "__main__":
 #   t1.start()
#    dataPro(readAPI)
    run_text = RunText()
    if (not run_text.process()):
        run_text.print_help()
