import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QVBoxLayout, QPushButton

class UrlCheckerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("URL Checker App")
        self.setGeometry(100, 100, 800, 600)

        self.origin_label = QLabel("Origin:")
        self.origin_entry = QLineEdit("https://lereve-lounge.karekodapp.com.tr/")

        self.dirs_label = QLabel("Directories:")
        self.dirs_entry = QTextEdit("/.htaccess\n/application\n/cgi-bin\n/charles\n"
                                    "/fileman\n/fileman/css\n/fileman/images\n/fileman/js\n"
                                    "/fileman/lang\n/fileman/php\n/fileman/tmp\n/fileman/Uploads\n"
                                    "/index.php\n/public\n/public/admin\n/public/admin/advanced-alertify.html")

        self.result_text = QTextEdit()

        self.check_button = QPushButton("Check URLs")
        self.check_button.clicked.connect(self.check_urls)

        layout = QVBoxLayout(self)
        layout.addWidget(self.origin_label)
        layout.addWidget(self.origin_entry)
        layout.addWidget(self.dirs_label)
        layout.addWidget(self.dirs_entry)
        layout.addWidget(self.check_button)
        layout.addWidget(self.result_text)

    def check_urls(self):
        origin = self.origin_entry.text()
        dirs = self.dirs_entry.toPlainText().splitlines()
        self.result_text.clear()

        for dir_path in dirs:
            check_result = self.check_url(origin, dir_path)
            self.result_text.append(check_result)

    def check_url(self, origin, dir_path):
        url = origin + dir_path
        try:
            response = requests.get(url)
            status = response.status_code
            return f"URL: {url} - Status: {status} - {'OK' if status == 200 else 'Not OK'}\n"
        except requests.exceptions.RequestException as e:
            return f"URL: {url} - Error: {e}\n"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UrlCheckerApp()
    window.show()
    sys.exit(app.exec_())
