"""
NOVA Planner
-------------
Decides how a command should be handled.
"""


class Planner:

    def __init__(self):

        self.skill_keywords = {

            "open": [
                "chrome",
                "google chrome",
                "vs code",
                "visual studio code",
                "notepad",
                "calculator",
                "paint",
                "cmd",
                "terminal",
                "explorer",
                "settings"
            ],

            "close": [
                "chrome",
                "vs code",
                "notepad"
            ]
        }

    def plan(self, command: str):

        command = command.lower().strip()

        # Memory Commands
        if command.startswith("remember"):
            return {
                "type": "memory",
                "command": command
            }

        # Automation Commands
        if command.startswith("schedule"):
            return {
                "type": "automation",
                "command": command
            }

        # Desktop Skills
        for action, apps in self.skill_keywords.items():

            if action in command:

                for app in apps:

                    if app in command:

                        return {
                            "type": "skill",
                            "action": action,
                            "target": app
                        }

        # Default → AI
        return {
            "type": "ai"
        }