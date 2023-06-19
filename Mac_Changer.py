#!/usr/bin env python
import subprocess
import optparse
import re

def get_argrument():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="To set the interface")
    parser.add_option("-m", "--mac", dest="mac", help="To change mac adderss")
    (opt, arg) = parser.parse_args()
    if not opt.interface:
        parser.error("[-] Not specified interface, use --help for more info ")
    elif not opt.mac:
        parser.error("[-] Not specified mac address, use --help for more info ")
    return opt

def mac_changer(interface, mac):
    print("[+] changing mac_addr for " + interface + " to " + mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])

def Print_Mac (interface):
    ifconfig_output = subprocess.check_output(["ifconfig", interface])
    Regx_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_output))
    if Regx_result:
        return Regx_result.group(0)
        #return ("New MAc_address = " + Regx_result.group(0))
    else:
        print("[-] Could not find Mac_address")

opt=get_argrument()
Current_Mac = Print_Mac(opt.interface)
print("old_Mac = "+ str(Current_Mac))
mac_changer(opt.interface, opt.mac)

Current_Mac = Print_Mac(opt.interface)
if Current_Mac == opt.mac:
    print("[+] Mac_address was successfully changed to " + Current_Mac)
else:
    print("[-] Mac_address was failed to change ")







