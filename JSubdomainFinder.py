import JDns
import JThread      # Simple Thread Module
import JFIO
import JEnum
import pickle
import os

class JSubdomainFinder :

    def __init__(self, domain, dnsServer = "8.8.8.8", lifeTime = 10, timeOut = 10, dictionary="./assets/subdomains/subdomains-1000.txt") :
        self.domain = domain
        self.dictionary = dictionary
        self.total = 0
        self.progress = 0
        self.binFile = "./assets/domains/%s.bin"%(self.domain.split("*.")[1])

    def generateDomains(self) :
        subdomains = JFIO.readFile2Line(self.dictionary)
        domains = []
        for subdomain in subdomains :
            if not subdomain.strip() :
                continue
            domains.append(self.domain.replace("*", subdomain))
        return domains
    
    def isExistSubdomain(self, domain) :
        mJDns = JDns.JDns(domain)
        mJDns.run()
        self.progress += 1
        print("[ %.2f%s ] Checking ... %s"%((self.progress/self.total*100), "%", domain))
        return mJDns.domains
        # if len(mJDns.domains) <= 1 :
        #     return False
        # return True
    
    def isExist(self) :
        try :
            with open(self.binFile, "rb") as f :
                return pickle.load(f)
        except :
            return {}

    def run(self) :

        if "*" not in self.domain :
            print("Error... Please input wildcard make ( * )")
            return

        domains = self.generateDomains()

        self.total = len(domains)
        self.progress = 0

        mJThread = JThread.JThread(self.isExistSubdomain, domains, count=250)
        mJThread.run()
        self.response = mJThread.getResponse()

        with open(self.binFile, "wb") as f :
            pickle.dump(self.response, f)
                    
        return self.response

if __name__ == "__main__" :
    print(">>")
    mJSubdomainFinder = JSubdomainFinder("*.google.com")
    mJSubdomainFinder.run()