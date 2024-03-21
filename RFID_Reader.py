from __future__ import print_function
import qwiic_rfid
import time
import sys


def run_example():
    print("\nSparkFun Qwiic RFID Reader Example 1")
    my_RFID = qwiic_rfid.QwiicRFID()

    if not my_RFID.begin():
        print("\nThe Qwiic RFID Reader isn't connected to the system. Please check your connection", file=sys.stderr)
        return

    print("\nReady to scan some tags!")

    while True:
        val = input("\nEnter 1 to get tag ID and scan time: ")

        if int(val) == 1:
            print("\nGetting your tag ID...")
            tag = my_RFID.get_tag()
            print("\nTag ID: " + tag)

            scan_time = my_RFID.get_prec_req_time()
            # If this time is too precise, try:
            # scan_time = my_RFID.get_req_time()
            print("\nScan Time: " + str(scan_time))

        time.sleep(0.02)


if __name__ == '__main__':
    try:
        run_example()
    except (KeyboardInterrupt, SystemExit) as exErr:
        print("\nEnding Example 1")
        sys.exit(0)
