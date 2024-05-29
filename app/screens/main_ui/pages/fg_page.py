
from app import (
    ft,
    BASE_DIR,
    PHONE_HEIGHT,
    PHONE_WIDTH
)

from app.style import *

from typing import (
    Optional,
    Literal
)

from app.util import (
    LocalStore
)

from app.hook import (
    AuthHook
)


CircleCustom = ft.Stack(
    controls=[
        ft.Container(
        width=100,
        height=100,
        border_radius=50,
        bgcolor='white12'
        ),
        ft.Container(
            gradient=ft.SweepGradient(
                center=ft.alignment.center,
                start_angle=0.0,
                end_angle=3,
                stops=[0.5,0.5],
            colors=['#00000000', BG_SEC1],
            ),
            width=100,
            height=100,
            border_radius=50,
            content=ft.Row(alignment='center',
                controls=[
                    ft.Container(
                        padding=ft.padding.all(5),
                        bgcolor=BG,
                        width=90,height=90,
                        border_radius=50,
                        content=ft.Container(
                            bgcolor=FG,
                            height=80,width=80,
                            border_radius=40,
                            content=ft.Image(
                                src='brand/brand-14.png',
                                width=80,height=80, 
                                fit=ft.ImageFit.COVER
                            ),
                        )
                    )
                ],
            ),
        ),
      
    ]
  )



class FgPage(ft.Container):
    def __init__(self, 
                 master: Optional[ft.Container] = None, 
                 page: Optional[ft.Page] = None,
                 **kwargs
                ):
        super().__init__(**kwargs)
        self.master = master #* dont use parent, because it is default property of the container
        self.page = page
        self.height = PHONE_HEIGHT
        self.width = PHONE_WIDTH
        self.bgcolor = BG
        self.border_radius=30
        self.padding = ft.padding.only(left=10,top=20,right=140)
        self.animate = ft.animation.Animation(600, ft.AnimationCurve.DECELERATE)
        self.animate_scale = ft.animation.Animation(400, ft.AnimationCurve.DECELERATE)

        self.size_fgpage = PHONE_WIDTH - 140
        self.content = ft.Column(
            controls=[
                self.init_ui_backnav(),
                self.init_ui_userinfo(),
            ]
        )
        #* Get data user
    
    def restore(self, e):
        self.master.restore(e)

    def init_ui_backnav(self):
        self.ui_backnav = ft.Row(
            controls=[
                ft.Container(
                    border_radius=25,
                    padding=ft.padding.only(
                    top=8,left=13,),
                    height=50,
                    width=50,
                    border=ft.border.all(color='white',width=1),
                    on_click=lambda e: self.restore(e),
                    content=ft.Text('<', size=20, color=PRIORITY)
                )
            ],
            alignment='end'
        )

        return self.ui_backnav
    
    def init_ui_userinfo(self):
        style_button_nav = {
            'color': PRIORITY,
            'bgcolor': BG,
            'on_hover': self.on_hover_btnmenubar,
            'width': 160,
            'height': 35,
        }


        self.ui_userinfo = ft.Column(
            controls=[
                CircleCustom,
                ft.Text(
                    value="Chào mừng bạn quay trở lại, "+ AuthHook.get_user()['username'],
                    size=20,
                    color=PRIORITY,
                ),
                #* Div wrap button, nghĩ đơn giản là div chứa button đang dùng flex
                ft.Column(
                    controls=[
                        ft.Column(
                            controls=[
                                ft.ElevatedButton(
                                    text="Trang chủ",
                                    icon=ft.icons.HOME,
                                    **style_button_nav,
                                    on_click=lambda e: self.navigate_to('/')
                                ),
                                ft.ElevatedButton(
                                    text="Khóa học",
                                    icon=ft.icons.BOOKMARK,
                                    **style_button_nav,
                                    on_click=lambda e: self.navigate_to('/course/3')
                                ),
                                ft.ElevatedButton(
                                    text="Liên hệ",
                                    icon=ft.icons.MAIL,
                                    **style_button_nav,
                                    on_click=lambda e: self.navigate_to('/contact'),
                                ),
                                ft.ElevatedButton(
                                    text="Bio",
                                    icon=ft.icons.WORK_OUTLINE,
                                    **style_button_nav,
                                    on_click=lambda e: self.navigate_to('/contact'),
                                ),
                            ]
                        ),
                        ft.Column(
                            controls=[
                                ft.ElevatedButton(
                                    text="Đăng xuất",
                                    icon=ft.icons.LOGOUT,
                                    **style_button_nav,
                                    on_click=lambda e: self.navigate_to('/')
                                ),
                                ft.Container(
                                    content=ft.Image(
                                        src='admin/admin-logo.png',
                                        height=80,
                                    )
                                ),
                                ft.Row(
                                    controls=[
                                        ft.Container(
                                            content=ft.Image(
                                                src='admin/contact/facebook.png',
                                                height=60
                                            )
                                        ),
                                        ft.Container(
                                            content=ft.Image(
                                                src='admin/contact/tiktok.png',
                                                height=60
                                            )
                                        ),
                                        ft.Container(
                                            content=ft.Image(
                                                src='admin/contact/youtube.png',
                                                height=60
                                            )
                                        ),
                                    ],
                                    alignment='center',
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                        ),
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=self.size_fgpage,
                    alignment='spaceBetween',
                    height=500,
                )
            ]
        )

        return self.ui_userinfo
    
    def on_hover_btnmenubar(self, e: ft.HoverEvent):
        #* Get data from Main UI, Main UI control homepage control ui sections.
        # self.master.container_homepage.all_ui_controls
        e.control.bgcolor = BG_SEC1 if e.data=='true' else BG
        e.control.icon_color = PRIORITY if e.data=='true' else BG_SEC1
        e.control.update()

    def navigate_to(self, 
            path_route: Optional[Literal[
                '/',
            ]]='/',
        ):
        self.page.go(path_route)
            