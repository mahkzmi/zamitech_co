from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


class DemoForm(forms.Form):
    PRODUCT_CHOICES = [
        ('', '-- انتخاب محصول --'),
        ('abaak', 'آباک - تحلیل خاک هوشمند'),
        ('fertility', 'توصیه کودی هوشمند'),
        ('growth-iot', 'پایش رشد گیاه (IoT)'),
        ('all', 'پکیج کامل زامیتک'),
    ]

    fullname = forms.CharField(
        label='نام کامل',
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-xl border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition',
            'placeholder': 'نام و نام خانوادگی'
        }),
        max_length=100,
        required=True
    )

    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={
            'class': 'w-full rounded-xl border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition',
            'placeholder': 'example@zamitech.ir'
        }),
        required=True
    )

    phone = forms.CharField(
        label='شماره تماس',
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-xl border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition',
            'placeholder': '۰۹۱۲۱۲۳۴۵۶۷'
        }),
        max_length=15,
        required=True
    )

    company = forms.CharField(
        label='نام شرکت/مزرعه',
        widget=forms.TextInput(attrs={
            'class': 'w-full rounded-xl border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition',
            'placeholder': 'نام شرکت یا مزرعه شما'
        }),
        max_length=100,
        required=False
    )

    product = forms.ChoiceField(
        label='محصول مورد نظر',
        choices=PRODUCT_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full rounded-xl border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition'
        }),
        required=True
    )

    message = forms.CharField(
        label='توضیحات اضافه',
        widget=forms.Textarea(attrs={
            'class': 'w-full rounded-xl border border-gray-300 p-3 focus:outline-none focus:ring-2 focus:ring-green-500 focus:border-transparent transition',
            'placeholder': 'در صورت نیاز توضیحات بیشتری بنویسید...',
            'rows': 4
        }),
        required=False
    )

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # حذف همه کاراکترهای غیر عددی
        phone = re.sub(r'[^\d]', '', phone)
        
        # بررسی معتبر بودن شماره تلفن ایرانی
        if not re.match(r'^(\+98|0)?9\d{9}$', phone):
            raise ValidationError('لطفاً یک شماره تلفن همراه معتبر وارد کنید')
        
        return phone

    def clean_email(self):
        email = self.cleaned_data['email']
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError('لطفاً یک ایمیل معتبر وارد کنید')
        
        return email