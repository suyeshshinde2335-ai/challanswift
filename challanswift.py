import time
import sys

def type_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ----------------- MAIN PROGRAM -----------------
type_effect("\n=== Welcome to CHALLANSWIFT: Smart Traffic Penalty System ===", 0.05)
type_effect("------------------------------------------------------------", 0.05)

officer_name = input("Enter Officer Name: ")
driver_name = input("Enter Driver Name: ")
vehicle_number = input("Enter Vehicle Number (e.g., MH14AA1234): ")

total_fine = 0
violations_list = ""

print("\n--- Checking for traffic violations ---")

# Violation 1: Driving without Helmet
helmet_check = input("\nIs the driver wearing a helmet? (yes/no): ")
if helmet_check.lower() == "no":
    total_fine = total_fine + 500
    violations_list = violations_list + "* No Helmet (Fine: Rs 500)\n"
    print("❌ Fine Added: Rs 500 for No Helmet.")
else:
    print("✅ Checked: Driver is wearing a helmet.")

# Violation 2: Over-speeding
speed = int(input("\nEnter the vehicle speed (in km/h): "))
if speed > 60:
    total_fine = total_fine + 1000
    violations_list = violations_list + "* Over-speeding (Fine: Rs 1000)\n"
    print(f"❌ Fine Added: Rs 1000 for Over-speeding ({speed} km/h).")
else:
    print(f"✅ Checked: Speed is under control ({speed} km/h).")

# Violation 3: Driving without License
license_check = input("\nDoes the driver have a valid license? (yes/no): ")
if license_check.lower() == "no":
    total_fine = total_fine + 2000
    violations_list = violations_list + "* No Valid License (Fine: Rs 2000)\n"
    print("❌ Fine Added: Rs 2000 for No License.")
else:
    print("✅ Checked: Driver has a valid license.")

# Violation 4: Drunk Driving Check
drunk_check = input("\nIs the driver under the influence of alcohol? (yes/no): ")
if drunk_check.lower() == "yes":
    total_fine = total_fine + 10000
    violations_list = violations_list + "* Drunk Driving (Fine: Rs 10000)\n"
    print("❌ DANGER! Fine Added: Rs 10000 for Drunk Driving.")
else:
    print("✅ Checked: Driver is sober.")

# ----------------- FINAL CHALLAN RECEIPT -----------------
print("\n==============================================")
type_effect("       CHALLANSWIFT DIGITAL RECEIPT   ", 0.04)
print("==============================================")
print(f"On-Duty Officer : {officer_name}")
print(f"Driver Name     : {driver_name}")
print(f"Vehicle Number  : {vehicle_number}")
print("----------------------------------------------")
print("Violations Detected:")
if total_fine == 0:
    print(" * NO VIOLATIONS! Safe Driver Award! ⭐")
else:
    print(violations_list)
print("----------------------------------------------")
print(f"TOTAL PENALTY AMOUNT TO PAY: Rs {total_fine}")
print("==============================================")
type_effect("Drive safe and follow traffic rules! 🚗⚡", 0.04)