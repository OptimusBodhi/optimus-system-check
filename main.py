import functions_framework

@functions_framework.http
def system_check_ok(request):
    """A simple HTTP function for testing deployment."""
    return ("--- Optimus AI OS: Core System Deployment Check... SUCCESS ---", 200)
