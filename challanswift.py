# Project: ChallanSwift v6.0 | Final Production Build
import time
import sys
import random # Random Receipt ID ke liye

def type_effect(text, speed=0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# ----------------- MAIN PROGRAM v6.0 -----------------
type_effect("\n=== Welcome to CHALLANSWIFT v6.0: Final Production Build ===", 0.05)
type_effect("------------------------------------------------------------", 0.05)

officer_name = input("Enter On-Duty Officer Name: ")

total_vehicles_logged = 0
total_revenue_collected = 0

system_active = "yes"

while system_active.lower() == "yes" or system_active.lower() == "y":
    print("\n============================================================")
    print("                     NEW CHALLAN ENTRY                      ")
    print("============================================================")
    
    driver_name = input("Enter Driver Name: ")
    vehicle_number = input("Enter Vehicle Number: ")

    emergency_check = input("\nIs this an Emergency Vehicle? (yes/no): ")

    total_fine = 0
    violations_list = ""

    if emergency_check.lower() == "yes":
        print("\n🚨 EMERGENCY VEHICLE DETECTED! Penalties waived automatically. 🚨")
        violations_list = "* EMERGENCY VEHICLE OVERRIDE (Fine: Rs 0)\n"
    else:
        print("\nSelect Vehicle Type:")
        print("[1] Two-Wheeler (Bike/Scooty)")
        print("[2] Four-Wheeler (Car/SUV)")
        vehicle_type = input("Enter choice (1 or 2): ")

        print("\n--- Checking for traffic violations ---")

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

        speed = int(input("\nEnter vehicle speed (Limit is 60 km/h): "))
        if speed > 60:
            total_fine = total_fine + 2000
            violations_list = violations_list + "* Over-speeding (Fine: Rs 2000)\n"
            print(f"❌ Fine Added: Rs 2000 for Over-speeding ({speed} km/h).")
        else:
            print(f"✅ Checked: Speed is under control ({speed} km/h).")

        license_check = input("\nDoes the driver have a valid license? (yes/no): ")
        if license_check.lower() == "no":
            total_fine = total_fine + 5000
            violations_list = violations_list + "* No Valid License (Fine: Rs 5000)\n"
            print("❌ Fine Added: Rs 5000 for No License.")
        else:
            print("✅ Checked: Driver has a valid license.")

        drunk_check = input("\nIs the driver under the influence of alcohol? (yes/no): ")
        if drunk_check.lower() == "yes":
            total_fine = total_fine + 10000
            violations_list = violations_list + "* Drunk Driving (Fine: Rs 10000)\n"
            print("❌ DANGER! Fine Added: Rs 10000 for Drunk Driving.")
        else:
            print("✅ Checked: Driver is sober.")

    total_vehicles_logged = total_vehicles_logged + 1
    total_revenue_collected = total_revenue_collected + total_fine

    # Payment Mode Feature
    payment_mode = "N/A"
    if total_fine > 0:
        print("\nSelect Payment Mode:")
        print("[1] Cash")
        print("[2] UPI / QR Code")
        print("[3] Credit/Debit Card")
        pay_choice = input("Enter choice (1-3): ")
        if pay_choice == "1": payment_mode = "Cash"
        elif pay_choice == "2": payment_mode = "UPI"
        elif pay_choice == "3": payment_mode = "Card"

    # Random Receipt ID Generation
    receipt_id = f"CS-{random.randint(10000, 99999)}"

    # ----------------- FINAL CHALLAN RECEIPT -----------------
    print("\n==============================================")
    type_effect(f"   CHALLANSWIFT DIGITAL RECEIPT ({receipt_id})  ", 0.04)
    print("==============================================")
    print(f"On-Duty Officer : {officer_name}")
    print(f"Driver Name     : {driver_name}")
    print(f"Vehicle Number  : {vehicle_number}")
    print(f"Payment Method  : {payment_mode}")
    print("----------------------------------------------")
    print("Violations/Status:")
    print(violations_list if violations_list != "" else " * NO VIOLATIONS! Safe Driver Award! ⭐")
    print("----------------------------------------------")
    print(f"TOTAL PENALTY AMOUNT TO PAY: Rs {total_fine}")
    print("==============================================")
    
    print("\n----------------------------------------------")
    system_active = input("Do you want to log another vehicle? (yes/no): ")

print("\n==============================================")
type_effect("       ⚡ END OF SHIFT SUMMARY REPORT ⚡     ", 0.04)
print("==============================================")
print(f"On-Duty Officer       : {officer_name}")
print(f"Total Vehicles Checked : {total_vehicles_logged}")
print(f"Total Fine Collected  : Rs {total_revenue_collected}")
print("==============================================")
type_effect("ChallanSwift System Closed. Deployment Successful! 🚦🚗", 0.04)