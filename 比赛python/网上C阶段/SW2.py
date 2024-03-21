# $language = "python"
# $interface = "1.0"

# This automatically generated script may need to be
# edited in order to work correctly.

def Main():
# --------- 
	crt.Screen.Synchronous = True
	crt.Screen.Send(chr(26))
	crt.Screen.WaitForString("#")
	crt.Screen.Send("\n")
	crt.Screen.WaitForString("#")

	crt.Screen.Send("terminal length 0" + "\n")
	crt.Screen.WaitForString("#")
# ---------
	crt.Session.LogFileName = "D:/soft/scripts/SW-2-vlan.txt"
	crt.Session.Log(True)

	crt.Screen.Send("show vlan" + "\n")
	
	crt.Screen.WaitForString("#")
	crt.Session.Log(False)
# ---------
	crt.Session.LogFileName = "D:/soft/scripts/SW-2-interface.txt"
	crt.Session.Log(True)

	crt.Screen.Send("show interface ethernet status" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show run int e1/0/27 | include bandwidth" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ip vrf cw" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show int e1/0/27" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show run int vl 4094 | include mtu" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show port-group 1 brief" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show run | include load-balance" + "\n")


	crt.Screen.WaitForString("#")
	crt.Session.Log(False)
# ---------
	crt.Session.LogFileName = "D:/soft/scripts/SW-2-server.txt"
	crt.Session.Log(True)

	crt.Screen.Send("show run | include snmp" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show lldp" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show lldp neighbors brief " + "\n")

	crt.Screen.WaitForString("#")
	crt.Session.Log(False)
# ---------
	crt.Session.LogFileName = "D:/soft/scripts/SW-2-ospf.txt"
	crt.Session.Log(True)

	crt.Screen.Send("show ip ospf database" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ip ospf interface" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ip route ospf" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ipv6 ospf route" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ip route  ospf" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ip route ospf | include 0.0.0.0" + "\n")


	crt.Screen.WaitForString("#")
	crt.Session.Log(False)
# ---------
	crt.Session.LogFileName = "D:/soft/scripts/SW-2-bgp.txt"
	crt.Session.Log(True)

	crt.Screen.Send("show ip bgp" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ip route bgp" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show run router bgp | include dampening" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ip route bgp" + "\n")

	crt.Screen.WaitForString("#")
	crt.Session.Log(False)
# ---------
	crt.Session.LogFileName = "D:/soft/scripts/SW-2-ospfxl.txt"
	crt.Session.Log(True)

	crt.Screen.Send("show ip route ospf | include 10.50.12.0" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ipv6 route | include 2001:10:50:22" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ipv6 route | include 2001:10:50:32" + "\n")
	crt.Screen.WaitForString("#")
	crt.Screen.Send("show ipv6 route | include 2001:10:50:52" + "\n")

	crt.Screen.WaitForString("#")
	crt.Session.Log(False)
# ---------
	crt.Session.LogFileName = "D:/soft/scripts/SW-2-run.txt"
	crt.Session.Log(True)

	crt.Screen.Send("show run" + "\n")


	crt.Screen.WaitForString("#")
	crt.Session.Log(False)
# ---------
Main()
