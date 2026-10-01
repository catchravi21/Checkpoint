# Checkpoint
Checkpoint related script
# Check Point Firewall Health Check

A SecureCRT Python script that runs a set of operational health checks on a
connected Check Point firewall. It sends each command to the active terminal
session in sequence, with a one-second pause between commands.

## Requirements

- SecureCRT with Python scripting support
- An active SSH or terminal session to a Check Point firewall
- A user account with permission to run the listed commands

This script uses SecureCRT's built-in `crt` scripting interface and is intended
to be run from SecureCRT's Script menu. It is not a standalone Python script.

## Health checks

| Command | Purpose |
| --- | --- |
| `cpstat os -f cpu` | CPU performance metrics |
| `cpstat os -f memory` | Memory allocation breakdown |
| `cpstat os -f multi_cpu` | CoreXL per-core processing distribution |
| `cpstat fw` | Firewall core engine health |
| `fw stat` | Active security policy and installation information |
| `fw tab -s -t connections` | Active connection table totals and historical peak |
| `fw ctl multik stat` | CoreXL kernel instance load-balancer status |
| `cpstat ha` | High Availability cluster synchronization status |
| `cpstat vpn` | VPN software blade and active tunnel status |
| `cpwd_admin list` | Check Point process watchdog status |
| `cplic print` | Installed licenses and service contract entitlements |

The descriptions above document the checks in the script; only the commands
are sent to the firewall. Display labels are deliberately not written to the
terminal, as the firewall CLI would interpret them as commands.

## Usage

1. Connect to the Check Point firewall in SecureCRT.
2. Open the SecureCRT Script menu and run `checkpoint_health.py`.
3. Review the command output in the terminal session.

The script checks that a session is connected before starting. It enables
SecureCRT synchronous screen handling while sending the commands and waits one
second after each command before sending the next. This is a fixed delay, not a
check that the previous command has completed; if a command takes longer to
finish, output may overlap with the next command.


thank you