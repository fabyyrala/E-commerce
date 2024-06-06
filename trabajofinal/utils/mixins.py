from django.shortcuts import render, redirect

class VerificarPermisosMixins:
    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.is_staff and not self.request.user.is_superuser:
            return redirect("error_permisos")
            
        return super(VerificarPermisosMixins, self).dispatch(request, *args, **kwargs)