# $language = "Python"
# $interface = "1.0"

# Description: Automated Check Point Gateway Health Check Script
# This script sends health commands sequentially with minor delays.

import time

def main():
    # Verify there is an active connection before running commands
    if not crt.Session.Connected:
        crt.Dialog.MessageBox("Error: You must be connected to a session to run this script.")
        return

    # Turn on Synchronous mode to prevent typing overlaps
    objScreen = crt.Screen
    objScreen.Synchronous = True

    health_checks = {
        "cpstat os -f cpu": "CPU Performance Metrics",
        "cpstat os -f memory": "Memory Allocation Breakdown",
        "cpstat os -f multi_cpu": "CoreXL Individual Core Processing Distribution",
        "cpstat fw": "Firewall Core Engine Health",
        "fw stat": "Active Security Policy Verification & Install Date",
        "fw tab -s -t connections": "Active Connection Table Totals and Historical Peak",
        "fw ctl multik stat": "CoreXL Kernel Instances Load Balancer Status",
        "cpstat ha": "High Availability Cluster Protocol Synchronization Status",
        "cpstat vpn": "VPN Software Blade & Active Tunnel Volume Status",
        "cpwd_admin list": "Check Point Internal Daemons Watchdog Monitoring Process",
        "cplic print": "Installed System Licenses & Service Contract Entitlements"
    }

    # Execute only the health-check commands; labels sent with Screen.Send are
    # interpreted by the firewall CLI as commands rather than display-only text.
    for cmd in health_checks:
        objScreen.Send(cmd + "\r")

        # Allow command output time to finish printing before continuing
        time.sleep(1)

    # Clean up and restore default screen handling
    objScreen.Synchronous = False

main()
