from citi_digits.service import MembershipService

__author__ = 'vikash'

from models import CityDigitsUser as User

class CityDigitsBackend(object):
    """
     Custom Authorization Backend
    """
    def authenticate(self,role=None, username=None, password=None):
        try:
            # Try to find a user matching your username and role
            #default to role TEACHER if no role is passed
            if(not role):
                role = "TEACHER"
            user = User.objects.get(username=username,role=role)
            #check password
            if user.is_admin:
                password = MembershipService.encryptPassword(username,password)
            if password == user.password:
                return user
            else:
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None