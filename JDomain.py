import copy

class JDomain :
    def __init__(self, domains) :
        self.rawDomains = copy.deepcopy(domains)
        self.domain = {
            "parent" : [], # Parent domain list
            "child" : [] # Child domain list = All of domains
        }
        for domain in self.rawDomains :
            if domain == "" :
                continue
            if "*" in domain :
                self.domain['parent'].append(domain)
            else :
                self.domain['child'].append(domain)
                        
