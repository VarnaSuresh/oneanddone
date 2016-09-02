# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from pages.home import HomePage


class TestAvailableTasks():

    def test_assigned_task_is_not_available(self, base_url, selenium, assigned_task, new_user):
        home_page = HomePage(selenium, base_url).open()
        home_page.login(new_user)
        available_tasks_page = home_page.click_available_tasks()
        home_page.search_for_task(assigned_task['task'].name)
        available_tasks = [x.name for x in available_tasks_page.available_tasks]
        assert available_tasks.count(assigned_task.name) == 0

    def test_assigned_task_is_available_to_assignee(self, base_url, selenium, assigned_task):
        home_page = HomePage(selenium, base_url).open()
        new_user = {
            'email': assigned_task['user'].email,
            'password': assigned_task['user'].password,
            'name': assigned_task['user'].name,
            'username': assigned_task['user'].username,
            'url': 'http://www.mozilla.org/'
        }
        home_page.login(new_user)
        available_tasks_page = home_page.click_available_tasks()
        home_page.search_for_task(assigned_task['task'].name)
        available_tasks = [x.name for x in available_tasks_page.available_tasks]
        assert available_tasks.count(assigned_task.name) == 1

    def test_that_unassigned_task_is_available(self, base_url, selenium, task, new_user):
        home_page = HomePage(selenium, base_url).open()
        home_page.login(new_user)
        available_tasks_page = home_page.click_available_tasks()
        home_page.search_for_task(task.name)
        available_tasks = [x.name for x in available_tasks_page.available_tasks]
        assert available_tasks.count(task.name) == 1