from django.contrib.auth import backends


class MongoEngineBackend(object):
    """Authenticate using MongoEngine and mongoengine.django.auth.User.
    """

    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    authenticate = backends.ModelBackend.__dict__["authenticate"]
    get_user = backends.ModelBackend.__dict__["get_user"]
