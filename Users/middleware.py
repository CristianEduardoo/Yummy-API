import datetime
from django.conf import settings
from django.contrib.auth import logout
from django.utils.deprecation import MiddlewareMixin


class AutoLogoutMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if not request.user.is_authenticated:
            return

        current_time = datetime.datetime.now().timestamp()  # Convertir a timestamp
        last_activity = request.session.get("last_activity")

        if last_activity:
            elapsed_time = current_time - last_activity
            if elapsed_time > 300:  # 5 minutos
                logout(request)
                return

        request.session["last_activity"] = current_time  # Almacenar el timestamp
