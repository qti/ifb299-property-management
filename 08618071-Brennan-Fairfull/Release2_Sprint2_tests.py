#Selenium test for release     

    def test_admin_property_add_insuffiecient_fields(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
	self.selenium.find_element_by_id("id_username").send_keys("admin")
        self.selenium.find_element_by_id("id_password").clear()
        self.selenium.find_element_by_id("id_password").send_keys("password")
        self.selenium.find_element_by_css_selector("button.btn.btn-primary").click()
        self.selenium.find_element_by_id("field_name").send_keys("housetest")
	self.selenium.find_element_by_css_selector("button.btn.btn-save").click()
	self.assertEqual(self.selenium.current_url, "http://127.0.0.1:8000/admin/properties/property/add/")

    def test_admin_remove_property(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        self.selenium.find_element_by_id("id_username").send_keys("admin")
        self.selenium.find_element_by_id("id_password").clear()
        self.selenium.find_element_by_id("id_password").send_keys("password")
        self.selenium.find_element_by_css_selector("button.btn.btn-primary").click()
	self.selenium.find_element_by_css_selector("button.btn.btn-delete").click()

    def test_admin_edit(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/admin/'))
        self.selenium.find_element_by_id("id_username").clear()
        self.selenium.find_element_by_id("id_username").send_keys("admin")
        self.selenium.find_element_by_id("id_password").clear()
        self.selenium.find_element_by_id("id_password").send_keys("password")
        self.selenium.find_element_by_css_selector("button.btn.btn-primary").click()
	self.selenium.find_element_by_id("field_name").send_keys("housetestedit")
        self.selenium.find_element_by_css_selector("button.btn.btn-save").click()
