import flet as ft
from app.screens import (
    AuthUI,
    MainUI
)
from app import (
    PHONE_HEIGHT,
    PHONE_WIDTH,
    BASE_DIR
)
from app.style import *

from app.api import (
    AuthAPI
)

class StateMainApp(object):
    count:int = 0



def main(page: ft.Page):
    page.window_top = 50
    page.window_left = 1400
    page.window_width = PHONE_WIDTH + 100
    page.window_height = PHONE_HEIGHT + 100
    
    # page.navigation_bar = init_ui_navbarbottom()
    view_style = {
        'horizontal_alignment':ft.CrossAxisAlignment.CENTER,
        'vertical_alignment':ft.MainAxisAlignment.CENTER,
    }
    
    

    #* My custom for app_router
    app_router = {
        '/': ft.View(
            "/",
            [
                MainUI(page=page)
            ],
            **view_style
        ),
        '/sign_in': ft.View(
            "/sign_in",
            [
                AuthUI(page=page)
            ],
            **view_style
        ),
        '/contact': ft.View(
            "/contact",
            [
                MainUI(page=page)
            ],
            **view_style
        ),
    }
    
    # Route change function
    def route_change(event: ft.RouteChangeEvent):
        page.views.clear() #* Optimized for clear views
        if len(page.overlay) > 0: 
            page.overlay.clear()
        troute = ft.TemplateRoute(page.route)
        if page.route in list(app_router.keys()):
            page.views.append(app_router[page.route])
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

    #* Set the on_route_change event handler each time the route changes
    page.on_route_change = route_change

    #* Check Auth before go to MainUI
    if page.route == "/" and AuthAPI.check_auth() == False:
        page.go("/sign_in")
    else:
        page.go(page.route)

# if __name__ == "__main__":
ft.app(target=main)
