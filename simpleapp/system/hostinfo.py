import socket

class HostInfo:
    @staticmethod
    def get_ip():
        return socket.gethostbyname(socket.gethostname())

    @staticmethod
    def gethostname():
        return socket.gethostname()