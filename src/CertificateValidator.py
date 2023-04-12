from OpenSSL import SSL
from cryptography.x509 import Certificate
import idna
import socket
from datetime import datetime

from utils.enums.network import CertificateType


class CertificateValidator:
    @staticmethod
    def get_certificate(ip_address, port) -> Certificate:
        hostname_idna = idna.encode(ip_address)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((ip_address, port))
            ctx = SSL.Context(SSL.SSLv23_METHOD)  # most compatible
            ctx.check_hostname = False
            ctx.verify_mode = SSL.VERIFY_NONE

            sock_ssl = SSL.Connection(ctx, sock)
            sock_ssl.set_connect_state()
            sock_ssl.set_tlsext_host_name(hostname_idna)
            sock_ssl.do_handshake()
            cert = sock_ssl.get_peer_certificate()
            crypto_cert = cert.to_cryptography()

        return crypto_cert

    @staticmethod
    def is_expired(cert: Certificate) -> bool:
        return cert.not_valid_after < datetime.now()

    @staticmethod
    def validate(ip_address, port) -> CertificateType:
        cert = CertificateValidator.get_certificate(ip_address, port)
        valid = not CertificateValidator.is_expired(cert)

        return CertificateType.VALID if valid else CertificateType.INVALID


certificate_validator = CertificateValidator()
