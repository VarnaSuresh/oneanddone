# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.base import Base
from pages.tasks.regions.task import Task


class AvailableTasksPage(Base):

    URL_TEMPLATE = '/tasks/available'

    _available_tasks_list_locator = (By.CSS_SELECTOR, '.task-list > li')
    _displayed_profile_name_locator = (By.CSS_SELECTOR, '.content-container > h3')

    @property
    def available_tasks(self):
        return [Task(self, web_element) for web_element in
                self.find_elements(*self._available_tasks_list_locator)]

    @property
    def displayed_profile_name(self):
        return self.find_element(*self._displayed_profile_name_locator).text

    @property
    def is_available_tasks_list_visible(self):
        return self.is_element_displayed(*self._available_tasks_list_locator)
