import httplib
import socket


class RokuConnector(object):
    """
    Manages connection to the Roku player.
    """

    def __init__(self, roku_ip):
        self._ip = roku_ip


    def ip(self):
        """
        gets the IP of the current Roku player.

        @returns Roku IP
        """

        return self._ip


    def send_key_cmd(self, cmd_string):
        """
        Sends a command to the Roku.

        @param cmd_string Command to send
        @returns True if send successfully, False otherwise
        """

        try:
            uri = '%s:8060' % self._ip
            conn = httplib.HTTPConnection(uri)
            command = '/keypress/%s' % cmd_string
            conn.request('POST', command)
            conn.close()
            return True
        except socket.error:
            return False
