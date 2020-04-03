try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

import os
import uuid
from flask import request,redirect,url_for,abort,flash,current_app
from flask_login import current_user
from functools import wraps

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_IMAGE_EXTENSIONS']

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

def random_filename(filetype):
    ext = filetype
    return uuid.uuid4().hex+ext

def redirect_back(default='main.index', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))

def permission_required(permission_name):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            if current_user.role != 3:
                abort(403)
            return func(*args, **kwargs)
        return decorated_function
    return decorator

def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))


def admin_required(func):
    return permission_required(3)(func)