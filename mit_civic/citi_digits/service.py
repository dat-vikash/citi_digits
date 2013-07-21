"""
 This class contains services for domain entities
"""
from django.contrib.auth import authenticate
from django.db import transaction

class MembershipService():
    """
     Membership related services
    """

    @staticmethod
    def encryptPassword(salt, raw_password):
        """
          This function encrypts the user's password using a salt and a sha512 hexdigest in the format
          hexdigest({salt}password)
        """
        import hashlib
        hexDigest = hashlib.sha512('{%s}%s'%(salt,raw_password))
        password = hexDigest.hexdigest()
        return password

    @staticmethod
    def authenticate(role,username,password):
        """
          This function authenticates a user and returns a user object or None
        """
        user = authenticate(role=role,username=username,password=MembershipService.encryptPassword(username,password))
        return user


