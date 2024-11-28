from django import forms

class ContactForm(forms.Form):
    # html側のデータを取得
    name = forms.CharField(label='お名前')
    email = forms.EmailField(label='メールアドレス')
    title = forms.CharField(label='件名')
    message = forms.CharField(label='メッセージ',widget=forms.Textarea)

    # 初期化メソッド
    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder']= '名前'
        self.fields['name'].widget.attrs['class']= 'form-control'

        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレス'        
        self.fields['email'].widget.attrs['class'] = 'form-control'

        self.fields['title'].widget.attrs['placeholder']= 'タイトル'
        self.fields['title'].widget.attrs['class'] = 'form-control'

        self.fields['message'].widget.attrs['placeholder']= 'メッセージ'
        self.fields['message'].widget.attrs['class'] = 'form-control'