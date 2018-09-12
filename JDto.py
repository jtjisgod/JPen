import JDns
import JThread      # Simple Thread Module
import JFIO
import pickle
import JEnum
import os
import requests

class JDto :

    vulnUrls = {"createsend":"https://www.zendesk.com/",
        "cargocollective":"https://cargocollective.com/",
        "cloudfront":"https://aws.amazon.com/cloudfront/",
        "desk.com":"https://www.desk.com/",
        "fastly.net":"https://www.fastly.com/",
        "feedpress.me":"https://feed.press/",
        "ghost.io":"https://ghost.org/",
        "github.io":"https://pages.github.com/",
        "helpjuice.com":"https://helpjuice.com/",
        "helpscoutdocs.com":"https://www.helpscout.net/",
        "herokudns.com":"https://www.heroku.com/",
        "herokussl.com":"https://www.heroku.com/",
        "herokuapp.com":"https://www.heroku.com/",
        "jetbrains.com":"https://myjetbrains.com/",
        "pageserve.co":"https://instapage.com/",
        "pingdom.com":"https://www.pingdom.com/",
        "amazonaws.com":"https://aws.amazon.com/s3/",
        "myshopify.com":"https://www.shopify.com/",
        "stspg-customer.com":"https://www.statuspage.io/",
        "sgizmo.com":"https://www.surveygizmo.com/",
        "surveygizmo.eu":"https://www.surveygizmo.com//",
        "sgizmoca.com":"https://www.surveygizmo.com/",
        "teamwork.com":"https://www.teamwork.com/",
        "tictail.com":"https://tictail.com/",
        "tumblr.com":"https://www.tumblr.com/",
        "unbouncepages.com":"https://unbounce.com/",
        "uservoice.com":"https://www.uservoice.com/",
        "bitbucket":"https://bitbucket.org/",
        "unbounce.com":"https://unbounce.com/",
        "vend":"https://vendcommerce.com/",
        "zendesk.com":"https://www.zendesk.com/",
        "bitbucket.io":"https://bitbucket.io",
        "cloudapp.net":"https://cloudapp.net",
        "trafficmanager.net":"https://trafficmanager.net",
        "cloudfront.net":"https://aws.amazon.com/ko/cloudfront/",
        "azurewebsites.net":"https://portal.azure.com",
        "core.windows.net":"https://portal.azure.com",
        "cloudapp.azure.com":"https://portal.azure.com",
        "updatemyprofile.com":"https://updatemyprofile.com",
        "heroku": "heroku", 
        "zendesk": "zendesk", 
        "bitbucket": "bitbucket",
        "shopify": "shopify",
        "teamwork": "teamwork",
        "unbounce": "unbounce",
        "github": "github",
        "helpjuice": "helpjuice",
        "helpscout": "helpscout",
        "cargocollective": "cargocollective",
        "statuspage": "statuspage",
        "tumblr": "tumblr"
        }    

    response=["<strong>Trying to access your account",
                "Use a personal domain name",
                "The request could not be satisfied",
                "Sorry, We Couldn't Find That Page",
                "Fastly error: unknown domain",
                "The feed has not been found",
                "You can claim it now at",
                "Publishing platform",                        
                "There isn't a GitHub Pages site here",
                "<title>No such app</title>",                        
                "No settings were found for this company",
                "<title>No such app</title>",
                "is not a registered InCloud YouTrack.",
                "You've Discovered A Missing Link. Our Apologies!",
                "Sorry, couldn&rsquo;t find the status page",                        
                "NoSuchBucket",
                "Sorry, this shop is currently unavailable",
                "<title>Hosted Status Pages for Your Company</title>",
                "data-html-name=\"Header Logo Link\"",                        
                "<title>Oops - We didn't find your site.</title>",
                "class=\"MarketplaceHeader__tictailLogo\"",                        
                "Whatever you were looking for doesn't currently exist at this address",
                "The requested URL was not found on this server",
                "The page you have requested does not exist",
                "This UserVoice subdomain is currently available!",
                "but is not configured for an account on our platform",
                "Looks like you've traveled too far into cyberspace.",
                "<title>Help Center Closed | Zendesk</title>",
                "Built for professional teams"]

    def __init__(self, domain) :
        self.domain = domain
        self.binFile = JEnum.dto + domain + ".bin"
        self.binDomain = JEnum.domains + domain + ".bin"

    def getHTML(self, url) :
        try :
            return requests.get("http://" + url, timeout=3)
        except :
            try :
                return requests.get("https://" + url, timeout=3)
            except :
                return ""
        return ""
    
    def check(self, domain) :
        res = self.getHTML(domain)
        for response in self.response :
            if response in res :
                return True
        return False

    def run(self) :
        dto = {}
        try :
           dnsInformation = JFIO.readPickle(self.binDomain)
        except :
            return False
        
        domains = []
        for domain in dnsInformation :
            if len(dnsInformation[domain]) <= 1 :
                continue
            domains.append(domain)

        mJThread = JThread.JThread(self.check, domains, 200)
        mJThread.run()
        exploitable = mJThread.response

        print(exploitable)

        return exploitable
