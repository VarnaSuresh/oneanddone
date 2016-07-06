# This Source Code Form is subjectfrom django import forms to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest

from pages.home import HomePage


class TestAvailableTasks():
    @pytest.mark.nondestructive
    def test_assign_tasks(self, base_url, selenium, nonrepeatable_assigned_task, task, new_user):
        home_page = HomePage(selenium, base_url).open()
        home_page.login(new_user)
        available_tasks_page = home_page.click_available_tasks()

        # Check if assignable task is found
        home_page.search_for_task(task.name)
        assert len(available_tasks_page.available_tasks)

        home_page.search_for_task(nonrepeatable_assigned_task.name)
        assert len(available_tasks_page.available_tasks) == 0
