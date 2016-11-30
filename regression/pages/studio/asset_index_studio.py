"""
Asset index page
"""
import urllib

from edxapp_acceptance.pages.studio.asset_index import AssetIndexPage
from edxapp_acceptance.pages.common.utils import wait_for_notification

from regression.pages.studio.utils import (
    get_course_key,
    click_css_with_animation_enabled,
)
from regression.pages.studio import BASE_URL


class AssetIndexPageExtended(AssetIndexPage):
    """
    Extended AssetIndex page.
    """
    UPLOAD_FORM_CSS = '.modal-body .title'

    @property
    def url(self):
        """
        Construct a URL to the page within the course.
        """
        course_key = get_course_key(self.course_info)
        url = "/".join(
            [BASE_URL, self.url_path, urllib.quote_plus(unicode(course_key))])
        return url if url[-1] is '/' else url + '/'

    def open_upload_file_prompt(self):
        """
        Open new file upload prompt.
        """
        click_css_with_animation_enabled(
            self, '.button.upload-button.new-button', 0, False)
        self.wait_for_element_visibility(
            self.UPLOAD_FORM_CSS, 'New file upload prompt has been opened.')

    def get_file_names(self):
        """
        Get the names of uploaded files.
        Returns:
            list: Uploaded files.
        """
        return self.q(css='.assets-table tbody tr .title').text

    def get_files_count(self):
        """
        Returns the count of files uploaded.
        """
        return len(self.q(css='#asset-table-body tr'))

    def delete_file(self):
        """
        Deletes the file till delete asset button is found on page
        """
        delete_button = '.remove-asset-button.action-button'
        while self.q(css=delete_button).present:
            self.q(css=delete_button).first.click()
            # Click initiates an ajax call
            self.wait_for_ajax()
            self.q(css='button.action-primary').click()
            self.wait_for_asset_delete_notification()

    def wait_for_asset_delete_notification(self):
        """
        Waits for the notification to appear and
        disappear on the given page (subclass of PageObject).
        """
        def is_shown():
            """
            Whether or not the notification is currently showing.
            """
            return self.q(
                css='.wrapper.wrapper-notification.'
                    'wrapper-notification-confirmation.is-shown').present

        def is_hidden():
            """
            Whether or not the notification is finished showing.
            """
            return self.q(
                css='.wrapper.wrapper-notification.'
                    'wrapper-notification-confirmation.is-hiding').present

        self.wait_for(is_shown, 'Notification should have been shown.')
        self.wait_for(is_hidden, 'Notification should have been hidden.')

    def lock_asset(self, index=0):
        """
        Lock the asset.
        Arguments:
            index (int): index of file to lock.
        """
        self.q(
            css='.assets-table tbody tr'
                ' .actions-col .lock-checkbox').results[index].click()
        wait_for_notification(self)

    def sort_assets(self):
        """
        Sort the assets
        """
        click_css_with_animation_enabled(self, '.column-sort-link', 0, False)

    def get_page_count(self):
        """
        Returns: Current page count in integers
        """
        return self.q(css='.current-page').text[0]

    def click_next_page_link(self):
        """
        Clicks next page link
        """
        self.q(css='.next-page-link').first.click()
        # Click initiates an ajax call
        self.wait_for_ajax()
