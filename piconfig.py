#!/usr/bin/python

import sys, os, fileinput, getpass

# Check that 2 arguments are passed and that they are correct-ish
if len(sys.argv) != 2:
    print "Die Die Die";
    exit()
elif sys.argv[1] == "--help":
    print "This is the help\n"
    exit()
elif os.path.exists(sys.argv[1]) == False:
    print "Path", sys.argv[1], "does not exist.\n"
    exit()

# Check to see if we enable ssh 
enable_ssh = raw_input( "> Enable SSH yes(y) or no(n)? [y] ")
if enable_ssh == "y":
    if(os.path.exists(''.join([sys.argv[1],"/etc/rc2.d/K01ssh"]))):
        os.rename(''.join([sys.argv[1],"/etc/rc2.d/K01ssh"]),''.join([sys.argv[1],"/etc/rc2.d/S02ssh"]))

# Check to see if we enable wifi 
enable_wifi = raw_input( "> Enable Wifi yes(y) or no(n)? [y] ")

if enable_wifi == "y":
    # Check to see if we enable wifi 
    wifi_ssid = raw_input( "> Enter the SSID of your wifi router.> ")
    wifi_psk = getpass.getpass("> Enter the Password of your wifi router.> ")

    with open(''.join([sys.argv[1],"/etc/wpa_supplicant/wpa_supplicant.conf"]), 'a') as file:
        file.write("\n")
        file.write("network={\n")
        file.write(''.join(['    ssid="',wifi_ssid,'"',"\n"]));
        file.write(''.join(['    psk="',wifi_psk,'"',"\n"]));
        file.write("}\n\n")