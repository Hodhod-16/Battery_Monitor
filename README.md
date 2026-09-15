# Battery Monitor

A background script that watches your laptop's battery status on Windows and sends a desktop notification when:
- The battery drops to 30% or below and the charger is not plugged in
- The battery reaches 100% while the charger is plugged in

Each notification is sent only once per state change, not repeatedly every minute.

## Requirements
- Python 3.11 or higher
- Windows only (the `winotify` library only works on Windows, not macOS or Linux)

## Setup

1. Clone this repository
2. Install the required libraries:


 pip install -r requirements.txt


## Usage

Run the script:

python battery.py

The script runs continuously in the background, checking the battery status every 60 seconds and printing it to the terminal. To stop it, press Ctrl+C.

## How it works

- The script uses the `psutil` library to read the current battery percentage and charger status every 60 seconds.
- Two boolean flags (`notified` and `full_notified`) keep track of whether a notification has already been sent for the current state, so the same alert is not repeated every minute while the condition remains true.
- When the battery is low and unplugged, a "Battery Low" notification is triggered once.
- When the battery is full and plugged in, a "Battery Full" notification is triggered once.
- Once the condition is no longer true (for example, the charger is unplugged, or the battery percentage changes), the corresponding flag resets to `False`, allowing a new notification the next time the condition is met again.

## Notes
- The script is meant to run continuously in the background while working, not as a one-time check.
