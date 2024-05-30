from app import ft, PHONE_HEIGHT, PHONE_WIDTH
from app.style import *
from typing import Optional
from app.api import (
    AuthAPI
)
from app.hook import (
    AuthHook
)

from app.util import (
    LocalStore
)


class AuthUI(ft.Container):
    def __init__(self, page: Optional[ft.Page] = None, **kwargs):
        super().__init__(**kwargs)
        self.height = PHONE_HEIGHT
        self.width = PHONE_WIDTH
        self.bgcolor = BG
        self.border_radius=30
        self.page = page
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=self.init_form(),
                    margin=ft.margin.only(top=200),
                    padding=ft.padding.all(20),
                )
            ],
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        
    def init_form(self):
        self.signin_text = ft.Text(
            value="Đăng nhập, chào mừng bạn quay trở lại!",
            color=PRIORITY,
            text_align=ft.TextAlign.CENTER,
            size=20,
            width=self.width,
        )
        self.username_txtfield = ft.TextField(
            value="",
            bgcolor=WRAPPER,
            label="Tên đăng nhập",
            border_color=BG_SEC1,
        )
        self.password_txtfield = ft.TextField(
            value="",
            bgcolor=WRAPPER,
            label="Mật khẩu",
            border_color=BG_SEC1,
            password=True,
        )

        self.email = ft.TextField(
            value="",
            bgcolor=WRAPPER,
            label="Email",
            border_color=BG_SEC1,
        )

        self.fullname = ft.TextField(
            value="",
            bgcolor=WRAPPER,
            label="Họ và tên",
            border_color=BG_SEC1,
        )

        self.phone = ft.TextField(
            value="",
            bgcolor=WRAPPER,
            label="Số điện thoại",
            border_color=BG_SEC1,
        )
        
        # Button initialization
        self.signin_btn = ft.ElevatedButton(
            text="Đăng nhập",
            bgcolor=BG_SEC1,
            color=PRIORITY,
            height=50,
            on_click=self.on_submit
        )
        
        # Loading indicator (initially hidden)
        self.loading_indicator = ft.Text(
            value="Loading...",
            color=PRIORITY,
            visible=False
        )
        
        self.forgotpw_text_button = ft.TextButton(
            text="Quên mật khẩu?",
            on_click=lambda e: self.page.go('/forgot-password')
        )
        
        self.register_text_button = ft.TextButton(
            text="Chưa có tài khoản?",
            on_click=lambda e: self.page.go('/sign-up') if self.page.route != '/sign-up' else self.page.go('/sign-in')
        )
        
        self.extra_section = ft.Row(
            controls=[
                self.forgotpw_text_button,
                self.register_text_button
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        
        if self.page.route == '/sign-up':
            self.signin_text.value = 'Đăng ký tài khoản'
            self.signin_btn.text = 'Đăng ký'
            self.register_text_button.text = 'Đã có tài khoản?'
            self.email.visible = True
            self.fullname.visible = True
            self.phone.visible = True
            self.extra_section = ft.Row(
                controls=[
                    self.register_text_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        elif self.page.route == '/sign-in':
            self.signin_text.value = 'Đăng nhập, chào mừng bạn quay trở lại!'
            self.signin_btn.text = 'Đăng nhập'
            self.email.visible = False
            self.fullname.visible = False
            self.phone.visible = False
            self.extra_section = ft.Row(
                controls=[
                    self.forgotpw_text_button,
                    self.register_text_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        elif self.page.route == '/forgot-password':
            self.signin_text.value = 'Quên mật khẩu?'
            self.signin_btn.text = 'Gửi'
            self.username_txtfield.label = 'Email'
            self.username_txtfield.value = ''
            self.username_txtfield.hint_text = 'Nhập email của bạn'
            self.password_txtfield.visible = False
            self.email.visible = False
            self.fullname.visible = False
            self.phone.visible = False
            self.extra_section = ft.Row(
                controls=[
                    self.register_text_button
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            )
        self.page.update()
        
        return ft.Column(
            controls=[
                self.signin_text,
                self.username_txtfield,
                self.password_txtfield,
                self.email,
                self.fullname,
                self.phone,
                ft.Row(  # Add a Row to hold the button and loading indicator
                    controls=[
                        self.signin_btn,
                        self.loading_indicator
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                self.extra_section
            ],
            spacing=10,
        )
        
    def on_submit(self, event):
        # 'Sign in button clicked')
        # Disable the button and show loading indicator
        if self.page.route == '/sign-up':
            self.handle_signup()
        elif self.page.route == '/sign-in':
            self.handle_signin()
        else:
            self.handle_forgot_password()
        

    def handle_signin(self):
        self.signin_btn.visible = False
        self.loading_indicator.visible = True
        self.page.update()
        
        
        username = self.username_txtfield.value
        password = self.password_txtfield.value
        
        # Fetch token
        if AuthAPI.check_auth() == False:
            data_fetch_token = AuthAPI.get_token({
                'username': username,
                'password': password
            })
            LocalStore.set_data(data_fetch_token, 'token')



        token = LocalStore.get_data(key='access', filename='token')
        # 'Token fetched', token)
        data_fetch_profile = AuthAPI.get_user_by_token(token)
        LocalStore.set_data(data_fetch_profile, 'profile')

        profile = LocalStore.get_data(key='data', filename='profile')

        try:
            if profile and profile.get('username') == username:
                self.page.go('/')
                AuthHook.set_authenticated(profile)
        except:
            pass
        finally:
            # Re-enable the button and hide loading indicator
            self.signin_btn.visible = True
            self.loading_indicator.visible = False
            self.page.update()

    def handle_signup(self):
        self.signin_btn.visible = False
        self.loading_indicator.visible = True
        self.page.update()
        
        username = self.username_txtfield.value
        password = self.password_txtfield.value
        email = self.email.value
        fullname = self.fullname.value
        phone = self.phone.value
        
        data = {
            'username': username,
            'password': password,
            'email': email,
            'full_name': fullname,
            'phone': phone
        }
        
        response = AuthAPI.sign_up(data)
        if response.get('code') == 'res_success':
            self.page.go('/sign-in')
        
        self.signin_btn.visible = True
        self.loading_indicator.visible = False
        self.page.update()

    def handle_forgot_password(self):
        self.signin_btn.visible = False
        self.loading_indicator.visible = True
        self.page.update()
        
        email = self.username_txtfield.value
        response = AuthAPI.forgot_password({
            'email': email
        })
        if response.get('code') == 'res_success':
            self.signin_text.value = 'Mật khẩu đã được gửi đến ' + email + '. Vui lòng kiểm tra email của bạn.' 
            self.page.go('/sign-in')
        
        self.signin_btn.visible = True
        self.loading_indicator.visible = False
        self.page.update()