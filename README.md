This post contains instructions to program the EZCOO SP12H2 HDMI splitters with a custom firmware that:

* Provides all possible Max Luminance options
* Changes colorspace to BT2020 (vs. DCI-P3 in the original)
* Disables display-led DV

Steps:

1. Download the vendor FW update software from here:
[www.easycoolav.com/tmp/madeimg/GD32 UPDATE EX11PRO and SP12H2.rar]('https://www.easycoolav.com/tmp/madeimg/GD32%20UPDATE%20EX11PRO%20and%20SP12H2.rar')
Note that this includes the programming software, Word doc on how to update, a video and their own FW update you can use to restore to the original.
2. Download my custom FWs from Github here:
https://github.com/xnappo/ez_dv_edid_fw/releases/tag/v0.1
3. Extract both packages somewhere convenient
4. In the extracted vendor directory, go to:
...\gd32\GD32AllInOneProgrammer\GD32DfuDrivers_V3.6.6.6167\x64\
and double click 'GD32DfuDrivers.exe' to install the drivers.
5. Go to ...\gd32\GD32AllInOneProgrammer\GD32AllInOneProgrammer\GD32AllInOneProgrammer_支持C103
and double click 'GD32AllInOneProgrammer.exe' to run the programmer.
6. Now, we need to put the device into update mode.  This involves holding the 'update' button WHILE plugging in the USB cable.
a. Plug the USB cable into your PC.
b. Set the device on your desk and find something to push the button with
c. Plug the cable into the EZCOO.
d. Release the button
The blue LED should start flashing every second.
7. In the programming software select USB under interface, then hit connect:
[ATTACH type="full"]3341889[/ATTACH]


8. Hit the 'Browse' button in the 'Download' section
[ATTACH type="full"]3341890[/ATTACH]


9. Browse to where you extracted the custom FWs, change the extension from .bin to .hex in the pulldown, and select the FW you would like to install (I suggest starting with 332 or 384) then hit Open.
[ATTACH type="full"]3341891[/ATTACH]


10. Hit Download, you should see the device program.
[ATTACH type="full"]3341892[/ATTACH]


11. Hit disconnect, and you are done!


If you ever want to restore the factory FW, it is here in the package from the vendor:
...\gd32\EZ-SP12H2_APP_DFU_GD32_Ver2.06(FB4D).hex

If you are curious how the sausage was made, check out the XLS in the FW zip along with the embedded VBA code inside it.
