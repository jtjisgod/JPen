import sys
import socket
import dns.resolver

import JThread      # Simple Thread Module

class JDns :

    types = {
        0 : "target",
        1 : "cname",
        2 : "a"
    }

    def __init__(self, domain, dnsServer = "8.8.8.8", lifeTime = 10, timeOut = 10) :
        self.domain = domain
        self.dnsServer = dnsServer
        self.lifeTime = lifeTime
        self.timeOut = timeOut
        self.domains = []
    
    def run(self) :
        return self.dns(self.domain)
    
    def dns(self, domain) :
        resolver = dns.resolver.Resolver()
        resolver.timeout = self.timeOut
        resolver.lifetime = self.lifeTime
        resolver.nameservers = [socket.gethostbyname(self.dnsServer)]
        domains = [(0, domain)]
        while True:
            try :
                answer = resolver.query(domain, 'CNAME')
                for rdata in answer :
                    domain = str(rdata.target)
                domains.append((1, domain.strip(".")))
            except :
                break
        try :
            answer = resolver.query(domain, 'A')
            for rdata in answer :
                ip = str(rdata.address)
                domains.append((2, ip))
        except :
            # domains.append([])
            pass
        self.domains = domains
        return domains

    def pretty(self) :
        l = []
        for domain in self.domains :
            try :
                l.append("[ %s ] %s"%(self.types[domain[0]].upper(), domain[1]))
            except :
                pass
        return "\n => ".join(l)