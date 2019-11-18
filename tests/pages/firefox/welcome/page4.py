# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

from selenium.webdriver.common.by import By

from pages.firefox.base import FirefoxBasePage
from pages.regions.modal import Modal
from pages.regions.send_to_device import SendToDevice


class FirefoxWelcomePage4(FirefoxBasePage):

    URL_TEMPLATE = '/{locale}/firefox/welcome/3/'

    _modal_primary_button_locator = (By.CSS_SELECTOR, '.primary-cta .js-modal-link')
    _modal_secondary_button_locator = (By.CSS_SELECTOR, '.secondary-cta .js-modal-link')
    _get_firefox_qr_code_locator = (By.ID, 'firefox-qr')

    @property
    def send_to_device(self):
        return SendToDevice(self)

    @property
    def is_firefox_qr_code_displayed(self):
        return self.is_element_displayed(*self._get_firefox_qr_code_locator)

    def open_modal(self, locator):
        modal = Modal(self)
        self.find_element(*locator).click()
        self.wait.until(lambda s: modal.is_displayed)
        return modal

    @property
    def is_primary_modal_button_displayed(self):
        return self.is_element_displayed(*self._modal_primary_button_locator)

    @property
    def is_secondary_modal_button_displayed(self):
        return self.is_element_displayed(*self._modal_secondary_button_locator)
