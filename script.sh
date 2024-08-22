#!/system/bin/sh

KEYBOARD_DEVICE="/dev/hidg0"
MOUSE_DEVICE="/dev/hidg1"

# Key press and release function for keyboard
send_keyboard() {
    input=$1
    for i in $(seq 1 ${#input}); do
        char=${input:i-1:1}
        case "$char" in
            a) keycode="04" ;;
            b) keycode="05" ;;
            c) keycode="06" ;;
            d) keycode="07" ;;
            e) keycode="08" ;;
            f) keycode="09" ;;
            g) keycode="0A" ;;
            h) keycode="0B" ;;
            i) keycode="0C" ;;
            j) keycode="0D" ;;
            k) keycode="0E" ;;
            l) keycode="0F" ;;
            m) keycode="10" ;;
            n) keycode="11" ;;
            o) keycode="12" ;;
            p) keycode="13" ;;
            q) keycode="14" ;;
            r) keycode="15" ;;
            s) keycode="16" ;;
            t) keycode="17" ;;
            u) keycode="18" ;;
            v) keycode="19" ;;
            w) keycode="1A" ;;
            x) keycode="1B" ;;
            y) keycode="1C" ;;
            z) keycode="1D" ;;
            *) keycode="00" ;;  # Default to "no key" for unsupported characters
        esac
        echo -ne "\x01\x00\x00\x$keycode\x00" > $KEYBOARD_DEVICE
        sleep 0.1
        echo -ne "\x01\x00\x00\x00\x00" > $KEYBOARD_DEVICE
        sleep 0.1
    done
}

# Function for mouse movement
send_mouse() {
    input=$1
    echo -ne "$input" > $MOUSE_DEVICE
}

# Main script logic
if [ "$1" = "keyboard" ]; then
    send_keyboard "$2"
elif [ "$1" = "mouse" ]; then
    send_mouse "$2"
else
    echo "Usage: $0 {keyboard|mouse} <input>"
    exit 1
fi