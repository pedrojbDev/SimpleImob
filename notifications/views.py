# notifications/views.py
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .forms import NotificationForm
from django.core.mail import send_mail

def notification_request_view(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid() and form.cleaned_data['notify']:
            # Enviar email
            subject = 'Notificação Solicitada'
            message = 'Você solicitou uma notificação. Aqui está sua mensagem.'
            recipient_list = ['pedrojesuinobatista@gmail.com']

            send_mail(
                subject,
                message,
                'seu_email@example.com',  # Email remetente
                recipient_list,
            )

            # Redirecionar para uma página de sucesso
            return redirect('success_url')
    else:
        form = NotificationForm()

    return render(request, 'notifications/notification_form.html', {'form': form})

def success_view(request):
    return render(request, 'success.html')