#tests taken from test.py to show test for Release 2 sprint 1    

    def test_login_just_name(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/login/?next=/admin/'))
        self.selenium.find_element_by_id("id_username").clear()
        self.selenium.find_element_by_id("id_username").send_keys("admin")
        self.selenium.find_element_by_css_selector("button.btn.btn-primary").click()
        self.assertEqual(self.selenium.current_url, "http://localhost:8081/admin/login/?next=/admin/")

    def test_login_just_pass(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        self.selenium.find_element_by_id("id_password").clear()
        self.selenium.find_element_by_id("id_password").send_keys("password")
        self.selenium.find_element_by_css_selector("button.btn.btn-primary").click()
        self.assertEqual(self.selenium.current_url, "http://localhost:8081/admin/login/?next=/admin/")

    def test_successful_login_logout(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        self.selenium.find_element_by_id("id_username").clear()
        self.selenium.find_element_by_id("id_username").send_keys("admin")
        self.selenium.find_element_by_id("id_password").clear()
        self.selenium.find_element_by_id("id_password").send_keys("password")
        self.selenium.find_element_by_css_selector("button.btn.btn-primary").click()
        self.assertEqual(self.selenium.current_url, "http://localhost:8081/admin/login/?next=/admin/")

    def test_incorrect_login_details(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        self.selenium.find_element_by_id("id_username").clear()
        self.selenium.find_element_by_id("id_username").send_keys("admin")
        self.selenium.find_element_by_id("id_password").clear()
        self.selenium.find_element_by_id("id_password").send_keys("passw1rd")
        self.selenium.find_element_by_css_selector("button.btn.btn-primary").click()
        self.assertEqual(self.selenium.current_url, "http://localhost:8081/admin/login/?next=/admin/")


