# This Source Code Form is subjectfrom django import forms to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home import HomePage

from selenium.webdriver.common.by import By


class TestAvailableTasks():
    @pytest.mark.nondestructive
    def test_create_tasks(self, base_url, selenium, task, random_title):

        admin_user = {  'email': "varna.suresh@outlook.com",
                        'password': "varna123",
                        'name': "Varna",
                        'username': "Varna",
                        'url': 'http://www.mozilla.org/'
        }

        home_page = HomePage(selenium, base_url).open()
        assert not home_page.is_user_logged_in

        edit_profile = home_page.login(admin_user)
        assert edit_profile.is_user_logged_in
         
        available_tasks_page = home_page.click_available_tasks()
        home_page.click_create_task(random_title)

    
    @pytest.mark.nondestructive
    def test_assign_tasks(self, base_url, selenium, task, new_user, random_title):
        home_page= HomePage(selenium, base_url).open()
        assert not home_page.is_user_logged_in
        
        edit_profile = home_page.login(new_user)
        
        available_tasks_page = home_page.click_available_tasks()
        assert available_tasks_page.is_available_tasks_list_visible
        assert len(available_tasks_page.available_tasks) > 0        

        search_text = home_page.search_for_task(random_title) 
        task = available_tasks_page.available_tasks[0]
        task_name = task.name
        task_details = task.click()
        assert task_name == task_details.name
        assert task_details.is_get_started_button_visible
        task_details.click_get_started_button()
        assert task_details.is_abandon_task_button_visible
        assert task_details.is_complete_task_button_visible
        assert task_details.is_save_for_later_button_visible

    @pytest.mark.nondestructive
    def test_reassign_task(self, base_url, selenium, task, new_user, random_title):
        home_page = HomePage(selenium, base_url).open()
        assert not home_page.is_user_logged_in

        edit_profile = home_page.login(new_user)
        assert edit_profile.is_user_logged_in

        available_tasks_page = home_page.click_available_tasks()
        assert available_tasks_page.is_available_tasks_list_visible
        assert len(available_tasks_page.available_tasks) > 0
  
        search_text = home_page.search_for_task(random_title) 
        assert len(available_tasks_page.available_tasks) == 0