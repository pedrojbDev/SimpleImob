from django.core.mail import send_mail

def send_email_notification(subject, message, recipient_list):
    from_email = 'pedrojesuinobatista@gmail.com'  # você pode usar DEFAULT_FROM_EMAIL
    send_mail(subject, message, from_email, recipient_list)