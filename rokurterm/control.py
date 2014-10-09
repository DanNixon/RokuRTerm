import httplib
import socket

class RokuConnector(object):

    def __init__(self, roku_ip):
        self._ip = roku_ip

    def ip(self):
        return self._ip

    def send_key_cmd(self, cmd_string):
        try:
            uri = '%s:8060' % self._ip
            conn = httplib.HTTPConnection(uri)
            command = '/keypress/%s' % cmd_string
            conn.request('POST', command)
            conn.close()
            return True
        except socket.error:
            return False
