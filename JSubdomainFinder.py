import JDns
import JThread      # Simple Thread Module
import JFIO

class JSubdomainFinder :

    def __init__(self, domain, dnsServer = "8.8.8.8", lifeTime = 10, timeOut = 10, dictionary="./assets/subdomains/subdomains-1000.txt") :
        self.domain = domain
        self.dictionary = dictionary

    def generateDomains(self) :
        subdomains = JFIO.readFile2Line(self.dictionary)
        domains = []
        for subdomain in subdomains :
            if not subdomain.strip() :
                continue
            domains.append(self.domain.replace("*", subdomain))
        return domains
    
    def isExist(self, domain) :
        print("Checking ... %s"%(domain))
        mJDns = JDns.JDns(domain)
        mJDns.run()
        if len(mJDns.domains) <= 1 :
            return False
        return True

    def run(self) :
        if "*" not in self.domain :
            print("Error... Please input wildcard make ( * )")
            return
        domains = self.generateDomains()
        mJThread = JThread.JThread(self.isExist, domains, count=100)
        mJThread.run()
        self.response = mJThread.getResponse()
        return self.response

if __name__ == "__main__" :
    print(">>")
    mJSubdomainFinder = JSubdomainFinder("*.naver.com")
    mJSubdomainFinder.run()