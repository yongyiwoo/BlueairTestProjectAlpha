import socket

class ServoControl(object):
    """
    as a client send request to the server (Arduino MKR WIFI 1010) to control the servo motor through socket
    the servers are pre defined to have static IP addresses and ports, as well as pins to control different servo motors
    Classic server IP: 192.168.1.101:65000; WiFi pin: 6; Fan Speed pin: 7; Auto pin: 8; Filter pin: 5
    Sense+ server IP: 192.168.1.102:65000; WiFi pin: 6; Fan Speed pin: 7; Filter pin: 8
    G4 server IP: 192.168.1.103:65000; Switch pin: 6; Auto pin: 7; Fan Speed pin: 8; Germ pin: 4; WiFi pin: 5
    B4 server IP: 192.168.1.103:65000; Switch pin: 6; Fan Speed pin: 7

    Bytes meaning:
    b"1SPRS": 1 second press (normal press)
    b"3SPRS": 3 seconds press (enable wifi pairing mode auto/manual)
    b"10SPRS": 10 seconds press (reset filter classic/sense+)
    b"15SPRS": 15 seconds press (reset filter b4)
    b"30SPRS": 30 seconds press (enable failsafe mode)
    b4 factory reset?
    """
    @staticmethod
    def servo_control(ip: str, port: int, bytestr: bytes):
        """
        send byte string to the server and receive response
        :param ip: server IP address
        :param port: server port
        :param bytestr: byte string, e.g. b"3SPRS\n"
        :return: a message consists bytes
        """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((ip, port))
            s.sendall(bytestr)
            data = s.recv(1024)
        return data
