# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.base import Base
from pages.tasks.regions.task import Task
from pages.tasks.task_details import TaskDetailsPage
from pages.tasks.available_tasks import AvailableTasksPage

import time


class HomePage(Base):

    _displayed_profile_name_locator = (By.CSS_SELECTOR, '.billboard h3')
    _task_in_progress_locator = (By.ID, 'task-in-progress')
    _pick_a_task_locator = (By.ID, 'pick-a-task')
    _suggested_first_tasks_heading_locator = (By.CSS_SELECTOR, '.task-list-container h3')
    _suggested_first_task_locator = (By.CSS_SELECTOR, '.task-list > li')
    _available_tasks_locator = (By.ID, 'available-tasks')
    _create_task_button = (By.CSS_SELECTOR, '.actions-container > a.button')
    _find_task_title = (By.CSS_SELECTOR, '#id_name')
    _find_task_team = (By.CSS_SELECTOR, '#id_team')
    _find_task_repeatable = (By.CSS_SELECTOR, '#id_repeatable')
    _find_task_instructions = (By.CSS_SELECTOR, '.ace_text-input')
    _submit_task_button = (By.CSS_SELECTOR, ' .actions-container > .button')
    _choose_team = (By.CSS_SELECTOR, ' #id_team option:nth-child(2)')
    _instruction_locator = (By.CSS_SELECTOR, '.django-ace-widget')
    _find_search_button = (By.CSS_SELECTOR, '#id_search')

    @property
    def displayed_profile_name(self):
        return self.find_element(self._displayed_profile_name_locator).text

    @property
    def is_task_in_progress(self):
        return self.is_element_displayed(self._task_in_progress_locator)

    @property
    def task_in_progress(self):
        return self.find_element(self._task_in_progress_locator).text

    @property
    def is_suggested_first_tasks_heading_visible(self):
        return self.is_element_displayed(self._suggested_first_tasks_heading_locator)

    @property
    def suggested_first_tasks(self):
        return [Task(self, web_element) for web_element in
                self.find_elements(self._suggested_first_task_locator)]

    def click_task_in_progress(self):
        self.find_element(self._task_in_progress_locator).click()
        return TaskDetailsPage(self.selenium, self.base_url).wait_for_page_to_load()

    def click_pick_a_task_button(self):
        self.find_element(self._pick_a_task_locator).click()
        return AvailableTasksPage(self.selenium, self.base_url).wait_for_page_to_load()

    def click_available_tasks(self):
        self.find_element(self._available_tasks_locator).click()
        return AvailableTasksPage(self.selenium, self.base_url).wait_for_page_to_load()

    def click_create_task(self, task_name):
        self.find_element(self._create_task_button).click()
        assert self.is_element_displayed(self._find_task_title)
        title = self.find_element(self._find_task_title)
        title.send_keys(task_name)
        assert self.is_element_displayed(self._find_task_team)
        self.find_element(self._find_task_team).click()
        assert self.is_element_displayed(self._choose_team)
        self.find_element(self._choose_team).click()
        assert self.is_element_displayed(self._instruction_locator)
        self.find_element(self._instruction_locator).click()
        instructions = self.find_element(self._find_task_instructions)
        instructions.send_keys("This is a non repeatable task")
        assert self.is_element_displayed(self._find_task_repeatable)
        self.find_element(self._find_task_repeatable).click()
        time.sleep(5)
        self.find_element(self._submit_task_button).click()
        time.sleep(5)

    def search_for_task(self, task_name):
        search_text = self.find_element(self._find_search_button)
        search_text.send_keys(task_name)
        search_text.send_keys(Keys.RETURN)
