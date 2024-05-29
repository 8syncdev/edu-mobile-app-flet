from app import (
    ft,
    BASE_DIR,
    PHONE_HEIGHT,
    PHONE_WIDTH
)

from app.style import *
from typing import (
    Optional,
    Literal,
    Dict,
    Any
)

from app.screens.main_ui.pages.main_page import MainPage
from app.screens.main_ui.pages.fg_page import FgPage




class MainUI(ft.Container):
    def __init__(self, page: Optional[ft.Page] = None, **kwargs):
        super().__init__(**kwargs)
        self.height = PHONE_HEIGHT
        self.width = PHONE_WIDTH
        self.page = page
        self.bgcolor = BG
        self.border_radius=30
        self.content = ft.Container(
            height=PHONE_HEIGHT,
            width=PHONE_WIDTH,
            content=ft.Stack(
                controls=[
                    self.init_ui_fgpage(),
                    ft.Column(
                        controls=[
                            ft.Row(
                                controls=[
                                    self.init_ui_homepage()
                                ],
                                alignment='end',
                                width=PHONE_WIDTH,
                                height=PHONE_HEIGHT-60,
                            ),
                            self.init_ui_navbarbottom(),
                        ],
                    )
                ],
                height=PHONE_HEIGHT,
            )
        )

    def init_ui_navbarbottom(self):
        style_navbarbottom = {
            'color': PRIORITY,
            'size': 30,
        }
        self.ui_navbarbottom  = ft.Row(
            controls=[
                ft.Container(
                    on_click=lambda e: self.page.go('/'),
                    content=ft.Icon(
                        ft.icons.HOME,
                        **style_navbarbottom
                    )
                ),
                ft.Container(
                    on_click=lambda e: self.page.go('/course/3'),
                    content=ft.Icon(
                        ft.icons.BOOKMARK,
                        **style_navbarbottom
                    ),
                ),
                ft.Container(
                    on_click=lambda e: self.page.go('/course/3'),
                    content=ft.Icon(
                        ft.icons.CONTACT_SUPPORT_OUTLINED,
                        **style_navbarbottom
                    ),
                ),
                ft.Container(
                    on_click=lambda e: self.select_route(),
                    content=ft.Icon(
                        ft.icons.SETTINGS,
                        **style_navbarbottom
                    )
                ),
            ],
            width=PHONE_WIDTH,
            alignment='spaceAround',
        )

        return self.ui_navbarbottom

    def init_ui_navbar(self):
        self.ui_navbar = ft.Row(
            controls=[
                ft.Container(
                    on_click=lambda e: self.shrink(e),
                    content=ft.Icon(
                        ft.icons.MENU,
                        color=PRIORITY,
                    )
                ),
                ft.Row(
                    controls=[
                        ft.Container(
                            content=ft.Icon(
                                ft.icons.SEARCH,
                                color=PRIORITY,
                            )
                        ),
                        ft.Container(
                            content=ft.Icon(
                                ft.icons.NOTIFICATIONS,
                                color=PRIORITY,
                            )
                        ),
                    ]
                )
            ],
            alignment='spaceBetween',
            height=40,
        )

        return self.ui_navbar
    
    def init_ui_fgpage(self):
        self.container_fgpage = FgPage(master=self, page=self.page)
        return self.container_fgpage
    

    def init_ui_homepage(self):
        self.container_mainpage = MainPage(master=self, page=self.page)
        return self.container_mainpage
    
    def shrink(self, e):
        self.container_mainpage.width = 120
        self.container_mainpage.bgcolor=BG_SEC2
        self.container_mainpage.scale = ft.transform.Scale(
            0.8,
            alignment=ft.alignment.center_right
        )
        self.container_mainpage.border_radius=ft.border_radius.only(
            top_left=30,
            top_right=0,
            bottom_left=30,
            bottom_right=0
        )
        self.container_mainpage.update()

    
    def restore(self, e):
        self.container_mainpage.width = 400
        self.container_mainpage.bgcolor=BG
        self.container_mainpage.border_radius = 35
        self.container_mainpage.scale = ft.transform.Scale(

        1,alignment=ft.alignment.center_right)
        self.container_mainpage.update()

    def select_route(self):
        route_name = self.page.route
        print(route_name)