__author__ = 'vikash'
"""
 This program will generate a password.
 Usage is :
 python password_generator <username> <password>
"""
import sys

def generatePassword(username,password):
    import hashlib
    hexDigest = hashlib.sha512('{%s}%s'%(username,password))
    password = hexDigest.hexdigest()
    return password

if __name__ == "__main__":
    if len(sys.argv) <2:
        print "USAGE: python password_generator username password"
    else:
        print "NEW PASSWORD HASH: %s" % (generatePassword(sys.argv[1],sys.argv[2]))
