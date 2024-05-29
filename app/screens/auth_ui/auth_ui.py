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
        self.page = page
        self.content = ft.Column(
            controls=[
                ft.Container(
                    content=self.init_form(),
                    margin=ft.margin.only(top=200),
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
        
        self.forgotpw_text = ft.TextButton(
            text="Quên mật khẩu?",
        )
        
        self.register_text = ft.TextButton(
            text="Chưa có tài khoản?",
        )
        
        self.extra_section = ft.Row(
            controls=[
                self.forgotpw_text,
                self.register_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
        
        return ft.Column(
            controls=[
                self.signin_text,
                self.username_txtfield,
                self.password_txtfield,
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
        # Disable the button and show loading indicator
        self.signin_btn.visible = False
        self.loading_indicator.visible = True
        self.page.update()
        
        
        username = self.username_txtfield.value
        password = self.password_txtfield.value
        
        if LocalStore.get_data('access', 'token') == None:
            data_fetch_token = AuthAPI.get_token({
                'username': username,
                'password': password
            })
            LocalStore.set_data(data_fetch_token, 'token')
            # print(1)
        else:
            # print(2)
            ...
        token = LocalStore.get_data(key='access', filename='token')
        
        if LocalStore.get_data('data', 'profile') == None:
            data_fetch_profile = AuthAPI.get_user_by_token(token)
            LocalStore.set_data(data_fetch_profile, 'profile')
            # print(3)
        else:
            # print(4)
            ...
        profile = LocalStore.get_data(key='data', filename='profile')
        # print(profile)
        try:
            if profile and profile.get('username') == username:
                AuthHook.set_authenticated(profile)
                self.page.go('/')
            ...
        except:
            pass
        finally:
            # Re-enable the button and hide loading indicator
            self.signin_btn.visible = True
            self.loading_indicator.visible = False
            self.page.update()
