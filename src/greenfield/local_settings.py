import ldap, logging
import os
from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

AUTH_LDAP_SERVER_URI="ldaps://dc"
#AUTH_LDAP_BIND_DN = "cn=Administrator,cn=Users,dc=openforce,dc=org"
AUTH_LDAP_BIND_DN = "Administrator@OPENFORCE.ORG"
AUTH_LDAP_BIND_PASSWORD = "Abc123!"
AUTH_LDAP_USER_SEARCH = LDAPSearch("cn=Users,dc=openforce,dc=org", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")

AUTHENTICATION_BACKENDS = [
    'django_auth_ldap.backend.LDAPBackend',
]
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    'is_staff': 'cn=Staff,cn=Users,dc=openforce,dc=org',
    'is_superuser': 'cn=Superusers,cn=Users,dc=openforce,dc=org'
}
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("cn=Users,dc=openforce,dc=org", ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE=ActiveDirectoryGroupType()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'greenfield',
        'USER': 'greenfield',
        'PASSWORD': 'greenfield',
        'HOST': 'postgres',
        'PORT': 5432,
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
