import ipaddress
class Solution:
    def validIPAddress(self, IP: str) -> str:
        try:
            ip = ipaddress.ip_address(IP)
            if "." in IP:
                arr = IP.split(".")
                if len(arr) != 4:
                    return "Neither"
                for part in arr:
                    if part[0] == "0" and len(part) != 1:
                        return "Neither"
            if ":" in IP:
                arr = IP.split(":")
                print(arr)
                if len(arr) != 8 or "" in arr:
                    return "Neither"
            return "IPv" + str(ip.version)
        except ValueError:
            return "Neither"