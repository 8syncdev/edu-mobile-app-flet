
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

from app.util import LocalStore

from app.api import CourseAPI

from app.schema import (
    get_brand_imagpath,
    get_tech_imagpath,
    get_with_relativename
)

from typing import (
    Literal,
    Dict,
    List
)

import math

from datetime import datetime


class MainPage(ft.Container):
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
        self.padding = ft.padding.only(left=10,top=20,right=10)
        self.animate = ft.animation.Animation(600, ft.AnimationCurve.DECELERATE)
        self.animate_scale = ft.animation.Animation(400, ft.AnimationCurve.DECELERATE)

        #* Global variable
        self.label_map_level = {
            'foudation': 'Nền tảng',
        }

        self.content = ft.Column(
            controls=[
                self.init_ui_navbar(),
                self.select_ui()
            ],
            height=PHONE_HEIGHT-60,
            scroll=ft.ScrollMode.AUTO,
        )

        # print(LocalStore.get_data('access', 'token'))


    def shrink(self, e):
        self.master.shrink(e) #* Overriding the shrink method from the parent class, from MainUI class

    def init_ui_navbar(self):
        return self.master.init_ui_navbar() #* Overriding the init_ui_navbar method from the parent class, from MainUI class
    
    def init_ui_intro_content(self):
        data_all_courses = CourseAPI.get_all_courses().get('results')
        # print(data_all_courses.get('results'))
        list_card_items = [
             ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Container(
                                    content=ft.Image(
                                        src=get_with_relativename(item_card.get('title')),
                                    ),
                                    bgcolor=ft.colors.WHITE,
                                    width=50,
                                    height=50,
                                    padding=ft.padding.all(5),
                                    border_radius=10
                                ),
                                title=ft.Text(
                                    value=item_card.get('title'),
                                    size=14,
                                ),
                                subtitle=ft.Column(
                                    controls=[
                                        ft.Text(
                                            value=item_card.get('description')[:len(item_card.get('description'))//3]+'...',
                                        )
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                    height=110,
                                ),
                                height=160,
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        text="Lộ trình",
                                        color=BG_SEC1,
                                    ), 
                                    ft.ElevatedButton(
                                        text="Xem chi tiết",
                                        color=BG_SEC1,
                                        on_click=lambda e, id=item_card.get('id'): self.page.go(f'/course/{id}')
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                spacing=5
                            ),

                        ],
                    ),
                    width=300,
                    height=220,
                    padding=10,
                )
            )
            for item_card in data_all_courses
        ]
        self.ui_content = ft.Column(
            controls=[
                ft.Text(
                    value="Khóa Học Mới Nhất",
                    color=PRIORITY,
                    size=20,
                    text_align=ft.TextAlign.CENTER,
                    width=PHONE_WIDTH,
                ),
                ft.Row(
                    controls=list_card_items,
                    height=260,
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,
                )
            ]
        )
        return self.ui_content
    

    def init_ui_all_lessons_of_courses(self):
        get_id=int(self.page.route.split('/')[-1])
        data_all_lessons = CourseAPI.get_all_lessons_of_course(get_id).get('results')

        list_card_items = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Container(
                                    content=ft.Image(
                                        src=get_tech_imagpath('python-original'),
                                    ),
                                    bgcolor=ft.colors.WHITE,
                                    width=50,
                                    height=50,
                                    padding=ft.padding.all(5),
                                    border_radius=10
                                ),
                                title=ft.Text(
                                    value=item_card.get('name'),
                                ),
                                subtitle=ft.Text(
                                    value=self.label_map_level[item_card.get('extent_name')],
                                ),
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        text="Xem chi tiết",
                                        color=BG_SEC1,
                                        on_click=lambda e, id=item_card.get('id'): self.page.go(f'/lesson/{id}?page=1')
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                spacing=5
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )
            for item_card in data_all_lessons
        ]
        
        self.ui_all_lessons_of_courses = ft.Column(
            controls=[
                ft.ListView(
                    controls=list_card_items,
                    padding=ft.padding.all(10),
                    spacing=10,
                    height=PHONE_HEIGHT - 200,
                ),
            ]
        )

        return self.ui_all_lessons_of_courses
    
    def init_ui_all_detail_lessons_of_lesson(self):
        page_query = int(self.page.query.get('page'))
        get_id = int(self.page.route.split('/')[-1].split('?')[0])
        data_all_detail_lessons = CourseAPI.get_all_detail_lesson(get_id, page_query)
        
        # print(data_all_detail_lessons)
        results = data_all_detail_lessons.get('results')
        count = data_all_detail_lessons.get('count')
        pagination = math.ceil(count/10)

        list_card_items = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Container(
                                    content=ft.Image(
                                        src=get_tech_imagpath('python-original'),
                                    ),
                                    bgcolor=ft.colors.WHITE,
                                    width=50,
                                    height=50,
                                    padding=ft.padding.all(5),
                                    border_radius=10
                                ),
                                title=ft.Text(
                                    value=item_card.get('name'),
                                ),
                                subtitle=ft.Text(
                                    value=item_card.get('extent_name'),
                                ),
                            ),
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        text="Xem chi tiết",
                                        color=BG_SEC1,
                                        on_click=lambda e, id=item_card.get('id'): self.page.go(f'/detail-lesson/{id}')
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                spacing=5
                            ),
                        ]
                    ),
                    width=400,
                    padding=10,
                )
            )
            for item_card in results
        ]

        self.lv_ui_all_detail_lessons_of_lesson = ft.ListView(
            controls=list_card_items,
            padding=ft.padding.all(10),
            spacing=10,
            height=PHONE_HEIGHT - 200
        )
        self.ui_pagination = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=f"{i}",
                    color=BG_SEC1,
                    on_click=lambda e, i=i: self.page.go(f'/lesson/{get_id}?page={i}')
                )
                for i in range(1,pagination+1)
            ],
            alignment='center'
        )

        self.ui_all_detail_lessons_of_lesson = ft.Column(
            controls=[
                self.lv_ui_all_detail_lessons_of_lesson,
                self.ui_pagination
            ]
        )

        return self.ui_all_detail_lessons_of_lesson
    
    def init_ui_detail_one_lesson(self):
        get_id = int(self.page.route.split('/')[-1])
        data_detail_lesson = CourseAPI.get_detail_one_lesson(get_id)

        #* Extract data
        name = data_detail_lesson.get('name')
        content = data_detail_lesson.get('content')
        extent_name = data_detail_lesson.get('extent_name')
        updated_at = data_detail_lesson.get('updated_at')

        # print(name, content, extent_name, updated_at)

        self.ui_all_detail_lessons_of_one_lesson = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Text(
                            value=name,
                            color=BG_SEC1,
                            size=25,
                            font_family='Roboto',
                            italic=True,
                        ),
                        ft.Container(
                            content=ft.Text(
                                value=self.label_map_level[extent_name],
                                color=PRIORITY,
                                size=12,
                            ),
                            bgcolor=BG_SEC1,
                            border_radius=10,
                            padding=ft.padding.all(5)
                        ),
                    ],
                    alignment='spaceBetween',
                    vertical_alignment='center',
                ),
                ft.Text(
                    value=f'Cập nhật lần cuối: {datetime.fromisoformat(updated_at).strftime("%d/%m/%Y %H:%M")}',
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                ft.Column(
                    controls=[
                        ft.Markdown(
                            value=content,
                            selectable=True,
                            extension_set=ft.MarkdownExtensionSet.GITHUB_WEB,
                            on_tap_link=lambda e: self.page.launch_url(e.data),
                        ),
                    ],
                    scroll=ft.ScrollMode.AUTO,
                    height=PHONE_HEIGHT - 300,
                )
            ]
        )

        return self.ui_all_detail_lessons_of_one_lesson
    
    def init_ui_contactpage(self):

        self.ui_contactpage = ft.Column(
            controls=[
                ft.Text(
                    value="Liên Hệ",
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                ft.Text(
                    value="Chúng tôi luôn lắng nghe và hỗ trợ bạn mọi lúc mọi nơi",
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
            ]
        )


        return self.ui_contactpage
    
    def select_ui(self):
        print(self.page.route)
        if self.page.route == '/' or self.page.route == '': #* Path after first slash is empty
            return self.init_ui_intro_content()
        
        elif '/course/' in self.page.route:
            return self.init_ui_all_lessons_of_courses()
        
        elif '/lesson/' in self.page.route:
            return self.init_ui_all_detail_lessons_of_lesson()
        
        elif '/detail-lesson/' in self.page.route:
            return self.init_ui_detail_one_lesson()
        
        elif '/contact' in self.page.route:
            return self.init_ui_contactpage()

    