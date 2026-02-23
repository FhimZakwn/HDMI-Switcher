from gpiozero import LED
import sys

# --- Configuration (v0.0.2) ---
led_green  = LED(22)    # Green Light (Online)
led_red    = LED(27)    # Red Light (Offline)
output_pin = LED(17)    # Transistor switch (NPN logic)

def ledON():
    """Turn the HDMI connection ON"""
    led_green.on()
    led_red.off()
    output_pin.off() # Release Ground (NPN) -> Connection starts
    print(">> STATUS: SYSTEM ONLINE [Connected]")

def ledOFF():
    """Turn the HDMI connection OFF"""
    led_green.off()
    led_red.on()
    output_pin.on()  # Ground the line (NPN) -> Connection cuts
    print(">> STATUS: SYSTEM OFFLINE [Disconnected]")

# --- Main Terminal Loop ---
print("--- HDMI Terminal Controller v0.0.2 ---")
print("Commands: 'on' to connect, 'off' to disconnect, 'exit' to quit")

# Set initial state
ledOFF()

try:
    while True:
        # Get input from the user
        command = input("Enter Command: ").strip().lower()

        if command == "on":
            ledON()
        elif command == "off":
            ledOFF()
        elif command == "exit":
            print("Shutting down controller...")
            break
        else:
            print("Invalid command. Use 'on', 'off', or 'exit'.")

except KeyboardInterrupt:
    print("\nProgram stopped by user.")
finally:
    # Cleanup: optional, but good practice to leave system in a safe state
    ledOFF()
