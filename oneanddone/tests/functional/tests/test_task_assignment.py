# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home import HomePage


class TestAvailableTasks():

    @pytest.mark.nondestructive
    def test_assigned_task_is_not_available(self, base_url, selenium, assigned_task, new_user):
        home_page = HomePage(selenium, base_url).open()
        home_page.login(new_user)
        available_tasks_page = home_page.click_available_tasks()
        home_page.search_for_task(assigned_task['task'].name)
        assert len(available_tasks_page.available_tasks) == 0
        assert assigned_task['task'].is_available_to_user(assigned_task['user']) == True

    @pytest.mark.nondestructive
    def test_that_unassigned_task_is_available(self, base_url, selenium, task, new_user):
        home_page = HomePage(selenium, base_url).open()
        home_page.login(new_user)
        available_tasks_page = home_page.click_available_tasks()
        home_page.search_for_task(task.name)
        assert len(available_tasks_page.available_tasks)
