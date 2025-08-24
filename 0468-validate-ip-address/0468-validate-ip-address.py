class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        ipv4 = queryIP.split('.')
        ipv6 = queryIP.split(':')

        if len(ipv4) == 4:
            for ip in ipv4:
                val = 0
                if not ip:
                    return "Neither"
                for idx, c in enumerate(ip):
                    if ord('0') <= ord(c) <= ord('9'):
                        if idx > 0 and val == 0:
                            return 'Neither'
                        val = val * 10 + int(c)
                    else:
                        return 'Neither'
                if val > 255:
                    return 'Neither'
            return 'IPv4'

        elif len(ipv6) == 8:
            for ip in ipv6:
                if not ip or len(ip) > 4:
                    return 'Neither'
                for c in ip:
                    if not (ord('0') <= ord(c) <= ord('9') or ord('a') <= ord(c.lower()) <= ord('f')):
                        return 'Neither'
            return 'IPv6'
        else:
            return 'Neither'