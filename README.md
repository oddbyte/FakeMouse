# FakeMouse
## Requires root!
 Moves your mouse using a rooted android device. Note:
 - **You need to be able to "adb root", so if you are not rooted, or cant "adb root", please get root and come back.**
## Pre installation:
- Install https://github.com/tejado/android-usb-gadget and enable the HID gadget. This is required for the other app to be able to make a HID device. ![picture showing hid enabled](https://github.com/oddbyte/FakeMouse/blob/62220d32f31e51ea22d53c61eee1d393ed83ae58/Screenshot_20241014-111951_USB%20Gadget%20Tool.png)

# Installation
 1. Install [This app](https://github.com/Arian04/android-hid-client)
 2. Open it, and move the touchpad a bit to make sure it works.
 3. Run "adb root".
 4. Run adb push script.sh /data/local/tmp/script.sh
 5. Install python (if you havent already), and run test.py on your pc while connected to your rooted phone.
 - When you reboot you will need to re-open the app and move the touchpad a bit so it can re-make all the files.
