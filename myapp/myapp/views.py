from django.shortcuts import render


def custom_page_not_found(request, exception):
    """
    Custom 404 error view.
    """
    return render(request, '404.html', status=404)

