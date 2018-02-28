import requests


class RokuConnector(object):
    """
    Manages connection to the Roku player.
    """

    def __init__(self, ip):
        self.ip = ip
        self.uri = 'http://{}:8060'.format(self.ip)


    def send_key_cmd(self, cmd_string):
        """
        Sends a command to the Roku.

        @param cmd_string Command to send
        @returns True if send successfully, False otherwise
        """
        command = '{}/keypress/{}'.format(self.uri, cmd_string)
        r = requests.post(command)
        return r.ok
