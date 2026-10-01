# $language = "Python"
# $interface = "1.0"

# Description: List unused objects in the Check Point Management database.
# Run from a SecureCRT session connected to the Management Server.


def main():
    if not crt.Session.Connected:
        crt.Dialog.MessageBox("Error: Connect to the Check Point Management Server first.")
        return

    objScreen = crt.Screen
    objScreen.Synchronous = True
    try:
        objScreen.Send(
            "mgmt_cli -r true show unused-objects limit 500 offset 0 --format json\r"
        )
    finally:
        objScreen.Synchronous = False


main()
