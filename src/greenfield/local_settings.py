import ldap, logging
from django_auth_ldap.config import LDAPSearch, ActiveDirectoryGroupType

logger = logging.getLogger('django_auth_ldap')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)

AUTH_LDAP_SERVER_URI="ldaps://127.0.0.1"
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
        'PASSWORD': 'Secret012',
        'HOST': '127.0.0.1',
        'PORT': 5432,
    }
}
