# Project: ChallanSwift v4.0 | Developed by Suyesh Shinde
import time
import sys

def type_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ----------------- MAIN PROGRAM v4.0 (INFINITE LOOP) -----------------
type_effect("\n=== Welcome to CHALLANSWIFT v4.0: Continuous Logging System ===", 0.05)
type_effect("****----------------------------------------------------****", 0.05)

officer_name = input("Enter On-Duty Officer Name: ")

# Naya Feature: Loop continuous chalega jab tak system exit na ho
system_active = "yes"

while system_active.lower() == "yes" or system_active.lower() == "y":
    print("\n============================================================")
    print("                     NEW CHALLAN ENTRY                      ")
    print("============================================================")
    
    driver_name = input("Enter Driver Name: ")
    vehicle_number = input("Enter Vehicle Number: ")

    # Emergency Vehicle Check
    emergency_check = input("\nIs this an Emergency Vehicle? (Ambulance/Fire Brigade/Army) (yes/no): ")

    total_fine = 0
    violations_list = ""

    if emergency_check.lower() == "yes":
        print("\n🚨 EMERGENCY VEHICLE DETECTED! All penalties waived automatically. 🚨")
        violations_list = "* EMERGENCY VEHICLE OVERRIDE (Fine: Rs 0)\n"
    else:
        # Select Vehicle Type
        print("\nSelect Vehicle Type:")
        print("[1] Two-Wheeler (Bike/Scooty)")
        print("[2] Four-Wheeler (Car/SUV)")
        vehicle_type = input("Enter choice (1 or 2): ")

        print("\n--- Checking for traffic violations ---")

        # 1. Specific Check for Two-Wheeler vs Four-Wheeler
        if vehicle_type == "1":
            helmet_check = input("\nIs the rider wearing a helmet? (yes/no): ")
            if helmet_check.lower() == "no":
                total_fine = total_fine + 500
                violations_list = violations_list + "* No Helmet (Fine: Rs 500)\n"
                print("❌ Fine Added: Rs 500 for No Helmet.")
            else:
                print("✅ Checked: Rider is wearing a helmet.")
        elif vehicle_type == "2":
            seatbelt_check = input("\nIs the driver wearing a seatbelt? (yes/no): ")
            if seatbelt_check.lower() == "no":
                total_fine = total_fine + 1000
                violations_list = violations_list + "* No Seatbelt (Fine: Rs 1000)\n"
                print("❌ Fine Added: Rs 1000 for No Seatbelt.")
            else:
                print("✅ Checked: Driver is wearing a seatbelt.")

        # 2. Speed Check
        speed = int(input("\nEnter the vehicle speed (limit is 60 km/h): "))
        if speed > 60:
            total_fine = total_fine + 2000
            violations_list = violations_list + "* Over-speeding (Fine: Rs 2000)\n"
            print(f"❌ Fine Added: Rs 2000 for Over-speeding ({speed} km/h).")
        else:
            print(f"✅ Checked: Speed is under control ({speed} km/h).")

        # 3. License Check
        license_check = input("\nDoes the driver have a valid license? (yes/no): ")
        if license_check.lower() == "no":
            total_fine = total_fine + 5000
            violations_list = violations_list + "* No Valid License (Fine: Rs 5000)\n"
            print("❌ Fine Added: Rs 2000 for No License.")
        else:
            print("✅ Checked: Driver has a valid license.")

        # 4. Drunk Driving Check
        drunk_check = input("\nIs the driver under the influence of alcohol? (yes/no): ")
        if drunk_check.lower() == "yes":
            total_fine = total_fine + 10000
            violations_list = violations_list + "* Drunk Driving (Fine: Rs 10000)\n"
            print("❌ DANGER! Fine Added: Rs 10000 for Drunk Driving.")
        else:
            print("✅ Checked: Driver is sober.")

    # ----------------- FINAL CHALLAN RECEIPT -----------------
    print("\n==============================================")
    type_effect("       CHALLANSWIFT DIGITAL RECEIPT v4.0  ", 0.04)
    print("==============================================")
    print(f"On-Duty Officer : {officer_name}")
    print(f"Driver Name     : {driver_name}")
    print(f"Vehicle Number  : {vehicle_number}")
    if emergency_check.lower() == "yes":
        print("Vehicle Status  : EMERGENCY OVERRIDE")
    else:
        if vehicle_type == "1":
            print("Vehicle Type    : Two-Wheeler (Bike)")
        else:
            print("Vehicle Type    : Four-Wheeler (Car)")
    print("----------------------------------------------")
    print("Violations/Status:")
    print(violations_list if violations_list != "" else " * NO VIOLATIONS! Safe Driver Award! ⭐")
    print("----------------------------------------------")
    print(f"TOTAL PENALTY AMOUNT TO PAY: Rs {total_fine}")
    print("==============================================")
    
    # Loop control: Poochhna ki agla challan kaatna hai ya nahi
    print("\n----------------------------------------------")
    system_active = input("Do you want to log another vehicle? (yes/no): ")

print("\nExiting ChallanSwift System. Data successfully compiled. Drive safe! 🚑⚡")