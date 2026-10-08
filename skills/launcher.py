"""
NOVA Application Launcher
"""

import subprocess


class Launcher:

    CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

    CHROME_PROFILES = {
        "aditya": "Profile 1",
        "arc": "Profile 2",
        "nikhil": "Profile 3",
        "nikhil raj": "Profile 4",
        "college": "Profile 5",
        "victor": "Profile 6",
        "person": "Profile 7",
        "guest": "Profile 8",
    }

    APPS = {
        "vs code": "code",
        "visual studio code": "code",
        "notepad": "notepad",
        "calculator": "calc",
        "paint": "mspaint",
        "cmd": "cmd",
        "terminal": "wt",
        "explorer": "explorer",
        "settings": "start ms-settings:",
    }

    def open(self, app: str, profile: str = None) -> bool:

        app = app.lower().strip()

        try:

            # -----------------------
            # Chrome
            # -----------------------

            if app == "chrome":

                if profile is None:

                    subprocess.Popen(
                        [self.CHROME_PATH],
                        shell=False
                    )

                    return True

                profile = profile.lower().strip()

                if profile not in self.CHROME_PROFILES:

                    print(f"Unknown Chrome profile : {profile}")

                    return False

                subprocess.Popen(
                    [
                        self.CHROME_PATH,
                        f'--profile-directory={self.CHROME_PROFILES[profile]}'
                    ],
                    shell=False
                )

                return True

            # -----------------------
            # Other Applications
            # -----------------------

            if app not in self.APPS:

                print(f"Unknown application : {app}")

                return False

            subprocess.Popen(
                self.APPS[app],
                shell=True
            )

            return True

        except Exception as e:

            print("Launcher Error :", e)

            return False