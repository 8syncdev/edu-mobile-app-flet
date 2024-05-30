
from app import (
    ft,
    BASE_DIR,
    PHONE_HEIGHT,
    PHONE_WIDTH,
    TURN_ON_SCREEN
)

from app.style import *

from typing import (
    Optional,
    Literal
)

from app.util import LocalStore

from app.api import (
    CourseAPI,
    CommonAPI
)

from app.schema import (
    get_brand_imagpath,
    get_tech_imagpath,
    get_with_relativename,
    TStaticTemplate
)

from typing import (
    Literal,
    Dict,
    List
)

import math

from datetime import datetime

from app.constant import (
    MEMBERS
)


class MainPage(ft.Container):
    def __init__(self, 
                 master: Optional[ft.Container] = None, 
                 page: Optional[ft.Page] = None,
                 static_template: TStaticTemplate = None,
                 **kwargs
                ):
        super().__init__(**kwargs)
        self.master = master #* dont use parent, because it is default property of the container
        self.page = page
        self.static_template = static_template
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
                self.select_ui(static_template=self.static_template)
            ],
            height=PHONE_HEIGHT-60,
            scroll=ft.ScrollMode.AUTO,
        )

        # LocalStore.get_data('access', 'token'))


    def shrink(self, e):
        self.master.shrink(e) #* Overriding the shrink method from the parent class, from MainUI class

    def init_ui_navbar(self):
        return self.master.init_ui_navbar() #* Overriding the init_ui_navbar method from the parent class, from MainUI class
    
    def init_ui_intro_content(self):
        data_all_courses = CourseAPI.get_all_courses().get('results')
        # data_all_courses.get('results'))
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

        def handle_send_comment(e):
            try:
                button_send.text = "Đang gửi..."
                button_send.disabled = True
                self.page.update()
                comment = comment_field.value
                # comment)
                #* Send data to backend
                CommonAPI.comment_course({
                    'content': comment,
                    'course': get_id
                })
                #* Reset value
                comment_field.value = ''
                button_send.text = "Gửi"
                button_send.disabled = False
                self.page.update()
                handle_route_comment_page(e, 1)
            except Exception as e:
                button_send.text = "Gửi"
                button_send.disabled = False
                self.page.update()

        #* Build Ui Comment Field
        comment_field = ft.TextField(
            hint_text="Bình luận",
            multiline=True,
            border_color=BG_SEC1,
            width=250,
        )
        button_send = ft.ElevatedButton(
            text="Gửi",
            color=BG_SEC1,
            height=40,
            width=100,
            on_click=handle_send_comment
        )

        

        self.ui_comment = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        comment_field,
                        button_send
                    ],
                    alignment='center',
                    spacing=10
                )
            ],
            spacing=10,
        )

        # Build UI for showing all comments
        data_all_comments = CommonAPI.get_all_comments().get('data')
        total_comments = data_all_comments.get('count')
        pagination = math.ceil(total_comments/10)
        list_comments_ui = [
            ft.Container(
                    content=ft.Row(
                    controls=[
                        ft.Text(
                            value=item_comment.get('content'),
                            color=PRIORITY,
                            size=14,
                            italic=True,
                        ),
                        ft.Text(
                            value=f"{datetime.fromisoformat(item_comment.get('created_at')).strftime('%d/%m/%Y %H:%M')}",
                            color=MUTED,
                            size=12,
                            italic=True,
                        ),
                    ],
                    alignment='spaceBetween',
                ),
                padding=ft.padding.all(10),
                bgcolor=WRAPPER,
                border_radius=10,
                border=ft.border.all(width=1, color=MUTED),
            )
            for item_comment in data_all_comments.get('results')
        ]

        def handle_route_comment_page(e, i):
            data_all_comments = CommonAPI.get_all_comments(i).get('data')
            total_comments = data_all_comments.get('count')
            pagination = math.ceil(total_comments/10)

            pagination_ui = ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text=f"{i}",
                        color=BG_SEC1,
                        on_click=lambda e, i=i: handle_route_comment_page(e, i)
                    )
                    for i in range(1, pagination+1)
                ],
                width=PHONE_WIDTH,
                alignment='center',
            )

            list_comments_ui = [
                ft.Container(
                    content=ft.Row(
                        controls=[
                            ft.Text(
                                value=item_comment.get('content'),
                                color=PRIORITY,
                                size=14,
                                italic=True,
                            ),
                            ft.Text(
                                value=f"{datetime.fromisoformat(item_comment.get('created_at')).strftime('%d/%m/%Y %H:%M')}",
                                color=MUTED,
                                size=12,
                                italic=True,
                            ),
                        ],
                        alignment='spaceBetween',
                    ),
                    padding=ft.padding.all(10),
                    bgcolor=WRAPPER,
                    border_radius=10,
                    border=ft.border.all(width=1, color=MUTED),
                )
                for item_comment in data_all_comments.get('results')
            ]
            self.ui_show_comments.controls = [
                *list_comments_ui,
                pagination_ui,
            ]
            self.page.update()



        pagination_ui = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=f"{i}",
                    color=BG_SEC1,
                    on_click=lambda e, i=i: handle_route_comment_page(e, i)
                )
                for i in range(1, pagination+1)
            ],
            width=PHONE_WIDTH,
            alignment='center',
        )
        self.ui_show_comments = ft.Column(
            controls=[
                *list_comments_ui,
                pagination_ui
            ],
            spacing=10,
        )

        # Build All UI of Lessons for a Course
        self.ui_all_lessons_of_courses = ft.Column(
            controls=[
                ft.ListView(
                    controls=[
                        *list_card_items,
                        self.ui_comment,
                        self.ui_show_comments
                    ],
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
        
        # data_all_detail_lessons)
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

        # name, content, extent_name, updated_at)

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

        def handle_send_contact(e):
            email = email_field.value
            message = message_field.value
            CommonAPI.send_contact({
                'email': email,
                'message': message
            })
            #* Send data to backend
            #* Reset value
            email_field.value = ''
            message_field.value = ''
        
        def validate_email(email):
            if '@' not in email:
                email_field.border_color = ft.colors.RED
            else:
                email_field.border_color = BG_SEC1
            self.page.update()

        
        email_field = ft.TextField(
            hint_text="Email",
            border_color=BG_SEC1,
            # on_change=lambda e: validate_email(e.data)
        )
        message_field = ft.TextField(
            hint_text="Lời nhắn (có thể xuống hàng)",
            multiline=True,
            border_color=BG_SEC1,
        )


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
                ft.Column(
                    controls=[
                        email_field,
                        message_field,
                    ],
                    spacing=10,
                ),
                ft.Row(
                    controls=[
                        ft.ElevatedButton(
                            text="Gửi",
                            color=BG_SEC1,
                            height=40,
                            width=100,
                            on_click=lambda e: handle_send_contact(e)
                        )
                    ],
                    alignment='center',
                    spacing=10
                )
            ],
            spacing=10,
        )


        return self.ui_contactpage
    
    def init_ui_biopage(self):
        list_card_items = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            ft.ListTile(
                                leading=ft.Container(
                                    content=ft.Image(
                                        src=item_card.get('avatar'),
                                        fit=ft.ImageFit.COVER,
                                    ),
                                    bgcolor=ft.colors.WHITE,
                                    padding=ft.padding.all(2),
                                    border_radius=5,
                                    width=60,
                                ),
                                title=ft.Text(
                                    value=item_card.get('name'),
                                ),
                                subtitle=ft.Column(
                                    controls=[
                                        ft.Text(
                                            value=item_card.get('position'),
                                            color=BG_SEC1 if item_card.get('position') == 'Founder & CEO' else PRIORITY,
                                        ),
                                        ft.Text(
                                            value=item_card.get('phone'),
                                        ),
                                        ft.Text(
                                            value=item_card.get('intro'),
                                        ),
                                        ft.Text(
                                            value=item_card.get('tech'),
                                        ),
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                    height=180,
                                ),
                            ),
                        ],
                    ),
                    height=250,
                    padding=10,
                )
            )
            for item_card in MEMBERS
        ]
        

        self.ui_contactpage = ft.Column(
            controls=[
                ft.Text(
                    value="Thông Tin Cá Nhân",
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                ft.Text(
                    value="Các thành viên sáng lập và phát triển ứng dụng này",
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                ft.Column(
                    controls=list_card_items,
                )
            ]
        )


        return self.ui_contactpage
    
    def init_ui_dashboard(self):
        data_sentiment = CommonAPI.get_analysis_sentiment().get('data')
        data_positive = data_sentiment.get('data_positive')
        data_negative = data_sentiment.get('data_negative')
        data_neutral = data_sentiment.get('data_neutral')
        total_comments = sum([data_positive.get('total'), data_negative.get('total'), data_neutral.get('total')])
        normal_border = ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE))
        hovered_border = ft.BorderSide(6, ft.colors.WHITE)

        list_data = [
            {
                **data_positive,
                'color': ft.colors.GREEN,
                'index': 0,
                'badge': ft.icons.SENTIMENT_SATISFIED
            },
            {
                **data_negative,
                'color': ft.colors.RED,
                'index': 1,
                'badge': ft.icons.SENTIMENT_DISSATISFIED
            },
            {
                **data_neutral,
                'color': ft.colors.YELLOW,
                'index': 2,
                'badge': ft.icons.SENTIMENT_NEUTRAL
            }
        ]

        chart_ui = ft.BarChart(
            bar_groups=[
                ft.BarChartGroup(
                    x=data.get('index'),
                    bar_rods=[
                        ft.BarChartRod(
                            from_y=0,
                            to_y=data.get('total'),
                            width=40,
                            color=data.get('color'),
                            tooltip=data.get('total'),
                            border_radius=ft.border_radius.all(10)
                        )
                    ]
                )
                for data in list_data
            ],
            border=ft.border.all(color=BG_SEC1, width=1),
            left_axis=ft.ChartAxis(
                labels_size=40,
                title=ft.Text("Số lượng comments"),
                title_size=20,
            ),
            bottom_axis=ft.ChartAxis(
                labels=[
                    ft.ChartAxisLabel(
                        label=ft.Container(
                            content=ft.Text("Tích cực"),
                        ),
                        value=0,
                    ),
                    ft.ChartAxisLabel(
                        label=ft.Container(
                            content=ft.Text("Tiêu cực"),
                        ),
                        value=1,
                    ),
                    ft.ChartAxisLabel(
                        label=ft.Container(
                            content=ft.Text("Trung lập"),
                        ),
                        value=2,
                    ),
                ],
                labels_size=40,
            ),
            horizontal_grid_lines=ft.ChartGridLines(
                color=BG_SEC1,
                width=1,
                dash_pattern=[5, 5],
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, BG_SEC1),
            max_y=100,
            interactive=True,
            expand=True
        )

        def on_chart_event(e: ft.PieChartEvent):
            for idx, section in enumerate(self.chart.sections):
                section.border_side = (
                    hovered_border if idx == e.section_index else normal_border
                )
            self.page.update()

        def handle_change_chart_type(e):
            if e.data == 'bar':
                self.chart = chart_ui
            else:
                self.chart = ft.PieChart(
                    sections=[
                        ft.PieChartSection(
                            value=data.get('total')/total_comments*100,
                            color=data.get('color'),
                            border_side=normal_border,
                            radius=150,
                            title=f'{
                                "Tích cực" if data.get("index") == 0 else "Tiêu cực" if data.get("index") == 1 else "Trung lập"
                            }: {data.get("total")/total_comments*100:.2f}%',
                            badge=ft.Container(
                                content=ft.Icon(
                                    data.get('badge'),
                                    size=40
                                ),
                                border=ft.border.all(1, ft.colors.BROWN),
                                border_radius=40 / 2,
                                bgcolor=ft.colors.WHITE,
                            ),
                            badge_position=0.99
                        )
                        for data in list_data
                    ],
                    sections_space=1,
                    center_space_radius=0,
                    on_chart_event=on_chart_event,
                    expand=True,
                )
            self.ui_dashboard.controls[3].content = self.chart
            self.page.update()

        self.ui_dashboard = ft.Column(
            controls=[
                ft.Text(
                    value="Dashboard Sử Dụng Sentiment Analysis",
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                ft.Text(
                    value="Trang quản trị của Admin",
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                ft.Row(
                    controls=[ft.Dropdown(
                        width=200,
                        options=[
                            ft.dropdown.Option(
                                key='bar',
                                text='Bar Chart',
                            ),
                            ft.dropdown.Option(
                                key='pie',
                                text='Pie Chart'
                            ),
                        ],
                        border_color=BG_SEC1,
                        value='bar',
                        key='chart_type',
                        on_change=lambda e: handle_change_chart_type(e)
                    )],
                    alignment='center',
                ),
                ft.Container(
                    content=chart_ui,
                    width=PHONE_WIDTH,
                    height=300,
                    padding=ft.padding.all(10),
                )
            ]
        )

        return self.ui_dashboard
    
    def init_ui_faqpage(self):

        self.ui_faqpage = ft.Column(
            controls=[
                ft.Text(
                    value="FAQ",
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                ft.Text(
                    value="Câu hỏi thường gặp",
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                ft.Text(
                    value="1. Làm thế nào để tạo một lớp học mới?",
                    color=BG_SEC1,
                    size=14,
                    italic=True,
                ),
                ft.Text(
                    value="Để tạo một lớp học mới, bạn cần vào phần quản lý lớp học, sau đó chọn 'Tạo lớp học mới' và điền thông tin cần thiết.",
                    color=MUTED,
                    size=12,
                    italic=False,
                ),
                ft.Text(
                    value="2. Làm thế nào để thêm học sinh vào lớp học?",
                    color=BG_SEC1,
                    size=14,
                    italic=True,
                ),
                ft.Text(
                    value="Bạn có thể thêm học sinh vào lớp học bằng cách nhập danh sách học sinh vào phần quản lý lớp học hoặc mời học sinh qua email.",
                    color=MUTED,
                    size=12,
                    italic=False,
                ),
                ft.Text(
                    value="3. Làm thế nào để tải lên tài liệu giảng dạy?",
                    color=BG_SEC1,
                    size=14,
                    italic=True,
                ),
                ft.Text(
                    value="Để tải lên tài liệu giảng dạy, bạn vào phần quản lý tài liệu, chọn 'Tải lên tài liệu' và chọn tệp bạn muốn tải lên từ máy tính của mình.",
                    color=MUTED,
                    size=12,
                    italic=False,
                ),
                ft.Text(
                    value="4. Làm thế nào để liên hệ với hỗ trợ kỹ thuật?",
                    color=BG_SEC1,
                    size=14,
                    italic=True,
                ),
                ft.Text(
                    value="Bạn có thể liên hệ với hỗ trợ kỹ thuật qua email support@example.com hoặc qua số điện thoại hỗ trợ được liệt kê trên trang web của chúng tôi.",
                    color=MUTED,
                    size=12,
                    italic=False,
                ),
            ]
        )

        return self.ui_faqpage
    

    def init_ui_profilepage(self):
        data = LocalStore.get_data('data', 'profile')


        self.ui_profilepage = ft.Column(
            controls=[
                ft.Text(
                    value="Thông Tin Cá Nhân",
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                ft.Text(
                    value="Thông tin cá nhân của bạn",
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                ft.Text(
                    value=f"Tên đăng nhập: {data.get('username')}",
                    color=BG_SEC1,
                    size=14,
                    italic=True,
                ),
                ft.Text(
                    value=f"Email: {data.get('email')}",
                    color=MUTED,
                    size=12,
                    italic=False,
                ),
                ft.Text(
                    value=f"Số điện thoại: {data.get('phone')}",
                    color=BG_SEC1,
                    size=14,
                    italic=True,
                ),
                ft.Text(
                    value=f"Lần đăng nhập cuối: {datetime.fromisoformat(data.get('last_login')).strftime('%d/%m/%Y %H:%M')}",
                    color=MUTED,
                    size=12,
                    italic=False,
                ),
            ]
        )

        return self.ui_profilepage
    
    def select_ui(
            self, 
            static_template: TStaticTemplate = None
        ):
        '''
            Static Route dùng để test nhanh UI, khi không có sự chuyển trang, giúp ta không query lên server của team BE.
            Dynamic Route dùng để chuyển trang, khi có sự chuyển trang, giúp ta query lên server của team BE.
        '''
        #* Static Route
        if static_template == 'intro':
            return self.init_ui_intro_content()
        elif static_template == 'contact':
            return self.init_ui_contactpage()
        elif static_template == 'bio':
            return self.init_ui_biopage()
        elif static_template == 'dashboard':
            return self.init_ui_dashboard()

        #* Dynamic Route
        if self.page.route == '/': 
            #* Path after first slash is empty
            return self.init_ui_intro_content()
        
        elif '/course/' in self.page.route:
            return self.init_ui_all_lessons_of_courses()
        
        elif '/lesson/' in self.page.route:
            return self.init_ui_all_detail_lessons_of_lesson()
        
        elif '/detail-lesson/' in self.page.route:
            return self.init_ui_detail_one_lesson()
        
        elif '/contact' == self.page.route:
            return self.init_ui_contactpage()
        
        elif '/bio' == self.page.route:
            return self.init_ui_biopage()
        
        elif '/dashboard' == self.page.route:
            return self.init_ui_dashboard()
        
        elif '/faq' == self.page.route:
            return self.init_ui_faqpage()
        
        elif '/profile' == self.page.route:
            return self.init_ui_profilepage()

    