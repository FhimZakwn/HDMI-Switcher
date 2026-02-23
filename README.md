# HDMI-Switcher
An automated HDMI signal controller featuring Hot Plug Detect (HPD) monitoring and custom switching logic for Raspberry Pi.

## Version 1.0.0 (Terminal Control)
The initial release of the HDMI Switcher.
- **Interface:** Linux Terminal / SSH.
- **Indicators:** Physical Red (OFFLINE) and Green (ONLINE) LEDs.
- **Functions:**
  - Manual toggle for HDMI output state.
  - Live LED feedback based on connection status.
  - Safe exit routine to clean up GPIO pins.
