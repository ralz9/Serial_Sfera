from django.core.mail import send_mail

def send_activation_code(email, code):
    send_mail(
        'Activation code',
        f'Привет перейди по ссылке что бы активировать аккаунт http://localhost:8000/api/v1/account/activate/{code}',
        'RodionDereha@gmail.com',
        [email]
    )