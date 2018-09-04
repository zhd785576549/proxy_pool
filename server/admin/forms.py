from wtforms import Form, BooleanField, StringField, PasswordField, validators


class AdminLoginForm(Form):

    username_validators = [
        validators.DataRequired(message="用户名不能为空"),
        validators.length(5, 20, "用户名必须5~20个字符")
    ]

    password_validators = [
        validators.DataRequired(message="密码不能为空"),
        validators.length(6, 20, "密码必须6~20个字符")
    ]

    username = StringField("username", validators=username_validators)
    password = StringField("password", validators=password_validators)
