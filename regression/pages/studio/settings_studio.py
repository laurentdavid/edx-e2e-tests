"""
Course Schedule and Details Settings page.
"""
from edxapp_acceptance.pages.studio.settings import SettingsPage
from regression.pages import UPLOAD_FILE_DIR

from regression.pages.studio.utils import (
    get_course_key,
    click_css_with_animation_enabled
)
from regression.pages.studio import BASE_URL


class SettingsPageExtended(SettingsPage):
    """
    Course Schedule and Details Settings page.
    """

    @property
    def url(self):
        """
        Construct a URL to the page within the course.
        """
        course_id = get_course_key(self.course_info)
        return BASE_URL + "/" + self.url_path + "/" + unicode(course_id)

    def upload_course_image(self, file_name):
        """
        Uploads course image without saving it.

        Arguments:
            file_name: file name to be uploaded.
        """
        click_css_with_animation_enabled(
            self, '.action.action-upload-image', 0, False
        )
        file_input_css = '.upload-dialog input'
        self.browser.execute_script(
            '$("{}").css("display","block");'.format(file_input_css)
        )
        self.wait_for_element_visibility(
            file_input_css, "Upload button is visible."
        )
        self.q(css=file_input_css).results[0].send_keys(
            UPLOAD_FILE_DIR + "/" + file_name)

    def cancel_upload(self):
        """
        Click 'cancel' on the file upload dialog.
        """
        click_css_with_animation_enabled(
            self, '.button.action-cancel', 0, False
        )

    def click_other_settings_links(self, link):
        """
        Clicks links under other course settings as per link provided
        """
        self.q(
            css='.nav-related a[' + link + ']'
        ).click()
