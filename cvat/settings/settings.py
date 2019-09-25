from cvat.settings.production import *

# add custom apps here
import ldap
from django_auth_ldap.config import LDAPSearch, PosixGroupType

DJANGO_AUTH_TYPE = 'LDAP'
AUTH_LOGIN_NOTE = '''<p>
    Please use your LDAP login credentials (the ones you use to login system-wide).
</p>'''

# Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldap://192.168.2.128:389"

# Credentials for LDAP server
AUTH_LDAP_BIND_DN = "cn=admin,dc=jonas,dc=host"
AUTH_LDAP_BIND_PASSWORD = "AlchemY08"

# Set up basic user search
AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=jonas,dc=host",
    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")

# Set up the basic group parameters.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("ou=groups,dc=jonas,dc=host",
    ldap.SCOPE_SUBTREE, "(objectClass=posixGroup)")
AUTH_LDAP_GROUP_TYPE = PosixGroupType()

# Populate the Django user from the LDAP directory.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
}

AUTH_LDAP_ALWAYS_UPDATE_USER = True

# Cache group memberships for an hour to minimize LDAP traffic
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600
AUTH_LDAP_AUTHORIZE_ALL_USERS = True
#AUTH_LDAP_FIND_GROUP_PERMS = True
# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS += ['django_auth_ldap.backend.LDAPBackend']

AUTH_LDAP_ADMIN_GROUPS = [
    'cn=admin,dc=jonas,dc=host',
]

AUTH_LDAP_ANNOTATOR_GROUPS = [
    'cn=user,dc=jonas,dc=host',
]

AUTH_LDAP_USER_GROUPS = [
    'cn=user,dc=jonas,dc=host',
]

AUTH_LDAP_OBSERVER_GROUPS = [
    'cn=user,dc=jonas,dc=host',
]
