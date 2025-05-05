from playwright.sync_api import sync_playwright

class AblespaceLogin:
    def __init__(self):
        self.browser = None
        self.page = None

    def launch_application(self):
        self.browser = self.playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://app.ablespace.io/signin")
        print("Application opened successfully.")
        print(self.page.title())
        self.page.wait_for_timeout(2000)

    def enter_email(self, email):
        email_field = self.page.wait_for_selector("//input[@name='email']")
        email_field.click()
        email_field.fill(email)
        self.page.wait_for_timeout(3000)

        email_text = email_field.input_value()
        if email_text == email:
            print(f"\nEmail entered successfully. The email is {email_text}")
        else:
            print("Email is not entered.")
        self.page.wait_for_timeout(3000)

    def click_continue(self):
        continue_button = self.page.wait_for_selector("//div[normalize-space()='Continue']")
        continue_button.click()
        self.page.wait_for_timeout(3000)

    def enter_password(self, password):
        password_field = self.page.wait_for_selector("//input[@id='password']")
        if password_field.is_visible():
            print("Continue button is clicked.")
        else:
            print("Continue button do not have clickability.")

        password_field.type(password)
        password_text = password_field.input_value()
        print("Password:", password_text)

    def click_sign_in(self):
        sign_in_button = self.page.wait_for_selector("//div[normalize-space()='Sign In']")
        sign_in_button.click()
        self.page.wait_for_timeout(3000)

    def verify_login(self):
        calendar_page = self.page.wait_for_selector("//h1[normalize-space()='Calendar']")
        if calendar_page.is_visible():
            print(f"Login was successful and {calendar_page.text_content()} page is loaded.")
        else:
            print("Login failed due to incorrect credentials.")
        self.page.wait_for_timeout(5000)

    def caseload_click(self):
        caseload=self.page.wait_for_selector("//a[@aria-label='Caseload']")
        caseload.click()
        self.page.wait_for_timeout(3000)

    def add_student(self, first_name, last_name):
        add_student=self.page.wait_for_selector("//span[contains(text(),'Add Student')]")
        if add_student.is_visible():
            print("Caseload tab has clicked.")
        else:
            print("Caseload tab has not clicked.")
        self.page.wait_for_timeout(5000)

        add_student.click()
        self.page.wait_for_timeout(3000)

        add_student_manually=self.page.wait_for_selector("//div[@aria-label='Add Student']")
        if add_student_manually.is_visible():
            print("Add student button is clicked.")
        else:
            print("Add student button is not clicked.")

        self.page.wait_for_timeout(3000)

        add_student_manually.click()
        self.page.wait_for_timeout(3000)

        student_first_name=self.page.wait_for_selector("//input[@aria-label='First Name']")
        student_first_name.fill(first_name)

        self.page.wait_for_timeout(2000)

        student_last_name=self.page.wait_for_selector("//input[@aria-label='Last Name']")
        student_last_name.fill(last_name)

        self.page.wait_for_timeout(2000)

        create_button=self.page.wait_for_selector("//div[contains(text(),'Create')]")
        create_button.click()

        # Now safely wait for success message with higher timeout
        try:
            success_message = self.page.wait_for_selector(
                "//div[contains(text(), 'Student created successfully')]",
                timeout=60000  # waits up to 60 seconds if needed
            )
            if success_message.is_visible():
                print(f"Student was created successfully. Success message is {success_message.text_content()}")
            else:
                print("Student not created.")
        except Exception as e:
            print("Error waiting for student creation success message:", e)

        self.page.wait_for_timeout(5000)

    def run(self, email, password):
        with sync_playwright() as playwright:
            self.playwright = playwright
            self.launch_application()
            self.enter_email(email)
            self.click_continue()
            self.enter_password(password)
            self.click_sign_in()
            self.verify_login()
            self.caseload_click()
            self.add_student("Sri", "Sai")
            self.browser.close()

if __name__ == "__main__":
    app = AblespaceLogin()
    app.run(email="pulkitmahour15jan+6@gmail.com", password="12345678")
