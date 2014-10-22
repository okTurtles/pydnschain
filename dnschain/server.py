import json, urllib2

from log import LoggingMixin


class MalformedJSON(Exception):
    pass


class DataNotFound(Exception):
    def __init__(self, HTTP404Error, name, blockchain):
        self.code = 404
        self.msg = "The name: %s was not found in the queried blockchain: %s."\
                   % (name, blockchain)
        self.hdrs = HTTP404Error.hdrs
        self.fp = HTTP404Error.fp
        self.filename = HTTP404Error.filename


class Server(LoggingMixin):
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
        self._logger_helper(__name__)
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
            if e.code == 404:
                e = DataNotFound(e, name, self.headers['Host'])
            if e.code < 200 or e.code > 299:
                self._log.debug("Raised: '%s', for reason '%s'." % (e, e.msg), exc_info=True)
                raise e

        namecoin_string = response.read()
        try:
            data = json.loads(namecoin_string)
        except ValueError:
            raise MalformedJSON("%s\n%s" % (ValueError, namecoin_string))
        return data


if __name__ == '__main__':
    DNSChainServer = Server("192.184.93.146", "NOTYETIMPLEMENTED")#Seems to coerce to https. 443?
    #DNSChainServer = Server("dns.dnschain.net", "NOTYETIMPLEMENTED")
    print DNSChainServer.lookup("id/greg")
    print DNSChainServer.lookup("d/greg")
    #print DNSChainServer.lookup("greg")
    DNSChainServer.lookup("id/OAUF:EUIERPEWEOPHOUH:QBP&(@PG$UFR:G//DFUhSUG")
