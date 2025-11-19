'''
    icmplib
    ~~~~~~~

    Easily forge ICMP packets and make your own ping and traceroute.

        https://github.com/ValentinBELYN/icmplib

    :copyright: Copyright 2017-2023 Valentin BELYN.
    :license: GNU LGPLv3, see the LICENSE for details.

    ~~~~~~~

    Example: interface binding
'''

from icmplib import ping, multiping


# Ping with interface binding
# Bind to loopback interface (Linux only)
host = ping('127.0.0.1', count=4, interface='lo')

print(host.is_alive)
# True


# Ping via specific network interface (Linux only)
# Common interface names: lo, eth0, wlan0, ens33, etc.
# You can list interfaces with: ip link show

# Uncomment and adjust the interface name to test:
# host = ping('8.8.8.8', count=4, interface='eth0')
# print(host.is_alive)
# True


# Multiping with interface binding (Linux only)
addresses = ['127.0.0.1', '::1']
hosts = multiping(addresses, count=2, interface='lo')

for host in hosts:
    print(host.address, host.is_alive)

# 127.0.0.1 True
# ::1 True
