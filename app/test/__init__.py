'''
    Author: Nguyễn Phương Anh Tú
    
    Main Purpose: Test all API functions in the app
'''
from app.api import (
    AuthAPI,   # Importing authentication-related API functions
    CommonAPI, # Importing common/general API functions
    CourseAPI, # Importing course-related API functions
)

import unittest  # Importing the unittest module for creating test cases

'''
ANSI Color Codes:
    31: Red
    32: Green
    33: Yellow
    34: Blue
    35: Magenta
    36: Cyan
'''

# Function to print text in a specified color using ANSI color codes
def print_color(text, color_code):
    print(f"\033[{color_code}m{text}\033[0m")

# Test cases for authentication-related API functions
class TestAuthenticationAPI(unittest.TestCase):
    '''
        Author: Nguyễn Phương Anh Tú
        
        Main Purpose: Test all API functions in the app
    '''
    # Class variables to control whether certain tests are active
    active_sign_up = True
    active_forgot_password = True

    def test_get_token(self):
        # Testing the get_token function of AuthAPI
        res_data = AuthAPI.get_token({
            'username': 'adminanhtudev',
            'password': 'anhtudev2003'
        })

        # Check if the access token is returned and is non-empty
        if res_data.get('access').__len__() > 0:
            print_color('Test get_token passed', 32)
        else:
            print_color('Test get_token failed', 31)
        self.assertTrue(res_data.get('access').__len__() > 0)

    def test_get_user_by_token(self):
        # Testing the get_user_by_token function of AuthAPI
        res_data = AuthAPI.get_token({
            'username': 'adminanhtudev',
            'password': 'anhtudev2003'
        })
        res_data = AuthAPI.get_user_by_token(res_data.get('access')).get('data')
        
        # Check if the username matches the expected value
        if res_data.get('username') == 'adminanhtudev':
            print_color('Test get_user_by_token passed', 32)
        else:
            print_color('Test get_user_by_token failed', 31)
        self.assertTrue(res_data.get('username') == 'adminanhtudev')

    def test_check_auth(self):
        # Testing the check_auth function of AuthAPI
        res_data = AuthAPI.check_auth()

        # Check if authentication is successful
        if res_data:
            print_color('Test check_auth passed', 32)
        else:
            print_color('Test check_auth failed', 31)
        self.assertTrue(res_data)

    def test_sign_up(self):
        # Testing the sign_up function of AuthAPI
        payload = {
            "username": "testuser101",
            "password": "adminanhtudev20032712",
            "email": "testuser101@gmail.com",
            "full_name": "Manager 1",
            "phone": "111111111"
        }
        if TestAuthenticationAPI.active_sign_up:
            res_data = AuthAPI.sign_up(payload)

            # Check if the sign-up was successful
            if res_data.get('code') == 'res_success':
                print_color('Test sign_up passed', 32)
            else:
                print_color('Test sign_up failed', 31)
            self.assertTrue(res_data.get('code') == 'res_success')
        else:
            print_color('Test sign_up skipped', 33)

    def test_forgot_password(self):
        # Testing the forgot_password function of AuthAPI
        payload = {
            "email": "tuan8165@gmail.com"
        }
        
        if TestAuthenticationAPI.active_forgot_password:
            res_data = AuthAPI.forgot_password(payload)

            # Check if the forgot password request was successful
            if res_data.get('code') == 'res_success':
                print_color('Test forgot_password passed', 32)
            else:
                print_color('Test forgot_password failed', 31)
            self.assertTrue(res_data.get('code') == 'res_success')
        else:
            print_color('Test forgot_password skipped', 33)

    def test_sign_in(self):
        # Testing the sign_in function of AuthAPI
        payload = {
            "username": "adminanhtudev",
            "password": "anhtudev2003"
        }
        res_data = AuthAPI.sign_in(payload)

        # Check if the sign-in was successful
        if res_data.get('code') == 'res_success':
            print_color('Test sign_in passed', 32)
        else:
            print_color('Test sign_in failed', 31)
        self.assertTrue(res_data.get('code') == 'res_success')

    def test_refresh_token(self):
        # Testing the refresh_token function of AuthAPI
        res_data = AuthAPI.get_token({
            'username': 'adminanhtudev',
            'password': 'anhtudev2003'
        })
        res_data = AuthAPI.refresh_token(res_data.get('refresh'))

        # Check if the refreshed token is returned and is non-empty
        if res_data.get('access').__len__() > 0:
            print_color('Test refresh_token passed', 32)
        else:
            print_color('Test refresh_token failed', 31)
        self.assertTrue(res_data.get('access').__len__() > 0)

    def test_auth_by_email(self):
        # Testing the auth_by_email function of AuthAPI
        res_data = AuthAPI.auth_by_email('techdev.td1111@gmail.com')

        # Check if the authentication by email was successful
        if res_data.get('code') == 'res_success':
            print_color('Test auth_by_email passed', 32)
        else:
            print_color('Test auth_by_email failed', 31)
        self.assertTrue(res_data.get('code') == 'res_success')

    def test_check_token_of_email(self):
        # Testing the check_token_of_email function of AuthAPI
        token = AuthAPI.get_token({
            'username': 'adminanhtudev',
            'password': 'anhtudev2003'
        }).get('access')
        res_data = AuthAPI.check_token_of_email(token)

        # Check if the token check for email was successful
        if res_data.get('code') == 'res_success':
            print_color('Test check_token_of_email passed', 32)
        else:
            print_color('Test check_token_of_email failed', 31)
        self.assertTrue(res_data.get('code') == 'res_success')

# Test cases for common/general API functions
class TestCommonAPI(unittest.TestCase):
    '''
        Author: Nguyễn Phương Anh Tú
        
        Main Purpose: Test all API functions in the app
    '''
    def test_sentiment_model(self):
        # Testing the sentiment_model function of CommonAPI
        res_data = CommonAPI.sentiment_model('Khóa học rất hay và bổ ích')

        # Check if the sentiment analysis was successful
        if res_data.get('detail') == 'success':
            print_color('Test sentiment_model passed', 32)
        else:
            print_color('Test sentiment_model failed', 31)
        self.assertTrue(res_data.get('detail') == 'success')
    
    def test_send_contact(self):
        # Testing the send_contact function of CommonAPI
        data = {
            "message": "Chào bạn Admin Anh Tú",
            "email": "tuan8165@gmail.com"
        }
        res_data = CommonAPI.send_contact(data)

        # Check if the contact message was sent successfully
        if res_data.get('code') == 'res_success':
            print_color('Test send_contact passed', 32)
        else:
            print_color('Test send_contact failed', 31)
        self.assertTrue(res_data.get('code') == 'res_success')

    def test_comment_course(self):
        # Testing the comment_course function of CommonAPI
        data = {
            "course": 1,
            "content": "Khóa học rất hay và bổ ích",
        }
        res_data = CommonAPI.comment_course(data)

        # Check if the course comment was posted successfully
        if res_data.get('code') == 'res_success':
            print_color('Test comment_course passed', 32)
        else:
            print_color('Test comment_course failed', 31)
        self.assertTrue(res_data.get('code') == 'res_success')

    def test_get_all_comments(self):
        # Testing the get_all_comments function of CommonAPI
        res_data = CommonAPI.get_all_comments(page=1)

        # Check if retrieving all comments was successful
        if res_data.get('code') == 'res_success':
            print_color('Test get_all_comments passed', 32)
        else:
            print_color('Test get_all_comments failed', 31)
        self.assertTrue(res_data.get('code') == 'res_success')

    def test_get_analysis_sentiment(self):
        # Testing the get_analysis_sentiment function of CommonAPI
        res_data = CommonAPI.get_analysis_sentiment()

        # Check if sentiment analysis was retrieved successfully
        if res_data.get('code') == 'res_success':
            print_color('Test get_analysis_sentiment passed', 32)
        else:
            print_color('Test get_analysis_sentiment failed', 31)
        self.assertTrue(res_data.get('code') == 'res_success')

    def test_check_admin_role(self):
        # Testing the check_admin_role function of CommonAPI
        res_data = CommonAPI.check_admin_role()

        # Check if the admin role is valid
        if res_data:
            print_color('Test check_admin_role passed', 32)
        else:
            print_color('Test check_admin_role failed', 31)
        self.assertTrue(res_data)

# Test cases for course-related API functions
class TestCourseAPI(unittest.TestCase):
    '''
        Author: Nguyễn Phương Anh Tú
        
        Main Purpose: Test all API functions in the app
    '''
    def test_get_all_courses(self):
        # Testing the get_all_courses function of CourseAPI
        res_data = CourseAPI.get_all_courses()

        # Check if retrieving all courses was successful
        if res_data.get('count') >= 0:
            print_color('Test get_all_courses passed', 32)
        else:
            print_color('Test get_all_courses failed', 31)
        self.assertTrue(res_data.get('count') >= 0)

    def test_get_all_lessons_of_course(self):
        # Testing the get_all_lessons_of_course function of CourseAPI
        res_data = CourseAPI.get_all_lessons_of_course(3)

        # Check if retrieving all lessons of a course was successful
        if res_data.get('count') >= 0:
            print_color('Test get_course_by_id passed', 32)
        else:
            print_color('Test get_course_by_id failed', 31)
        self.assertTrue(res_data.get('count') >= 0)

    def test_get_all_detail_lesson(self):
        # Testing the get_all_detail_lesson function of CourseAPI
        res_data = CourseAPI.get_all_detail_lesson(1)

        # Check if retrieving all detailed lessons was successful
        if res_data.get('count') >= 0:
            print_color('Test get_all_detail_lesson passed', 32)
        else:
            print_color('Test get_all_detail_lesson failed', 31)
        self.assertTrue(res_data.get('count') >= 0)

    def test_get_detail_one_lesson(self):
        # Testing the get_detail_one_lesson function of CourseAPI
        res_data = CourseAPI.get_detail_one_lesson(1)

        # Check if retrieving details of one lesson was successful
        if res_data.get('id') >= 0:
            print_color('Test get_detail_one_lesson passed', 32)
        else:
            print_color('Test get_detail_one_lesson failed', 31)
        self.assertTrue(res_data.get('id') >= 0)

    def test_get_all_exercise_by_slug(self):
        # Testing the get_all_exercise_by_slug function of CourseAPI
        res_data = CourseAPI.get_all_exercise_by_slug('python-fresher-buoi-1')

        # Check if retrieving all exercises by slug was successful
        if res_data.get('count') >= 0:
            print_color('Test get_all_exercise_by_slug passed', 32)
        else:
            print_color('Test get_all_exercise_by_slug failed', 31)
        self.assertTrue(res_data.get('count') >= 0)
