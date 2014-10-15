import json


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

    def lookup(self, name):
        """
        Looks up a name from the DNSChain server. Throws exception if the
        data is not valid JSON or if the namecoin entry does not exist in the
        blockchain.

        @param name: The name to lookup, e.g. 'id/dionyziz'
        """

        # namecoin_string = read_from_dnschain(name)
        data = json.loads(namecoin_string)
        return data
