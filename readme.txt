sessionDemo
    request.session["user_id"] = user.pk
    request.session["user_name"] = user.name

    if request.session.get("user_id"):
        request.session.get("user_name")