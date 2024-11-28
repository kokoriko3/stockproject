from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.urls import reverse_lazy

class ContactView(FormView):
    template_name = 'contact.html'
    form_class =ContactForm
    success_url = reverse_lazy('contact:contacts')

    def form_valid(self, form):
        # 入力されたデータを取得
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        title = form.cleaned_data['title']
        message = form.cleaned_data['message']

        # メールのタイトルの書式を設定
        subject = 'お問い合わせ:{}'.format(title)

        # フォームの入力データの書式を設定 ※教科書のバックスラッシュは改行の意
        message = '送信者名:{0}\nメールアドレス:{1}\nタイトル:{2}\nメッセージ:{3}'.format(name, email, title, message)

        # 送信元のアドレス
        from_email = 'admin@example.com'

        # 送信先のアドレス
        to_list = ['admin@example.com']

        # EmailMessageオブジェクトを生成
        message = EmailMessage(subject=subject,
                               body=message,
                               from_email=from_email,
                               to=to_list,
                                )
        # EmailMessageクラスのsend()でメール送信
        message.send()
        # 送信完了後のメッセージ
        messages.success(self.request, 'お問い合わせ結果は正常に送信されました')

        return super().form_valid(form)