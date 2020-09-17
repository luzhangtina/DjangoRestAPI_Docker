from django.contrib.auth.models import Group

import logging

logger = logging.getLogger(__name__)

class UserGroupPermission():
    def hasPermissionForTheAction(self, user, viewAction):
        logger.info(user.groups.all())
        return Group.objects.get(name=viewAction) in user.groups.all()
