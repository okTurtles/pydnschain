import json, urllib2, logging

class MalformedJSON(Exception):
    pass

class Server:
    """
    A connection to a DNSChain server.
    """

    def __init__(self, addr, fingerprint, http_host_header='namecoin.dns'):
        """
        Store configuration for requests to a DNSChain server.

        @param addr: The address of the trusted DNSChain server (IP or hostname)
        TODO: May need port here?
        @param fingerprint: The key fingerprint of the DNSChain server, for connection authorization
        """

        self.addr = addr
        self.fingerprint = fingerprint
        self.headers = {'Host': http_host_header}#Per http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html

    def lookup(self, name, host_override=None):
        """
        Looks up a name from the DNSChain server. Throws exception if the
        data is not valid JSON or if the namecoin entry does not exist in the
        blockchain.

        @param name: The name to lookup, e.g. 'id/dionyziz', note this $NAMESPACE/$NAME
        format is not guaranteed.  Additionally the caller must perform appropriate url
        encoding _before_ the name is passed to urllib2.urlopen
        """
        if host_override is not None:
            self.headers['Host'] = host_override
        full_url = "http://%s/%s" % (self.addr, name)
        request = urllib2.Request(full_url, None, self.headers)
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError, e:
            if e.reason == "Not Found":
                logging.log(1, "The name: %s was not found in the database, raised %s." % (name, e))
                raise e

        namecoin_string = response.read()
        try:
            data = json.loads(namecoin_string)
        except ValueError, e:
                raise MalformedJSON("%s\nData Follows:\n'''\n%s\n'''" % (e, namecoin_string))
        return data


if __name__ == '__main__':
    DNSChainServer = Server("192.184.93.146", "NOTYETIMPLEMENTED")#Seems to coerce to https. 443?
    #DNSChainServer = Server("dns.dnschain.net", "NOTYETIMPLEMENTED")
    print DNSChainServer.lookup("id/greg")
    print DNSChainServer.lookup("d/greg")
    #print DNSChainServer.lookup("greg")
    print DNSChainServer.lookup("id/OAUF:EUIERPEWEOPHOUH:QBP&(@PG$UFR:G//DFUhSUG")
