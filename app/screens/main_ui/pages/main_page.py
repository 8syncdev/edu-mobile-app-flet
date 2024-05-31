'''
    Author: Nguyễn Phương Anh Tú
    ID: 21110105
    Author: Đinh Thành Đức
    ID: 21110765
    Author: Lê Quốc Thắng
    ID: 21110799
'''
# Importing specific elements from the 'app' module
from app import (
    ft,                # Importing 'ft' (possibly a function or class) from 'app'
    BASE_DIR,          # Importing 'BASE_DIR' constant from 'app'
    PHONE_HEIGHT,      # Importing 'PHONE_HEIGHT' constant from 'app'
    PHONE_WIDTH,       # Importing 'PHONE_WIDTH' constant from 'app'
    TURN_ON_SCREEN     # Importing 'TURN_ON_SCREEN' constant from 'app'
)

# Importing something from the 'style' module within the 'app' package
from app.style import *

# Importing types for type hinting
from typing import (
    Optional,         # Importing 'Optional' type from 'typing'
    Literal           # Importing 'Literal' type from 'typing'
)

# Importing 'LocalStore' from the 'util' module within the 'app' package
from app.util import LocalStore

# Importing APIs from the 'api' module within the 'app' package
from app.api import (
    CourseAPI,        # Importing 'CourseAPI' class from 'api'
    CommonAPI         # Importing 'CommonAPI' class from 'api'
)

# Importing schema-related functions from the 'schema' module within the 'app' package
from app.schema import (
    get_brand_imagpath,      # Importing 'get_brand_imagpath' function
    get_tech_imagpath,       # Importing 'get_tech_imagpath' function
    get_with_relativename,   # Importing 'get_with_relativename' function
    TStaticTemplate          # Importing 'TStaticTemplate' type
)

# Importing types for type hinting
from typing import (
    Literal,         # Importing 'Literal' type again
    Dict,            # Importing 'Dict' type
    List             # Importing 'List' type
)

# Importing the 'math' module
import math

# Importing the 'datetime' class from the 'datetime' module
from datetime import datetime

# Importing constants from the 'constant' module within the 'app' package
from app.constant import (
    MEMBERS          # Importing 'MEMBERS' constant from 'constant'
)


# Define a class named MainPage, inheriting from ft.Container
class MainPage(ft.Container):
    '''
        Author: Nguyễn Phương Anh Tú
        ID: 21110105
    '''

    # Constructor method
    def __init__(
        self,
        master: Optional[ft.Container] = None,     # Parent container (optional)
        page: Optional[ft.Page] = None,            # Page (optional)
        static_template: TStaticTemplate = None,   # Static template (optional)
        **kwargs                                   # Additional keyword arguments
    ):
        super().__init__(**kwargs)  # Call superclass constructor

        # Assign constructor parameters to instance variables
        self.master = master
        self.page = page
        self.static_template = static_template

        # Set various attributes for layout and appearance
        self.height = PHONE_HEIGHT
        self.width = PHONE_WIDTH
        self.bgcolor = BG
        self.border_radius = 30
        self.padding = ft.padding.only(left=10, top=20, right=10)
        self.animate = ft.animation.Animation(600, ft.AnimationCurve.DECELERATE)
        self.animate_scale = ft.animation.Animation(400, ft.AnimationCurve.DECELERATE)

        # Initialize a dictionary to map labels to levels
        self.label_map_level = {
            'foudation': 'Nền tảng',
        }

        # Initialize the content attribute as a column container
        # containing UI elements for the main page
        self.content = ft.Column(
            controls=[
                self.init_ui_navbar(),                     # Initialize navbar UI
                self.select_ui(static_template=self.static_template)  # Initialize selected UI based on static template
            ],
            height=PHONE_HEIGHT-60,  # Set height (minus a margin)
            scroll=ft.ScrollMode.AUTO,  # Enable auto-scrolling
        )




    def shrink(self, e):
        '''
            Author: : Đinh Thành Đức
            ID: 21110765
            Main Purpose:
            => Call the shrink method of the parent class (MainUI class)
        '''
        self.master.shrink(e) #* Overriding the shrink method from the parent class, from MainUI class

    def init_ui_navbar(self):
        '''
            Author: : Đinh Thành Đức
            ID: 21110765
            Main Purpose:
            => Call the init_ui_navbar method of the parent class (MainUI class)
        '''
        return self.master.init_ui_navbar() #* Overriding the init_ui_navbar method from the parent class, from MainUI class
    
    def init_ui_intro_content(self):
        '''
            Author: Nguyễn Phương Anh Tú
            ID: 21110105
            Author: : Đinh Thành Đức
            ID: 21110765
        '''
        # Retrieve all courses data from the CourseAPI
        data_all_courses = CourseAPI.get_all_courses().get('results')

        # Create list of card items representing each course
        list_card_items = [
            # Create a card for each course
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            # Create a ListTile with image, title, and description for the course
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
                                            value=item_card.get('description')[:len(item_card.get('description')) // 3] + '...',
                                        )
                                    ],
                                    scroll=ft.ScrollMode.AUTO,
                                    height=110,
                                ),
                                height=160,
                            ),
                            # Create buttons for course actions (e.g., view details)
                            ft.Row(
                                [
                                    ft.ElevatedButton(
                                        text="Lộ trình",
                                        color=BG_SEC1,
                                    ),
                                    ft.ElevatedButton(
                                        text="Xem chi tiết",
                                        color=BG_SEC1,
                                        on_click=lambda e, id=item_card.get('id'): self.page.go(f'/course/{id}?page=1')
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                spacing=5
                            ),

                        ],
                    ),
                    height=220,
                    padding=10,
                )
            )
            for item_card in data_all_courses  # Iterate over each course data
        ]

        # Construct the UI content using the list of card items
        self.ui_content = ft.Column(
            controls=[
                # Title for the section
                ft.Text(
                    value="Khóa Học Mới Nhất",
                    color=PRIORITY,
                    size=20,
                    text_align=ft.TextAlign.CENTER,
                    width=PHONE_WIDTH,
                ),
                # Column container containing the list of card items
                ft.Column(
                    controls=list_card_items,
                    height=PHONE_HEIGHT - 200,  # Adjusted height
                    spacing=10,
                    scroll=ft.ScrollMode.AUTO,  # Enable auto-scrolling
                )
            ]
        )
        return self.ui_content # Return the UI content

    

    def init_ui_all_lessons_of_courses(self):
        '''
            Author: Nguyên Phương Anh Tú
            ID: 21110105
            Author: Lê Quốc Thắng
            ID: 21110799
            Main Purpose:
            => Initialize the UI for displaying all lessons of a course.
        '''
        # Extract the page query and course ID from the page route
        page_query = int(self.page.query.get('page'))
        # Extract the ID of the course from the page route
        get_id = int(self.page.route.split('/')[-1].split('?')[0])
        
        # Retrieve data of all lessons for the given course ID from the CourseAPI
        data_fetch = CourseAPI.get_all_lessons_of_course(get_id, page_query)
        data_all_lessons = data_fetch.get('results')
        total_lessons = data_fetch.get('count')
        pagination = math.ceil(total_lessons / 10)

        # Create UI Pagination
        pagination_ui_course = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=f"{i}",
                    color=BG_SEC1,
                    on_click=lambda e, i=i: self.page.go(f'/course/{get_id}?page={i}')
                )
                for i in range(1, pagination + 1)
            ],
            alignment='center',
        )

        # Create list of card items representing each lesson
        list_card_items = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            # ListTile representing lesson details
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
                            # Button to view lesson details
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

        # Define event handler function to send comment
        def handle_send_comment(e):
            '''
                Author: : Lê Quốc Thắng
                ID: 21110799
            '''
            try:
                # Disable the send button and update UI
                button_send.text = "Đang gửi..."
                button_send.disabled = True
                self.page.update()

                # Get comment from the text field
                comment = comment_field.value
                
                # Send comment data to the backend
                CommonAPI.comment_course({
                    'content': comment,
                    'course': get_id
                })

                # Reset text field and enable send button
                comment_field.value = ''
                button_send.text = "Gửi"
                button_send.disabled = False
                self.page.update()

                # Refresh comments section
                handle_route_comment_page(e, 1)
            except Exception as e:
                button_send.text = "Gửi"
                button_send.disabled = False
                self.page.update()

        # Build UI elements for comment field and send button
        comment_field = ft.TextField(
            hint_text="Bình luận (có thể xuống hàng)",
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

        # Construct UI for comment section
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

        # Build UI for displaying all comments
        # Retrieve comments data from the backend
        data_all_comments = CommonAPI.get_all_comments().get('data')
        total_comments = data_all_comments.get('count')
        pagination = math.ceil(total_comments / 10)

        # Construct UI for each comment
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

        # Define event handler function for pagination
        def handle_route_comment_page(e, i):
            '''
                Author: : Đinh Thành Đức
                ID: 21110765
                Author: : Lê Quốc Thắng
                ID: 21110799
            '''
            # Retrieve comments data for the given page number
            data_all_comments = CommonAPI.get_all_comments(i).get('data')
            total_comments = data_all_comments.get('count')
            pagination = math.ceil(total_comments / 10)

            # Construct pagination UI
            pagination_ui = ft.Row(
                controls=[
                    ft.ElevatedButton(
                        text=f"{i}",
                        color=BG_SEC1,
                        on_click=lambda e, i=i: handle_route_comment_page(e, i)
                    )
                    for i in range(1, pagination + 1)
                ],
                width=PHONE_WIDTH,
                alignment='center',
            )

            # Construct UI for comments section
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

            # Update UI for comments section
            self.ui_show_comments.controls = [
                *list_comments_ui,
                pagination_ui,
            ]
            self.page.update()

        # Construct pagination UI
        pagination_ui = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=f"{i}",
                    color=BG_SEC1,
                    on_click=lambda e, i=i: handle_route_comment_page(e, i)
                )
                for i in range(1, pagination + 1)
            ],
            width=PHONE_WIDTH,
            alignment='center',
        )

        # Construct UI for displaying all comments
        self.ui_show_comments = ft.Column(
            controls=[
                *list_comments_ui,
                pagination_ui
            ],
            spacing=10,
        )

        # Build UI for all lessons of the course
        self.ui_all_lessons_of_courses = ft.Column(
            controls=[
                ft.ListView(
                    controls=[
                        *list_card_items,
                        pagination_ui_course,
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
        '''
            Author: Nguyễn Phương Anh Tú
            ID: 21110105
        '''
        # Extract the page query and lesson ID from the page route
        page_query = int(self.page.query.get('page'))
        get_id = int(self.page.route.split('/')[-1].split('?')[0])
        
        # Retrieve data of all detail lessons for the given lesson ID and page from the CourseAPI
        data_all_detail_lessons = CourseAPI.get_all_detail_lesson(get_id, page_query)
        
        # Extract results and count from the data
        results = data_all_detail_lessons.get('results')
        count = data_all_detail_lessons.get('count')
        pagination = math.ceil(count / 10)

        # Create list of card items representing each detail lesson
        list_card_items = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            # ListTile representing detail lesson details
                            ft.ListTile(
                                leading=ft.Container(
                                    content=ft.Image(
                                        src=get_tech_imagpath('python-original'), # get_tech_imagpath: get image path to display
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
                            # Button to view detail lesson details
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

        # Construct ListView for displaying all detail lessons
        self.lv_ui_all_detail_lessons_of_lesson = ft.ListView(
            controls=list_card_items,
            padding=ft.padding.all(10),
            spacing=10,
            height=PHONE_HEIGHT - 200
        )

        # Construct pagination UI
        self.ui_pagination = ft.Row(
            controls=[
                ft.ElevatedButton(
                    text=f"{i}",
                    color=BG_SEC1,
                    on_click=lambda e, i=i: self.page.go(f'/lesson/{get_id}?page={i}')
                )
                for i in range(1, pagination + 1)
            ],
            alignment='center'
        )

        # Construct UI for all detail lessons of the lesson
        self.ui_all_detail_lessons_of_lesson = ft.Column(
            controls=[
                self.lv_ui_all_detail_lessons_of_lesson,
                self.ui_pagination
            ]
        )

        return self.ui_all_detail_lessons_of_lesson

    
    def init_ui_detail_one_lesson(self):
        '''
            Author: : Lê Quốc Thắng
            ID: 21110799
        '''
        # Extract the lesson ID from the page route
        get_id = int(self.page.route.split('/')[-1])
        
        # Retrieve data of the detail lesson from the CourseAPI
        data_detail_lesson = CourseAPI.get_detail_one_lesson(get_id)

        # Extract relevant data from the response
        name = data_detail_lesson.get('name')
        content = data_detail_lesson.get('content')
        extent_name = data_detail_lesson.get('extent_name')
        updated_at = data_detail_lesson.get('updated_at')

        # Construct UI for displaying detail lesson information
        self.ui_all_detail_lessons_of_one_lesson = ft.Column(
            controls=[
                # Row for lesson name and extent name
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
                    wrap=True,
                ),
                # Text showing last update time
                ft.Text(
                    value=f'Cập nhật lần cuối: {datetime.fromisoformat(updated_at).strftime("%d/%m/%Y %H:%M")}',
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                # Column for lesson content
                ft.Column(
                    controls=[
                        # Markdown component for rendering lesson content
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
        '''
            Author: : Đinh Thành Đức
            ID: 21110765
            Author: : Lê Quốc Thắng
            ID: 21110799
            Main Purpose:
            - It defines an event handler function handle_send_contact to send the contact message to the backend via CommonAPI.
            - It defines a function validate_email to validate the email format (not currently used).
            - It creates text fields for entering the email and message.
            - It constructs a UI layout using FlexTools components for the contact page, including header text, subtitle text, text fields, and a button to send the contact message.
            - The method returns the constructed UI component for further usage or display on the contact page.
        '''
        # Define event handler function to send contact message
        def handle_send_contact(e):
            # Retrieve email and message from the text fields
            email = email_field.value
            message = message_field.value
            
            # Send contact data to the backend using CommonAPI
            CommonAPI.send_contact({
                'email': email,
                'message': message
            })
            
            # Reset text fields after sending the message
            email_field.value = ''
            message_field.value = ''
        
        # Define function to validate email format
        def validate_email(email):
            if '@' not in email:
                email_field.border_color = ft.colors.RED
            else:
                email_field.border_color = BG_SEC1
            self.page.update()
        
        # Create text fields for email and message input
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
        
        # Construct UI layout for the contact page
        self.ui_contactpage = ft.Column(
            controls=[
                # Header text
                ft.Text(
                    value="Liên Hệ",
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                # Subtitle text
                ft.Text(
                    value="Chúng tôi luôn lắng nghe và hỗ trợ bạn mọi lúc mọi nơi",
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                # Text fields for email and message
                ft.Column(
                    controls=[
                        email_field,
                        message_field,
                    ],
                    spacing=10,
                ),
                # Button to send the contact message
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
        '''
            Author: : Đinh Thành Đức
            ID: 21110765
            Author: : Lê Quốc Thắng
            ID: 21110799
        '''
        # Generate list of card items representing each member's biography
        list_card_items = [
            ft.Card(
                content=ft.Container(
                    content=ft.Column(
                        [
                            # ListTile representing member's details
                            ft.ListTile(
                                leading=ft.Container(
                                    content=ft.Image(
                                        src=item_card.get('avatar'),  # Member's avatar image
                                        fit=ft.ImageFit.COVER,
                                    ),
                                    bgcolor=ft.colors.WHITE,
                                    padding=ft.padding.all(2),
                                    border_radius=5,
                                    width=60,
                                ),
                                title=ft.Text(
                                    value=item_card.get('name'),  # Member's name
                                ),
                                subtitle=ft.Column(
                                    controls=[
                                        ft.Text(
                                            value=item_card.get('position'),  # Member's position
                                            color=BG_SEC1 if item_card.get('position') == 'Founder & CEO' else PRIORITY,
                                        ),
                                        ft.Text(
                                            value=item_card.get('phone'),  # Member's phone number
                                        ),
                                        ft.Text(
                                            value=item_card.get('intro'),  # Member's introduction
                                        ),
                                        ft.Text(
                                            value=item_card.get('tech'),  # Member's technical expertise
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
            for item_card in MEMBERS  # Iterate through MEMBERS list to create a card item for each member
        ]
        
        # Construct UI layout for the biography page
        self.ui_contactpage = ft.Column(
            controls=[
                # Header text
                ft.Text(
                    value="Thông Tin Cá Nhân",  # Personal Information
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                # Subtitle text
                ft.Text(
                    value="Các thành viên sáng lập và phát triển ứng dụng này",  # Members who founded and developed this application
                    color=MUTED,
                    size=12,
                    italic=True,
                ),
                # Column of card items representing members' biographies
                ft.Column(
                    controls=list_card_items,
                )
            ]
        )

        # Return the constructed UI component for the biography page
        return self.ui_contactpage

    
    def init_ui_dashboard(self):
        '''
            Author: Nguyễn Phương Anh Tú
            ID: 21110105
            Main Purpose:
            - It retrieves sentiment analysis data from the backend using CommonAPI.
            - It extracts data for positive, negative, and neutral comments.
            - It constructs a bar chart or pie chart based on the selected chart type.
            - It defines event handlers for chart type change and chart section hover events.
            - It constructs the UI layout for the sentiment analysis dashboard.
            - The method returns the constructed UI component for the sentiment analysis dashboard.
        '''

        # Get data from the backend
        data_sentiment = CommonAPI.get_analysis_sentiment().get('data')

        # Extract data from the response
        data_positive = data_sentiment.get('data_positive')
        data_negative = data_sentiment.get('data_negative')
        data_neutral = data_sentiment.get('data_neutral')
        total_comments = sum([data_positive.get('total'), data_negative.get('total'), data_neutral.get('total')])

        # Define border styles for chart sections
        normal_border = ft.BorderSide(0, ft.colors.with_opacity(0, ft.colors.WHITE))
        hovered_border = ft.BorderSide(6, ft.colors.WHITE)

        # Define data for chart sections
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

        # Construct the bar chart UI
        chart_ui = ft.BarChart( # Create a bar chart
            bar_groups=[
                ft.BarChartGroup( # Create a bar chart group
                    x=data.get('index'),
                    bar_rods=[
                        ft.BarChartRod( # Create a bar chart rod, representing a bar in the chart
                            from_y=0, # Starting point of the bar
                            to_y=data.get('total'), # Ending point of the bar
                            width=40, # Width of the bar
                            color=data.get('color'), # Color of the bar
                            tooltip=data.get('total'), # Tooltip text for the bar
                            border_radius=ft.border_radius.all(10) # Border radius of the bar
                        )
                    ]
                )
                for data in list_data # Iterate over each data item to create a bar chart group
            ],
            border=ft.border.all(color=BG_SEC1, width=1), # Border style of the chart
            left_axis=ft.ChartAxis( # Define the left axis of the chart
                labels_size=40,
                title=ft.Text("Số lượng comments"),
                title_size=20,
            ),
            bottom_axis=ft.ChartAxis( # Define the bottom axis of the chart
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
            horizontal_grid_lines=ft.ChartGridLines( # Define horizontal grid lines
                color=BG_SEC1,
                width=1,
                dash_pattern=[5, 5], 
            ),
            tooltip_bgcolor=ft.colors.with_opacity(0.5, BG_SEC1), # Background color of the tooltip
            max_y=100, # Maximum value for the y-axis
            interactive=True, # Enable interactivity
            expand=True # Expand the chart to fill the available space
        )

        def on_chart_event(e: ft.PieChartEvent):
            '''
                Author: Nguyễn Phương Anh Tú
                ID: 21110105
                Main Purpose:
                - It defines an event handler for chart section hover events.
                - It updates the border style of the chart sections based on the hover event.
            '''
            for idx, section in enumerate(self.chart.sections):
                section.border_side = (
                    hovered_border if idx == e.section_index else normal_border
                )
            self.page.update()

        def handle_change_chart_type(e):
            '''
                Author: Nguyễn Phương Anh Tú
                ID: 21110105
                Main Purpose:
                - It defines an event handler for changing the chart type.
                - It updates the chart type based on the selected value.
            '''
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
            self.ui_dashboard.controls[3].content = self.chart # Update the chart in the UI
            self.page.update() # Update the page

        # Initialize the UI layout for the dashboard page
        self.ui_dashboard = ft.Column(
            controls=[
                ft.Text(
                    value="Dashboard Sử Dụng Sentiment Analysis AI",
                    color=BG_SEC1,
                    size=25,
                    font_family='Roboto',
                    italic=True,
                ),
                ft.Text(
                    value="Trang quản trị của Admin, dùng để xem tổng quan về cảm xúc của người dùng thông qua comments",
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
        '''
            Author: : Đinh Thành Đức
            ID: 21110765
            Main Purpose:
            - It creates a Column layout using the Fluent UI components. This layout consists of a series of Text components containing the FAQ content.
            - Each FAQ question is followed by an answer. Both the question and the answer are represented by Text components.
            - The questions are styled with a larger font size and a different color to make them stand out (using BG_SEC1 color).
            - The answers are styled with a smaller font size and a muted color (using MUTED color).
            - The questions and answers are hardcoded into the UI code. There are four sets of questions and answers provided.
            - The constructed UI layout is stored in the ui_faqpage variable.
        '''

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
        '''
            Author: : Nguyễn Phương Anh Tú
            ID: 21110105
            Main Purpose:
            - It retrieves user profile data from the local store using the LocalStore.get_data method. The data contains information such as username, email, phone number, and last login time.
            - It constructs a Column layout using the Fluent UI components to display the user's profile information.
            - Each piece of profile information (username, email, phone number, last login time) is represented by a Text component.
            - The username and phone number are styled with a larger font size and a different color to make them stand out (using BG_SEC1 color).
            - The email and last login time are styled with a smaller font size and a muted color (using MUTED color).
            - The constructed UI layout is stored in the ui_profilepage variable.
        '''
        # Retrieve user profile data from the local store
        data = LocalStore.get_data('data', 'profile')

        # Construct the UI layout for the profile page
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
                    value=f"Lần đăng nhập cuối: {datetime.fromisoformat(data.get('last_login')).strftime('%d/%m/%Y %H:%M') if data.get('last_login') else datetime.now().strftime('%d/%m/%Y %H:%M')}",
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
            Author: Nguyễn Phương Anh Tú
            ID: 21110105
            Author: : Đinh Thành Đức
            ID: 21110765
            Author: : Lê Quốc Thắng
            ID: 21110799
        '''
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

    