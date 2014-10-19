import json, urllib, httplib


class Server:
    """
    A connection to a DNSChain server.
    """

    def __init__(self, addr, fingerprint):
        """
        Initializes a connection to a DNSChain server.

        @param addr: The address of the trusted DNSChain server (IP or hostname)
        TODO: May need port here?
        @param fingerprint: The key fingerprint of the DNSChain server, for connection authorization
        """

        self.addr = addr
        self.fingerprint = fingerprint
        self.connection = httplib.HTTPConnection(addr)

    def lookup(self, name):
        """
        Looks up a name from the DNSChain server. Throws exception if the
        data is not valid JSON or if the namecoin entry does not exist in the
        blockchain.

        @param name: The name to lookup, e.g. 'id/dionyziz'
        """
        #uname = name.encode("utf-8")#Who knows what bytes will be submitted?! Look up dnschain spec.
        url_safe_name = urllib.quote(name, safe="") #Meant to be a url path _component_.
        path = "/id/%s" % (url_safe_name,)
        self.connection.request("GET", path)
        namecoin_response = self.connection.getresponse()
        namecoin_string = namecoin_response.read()
        try:
            data = json.loads(namecoin_string)
        except ValueError, e:
            if namecoin_string.startswith("Not Found: "):
                print "The name: %s was not found in the database, returning None." % (url_safe_name)
                return None
            else:
                print "Instead of JSON we got this:\n%s\n" % (e,)
                import sys
                sys.exit(99) #Fail hard.
        return data


if __name__ == '__main__':
    #DNSChainServer = Server("192.184.93.146", "NOTYETIMPLEMENTED")#Seems to coerce to https. 443?
    DNSChainServer = Server("dns.dnschain.net", "NOTYETIMPLEMENTED")
    print DNSChainServer.lookup("greg")
    print DNSChainServer.lookup("OAUF:EUIERPEWEOPHOUH:QBP&(@PG$UFR:G//DFUhSUG")
