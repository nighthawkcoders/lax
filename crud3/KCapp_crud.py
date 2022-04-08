
flask_login.login_required

@app_crud.route('/')
@login_required
def crud():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud.html", table=users_all())


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('crud.crud_login'))
