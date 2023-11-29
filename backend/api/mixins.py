from rest_framework import permissions

from .permissions import IsStaffEditorPermission


# can use this custom permission in any view that want the permission
class StaffEditorPermissionMixin():
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]



# only the user can see his added data
class UserQuerySetMixin():
    user_field = 'user'
    #  indicates whether staff users can view all objects or not.(This attribute can be overridden by subclasses to change the behavior.)
    allow_staff_view = False

    def get_queryset(self, *args, **kwargs):
        user = self.request.user
        # This variable will store the key-value pair that will be used to filter the queryset by the user field.
        lookup_data = {}

        # assigns the value of self.request.user to the key that corresponds to the value of self.user_field in the lookup_data dictionary.
        # {'user': self.request.user} 
        lookup_data[self.user_field] = user

        qs = super().get_queryset(*args, **kwargs)
        
        # if user allow_staff_view=True and user is staff:
        if self.allow_staff_view and user.is_staff:
            return qs

        # The ** operator unpacks the dictionary into keyword arguments, so that each key-value pair matches the corresponding field name and value in the model.
        return qs.filter(**lookup_data)