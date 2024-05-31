'''
    Author: Nguyễn Phương Anh Tú
    ID: 21110105
'''
'''
    Author: Nguyễn Phương Anh Tú
    ID: 21110105
- flet as ft: Import the Flet library, used for building GUI applications.
- from app.screens import (AuthUI, MainUI): Import AuthUI and MainUI classes from the app.screens module. These are likely custom UI components for authentication and main screens.
- from app import (PHONE_HEIGHT, PHONE_WIDTH, BASE_DIR, TURN_ON_SCREEN): - Import constants from the app module. These constants likely define the dimensions of a phone and a base directory path.
- from app.style import *: Import all definitions from the app.style module, which presumably contains style-related configurations.
- from app.api import (AuthAPI): Import the AuthAPI class or module from app.api, likely used for authentication-related API calls.
'''
import flet as ft
from app.screens import (
    AuthUI,
    MainUI
)
from app import (
    PHONE_HEIGHT,
    PHONE_WIDTH,
    BASE_DIR,
    TURN_ON_SCREEN
)
from app.style import *

from app.api import (
    AuthAPI
)


def main(page: ft.Page):
    '''
        Author: Nguyễn Phương Anh Tú
        ID: 21110105
        - main(page: ft.Page): The main function which initializes the app.
        - page.window_top and page.window_left: Set the position of the app window.
        - page.window_width and page.window_height: Set the size of the window based on the constants PHONE_WIDTH and PHONE_HEIGHT. These dimensions adjust if TURN_ON_SCREEN is True.
    '''
    page.window_top = 50
    page.window_left = 1400
    page.window_width = PHONE_WIDTH + 100 if TURN_ON_SCREEN else PHONE_WIDTH + 45
    page.window_height = PHONE_HEIGHT + 100 if TURN_ON_SCREEN else PHONE_HEIGHT + 60

    '''
        view_style: A dictionary that defines the alignment of the views, setting both horizontal and vertical alignment to center.
    '''
    view_style = {
        'horizontal_alignment':ft.CrossAxisAlignment.CENTER, #* Center the views horizontally
        'vertical_alignment':ft.MainAxisAlignment.CENTER, #* Center the views vertically
    }
    
    

    '''
        - app_router: A list of routes for the main application.
        - auth_router: A list of routes related to authentication
    '''
    app_router = [
        '/',
        '/contact',
        '/bio',
        '/dashboard',
        '/faq',
        '/profile'
    ]

    auth_router = [
        '/sign-in',
        '/sign-up',
        '/forgot-password',
    ]
    
    # Route change function
    def route_change(event: ft.RouteChangeEvent):
        '''
            Author: Nguyễn Phương Anh Tú
            ID: 21110105
            - route_change(event: ft.RouteChangeEvent): A function that is called each time the route changes.
            - page.views.clear(): Clear the views on the page.
            - page.overlay.clear(): Clear the overlay on the page.
            - troute: Create a TemplateRoute object from the current route. This object is used to match dynamic routes.
            - if page.route in auth_router: Check if the current route is in the auth_router list. If so, add an AuthUI view to the page.
            - elif page.route in app_router: Check if the current route is in the app_router list. If so, add a MainUI view to the page.
            - elif troute.match('/course/:course_id'): Check if the route matches a course ID. If so, add a MainUI view to the page.
            - elif troute.match('/lesson/:lesson_id'): Check if the route matches a lesson ID. If so, add a MainUI view to the page.
            - elif troute.match('/detail-lesson/:detail_lesson_id'): Check if the route matches a detail lesson ID. If so, add a MainUI view to the page.
            - page.update(): Update the page with the new views.
        '''
        page.views.clear() #* Optimized for clear views
        if len(page.overlay) > 0:
            page.overlay.clear()
        troute = ft.TemplateRoute(page.route)
        if page.route in auth_router:
            page.views.append(ft.View(
                page.route,
                [
                    AuthUI(page=page)
                ],
                **view_style
            ))
        elif page.route in app_router:
            page.views.append(ft.View(
                page.route,
                [
                    MainUI(page=page)
                ],
                **view_style
            ))
        #* Extent Dynamic Route
        elif troute.match('/course/:course_id'):
            page.views.append(ft.View(
                f"/course/{troute.course_id}",
                [
                    MainUI(page=page)
                ],
                **view_style
            ))
        elif troute.match('/lesson/:lesson_id'):
            page.views.append(ft.View(
                f"/lesson/{troute.lesson_id}",
                [
                    MainUI(page=page)
                ],
                **view_style
            ))
        elif troute.match('/detail-lesson/:detail_lesson_id'):
            page.views.append(ft.View(
                f"/detail-lesson/{troute.detail_lesson_id}",
                [
                    MainUI(page=page)
                ],
                **view_style
            ))
        page.update()

    '''
        Author: Nguyễn Phương Anh Tú
        ID: 21110105
        - page.on_route_change: Set the on_route_change event handler each time the route changes.
        - if page.route == "/": Check if the current route is the root route.
        - AuthAPI.check_auth(): Check if the user is authenticated.
    '''
    #* Set the on_route_change event handler each time the route changes
    page.on_route_change = route_change

    #* Check Auth before go to MainUI
    if page.route == "/" and AuthAPI.check_auth() == False:
        page.go("/sign-in")
    else:
        page.go(page.route) #* Go to the current route, if the user is authenticated

if __name__ == "__main__":
    ft.app(target=main)
