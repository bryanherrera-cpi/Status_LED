import serial
import time

usb_port_name = "/dev/tty.usbserial-0001"

serialPort = serial.Serial(
    port=usb_port_name, baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
)

print("Starting test...\n")
serialPort.write(b'sr\r')
time.sleep(7)
#serialPort.write(b'l 0 0 0\r')

#time.sleep(1)

print("Turn LED Red\n")
serialPort.write(b'l 0\r')

time.sleep(2)

print("Turn LED Green\n")
serialPort.write(b'l 120\r')

time.sleep(2)

print("Turn LED Blue\n")
serialPort.write(b'l 240\r')

time.sleep(2)

print("Turn LED White (All LED On)\n")
serialPort.write(b'l 50 50 50\r')

time.sleep(2)

print("Functional Test Completed\n")
serialPort.write(b'l 0 0 0\r')
serialPort.write(b'wo\r')
