from django.shortcuts import redirect

def LoginMiddleWare(get_response):
    # One-time configuration and initialization.

    excluded_paths = ['login', 'register']

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        current_path = request.path


        current_path_start = request.path.split('/')[1]

        print(current_path_start)

        if current_path_start not in excluded_paths:
            print(request.user.is_authenticated)
            if not request.user.is_authenticated:
                # user is not authenticated
                return redirect('/login')

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware

# ABouttgerw23@me#