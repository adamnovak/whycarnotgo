#!/usr/bin/env python2.7

"""
whycarnotgo.py: Use Python-OBD to report the Diagnostic Trouble Codes (DTC) from a vehicle.
"""

import obd

def main():
    print(obd.OBD().query(obd.commands.GET_DTC).value)

def clear():
    obd.OBD().query(obd.commands.CLEAR_DTC)
    print("DTC codes cleared")

if __name__ == "__main__":
    main()
