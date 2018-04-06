from django.core.exceptions import PermissionDenied
from restrict.models import RestrictInfrastructure

def restrict_infrastructure(title):

    def _method_wrapper(view_method):

        def _arguments_wrapper(request, *args, **kwargs) :
            """
            Wrapper with arguments to invoke the method
            """

            entry = RestrictInfrastructure.objects.get(title=title)
            print title
            print entry.is_hidden
            if not entry.is_hidden:
                return view_method(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return _arguments_wrapper

    return _method_wrapper