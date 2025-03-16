from django.test import SimpleTestCase, TestCase
from django.urls import reverse

# Create your tests here.
#


class HomePageTests(SimpleTestCase):
    """
    Test suite for verifying the homepage view functionality.

    This test case ensures that the homepage is accessable both via
    its direct URL ("/") and through its named URL ("home").

    It also verifies that the correct template is used and that
    expected content is present on the page.
    """

    def test_url_exists_at_correct_location_homepageview(self):
        """
        Verify that the homepage URL ("/")

        This method simulates a GET request to the root URL ("/")
        and asserts that the server returns a 200 OK status code,
        indicating that the homepage is correctly set up.
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_homepage_view(self):
        """
        Verify that the homepage view is correctly configured and renders
        as expected. This method uses Django's `reverse` function to resolve
        the URL by its name ("home") and then simulates a GET request to URL.

        It asserts the following:
            - The response status code is 200 OK.
            - The "home.html" template is used to render the response.
            - The rendered page contains the text "Home", confirming
                that the expected content is displayed.
        """
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "Home")
