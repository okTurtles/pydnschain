import mock
import unittest

import dnschain
from dnschain.server import Server

import json

class TestServerInstantiation(unittest.TestCase):

    @mock.patch('dnschain.server.urllib2.urlopen')
    def setUp(self, mock_opener):
        self.mock_opener = mock_opener
        self.assertIs(dnschain.server.urllib2.urlopen, self.mock_opener)
        self.dnschain_server = Server("0.0.0.0", "FAKEFINGERPRINT")

    def test_invalid_address(self):
        pass

    def test_invalid_fingerprint(self):
        pass

    def test_invalid_domain_name(self):
        pass

    def test_valid_address_and_fingerprint(self):
        pass


class TestServerLookup(unittest.TestCase):

    @mock.patch('dnschain.server.json.loads')
    @mock.patch('dnschain.server.urllib2.urlopen')
    def setUp(self, mock_opener, mock_json_loads):
        self.mock_opener = mock_opener
        self.assertIs(dnschain.server.urllib2.urlopen, self.mock_opener)
        self.dnschain_server = Server("0.0.0.0", "FAKEFINGERPRINT")
        self.dnschain_server.lookup("greg")

    def test_validrequest(self):
        print self.mock_opener

    def test_handle_nonascii_response(self):
        pass

    def test_no_match(self):
        pass


class TestDNSChainLookup(unittest.TestCase):

    def setUp(self):
        self.dnschain_server = Server("192.184.93.146", "NOTYETIMPLEMENTED")
        self.test_cases = {"id/dionyziz": "dionyziz@gmail.com",
                           "id/greg": ["contact@taoeffect.com", "hi@okturtles.com"]}
        self.responses = {}
        for name in self.test_cases:
            self.responses[name] = self.dnschain_server.lookup(name)
        
    def test_valid_JSON(self):
        for response in self.responses.itervalues():
            try:
                json.dumps(response)
            except:
                self.fail("Response was not in valid JSON format")
        
    def test_contains_email(self):
        for response in self.responses.itervalues():
            self.assertIn("email", response)

    def test_correct_email(self):
        for name in self.test_cases:
            if "email" not in self.responses[name]:
                self.skipTest('Response does not contain key "email"')
            self.assertEqual(self.test_cases[name], 
                             self.responses[name]["email"])


# class MaybeSubClassingIsTheCleanestWayForward

if __name__ == '__main__':
    unittest.main()
