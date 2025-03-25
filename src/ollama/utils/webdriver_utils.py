from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import logging

logger = logging.getLogger(__name__)

class WebDriverManager:
    @staticmethod
    def get_chrome_driver(headless: bool = True) -> webdriver.Chrome:
        try:
            chrome_options = Options()
            if headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")

            # Auto-install/update ChromeDriver
            service = Service(ChromeDriverManager().install())

            return webdriver.Chrome(
                service=service,
                options=chrome_options
            )
        except Exception as e:
            logger.error(f"Failed to initialize Chrome WebDriver: {str(e)}")
            raise
