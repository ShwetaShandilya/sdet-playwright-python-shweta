import os
from dotenv import load_dotenv

load_dotenv()


class ConfigReader:

    @staticmethod
    def get_base_url():
        return os.getenv("BASE_URL")

    @staticmethod
    def get_browser():
        return os.getenv("BROWSER", "chromium")

    @staticmethod
    def get_headless():
        return os.getenv("HEADLESS", "true").lower() == "true"