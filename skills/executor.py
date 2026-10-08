"""
NOVA Skill Executor
"""

from skills.launcher import Launcher


class Executor:

    def __init__(self):
        self.launcher = Launcher()

    def execute(self, plan: dict):

        if plan.get("type") != "skill":
            return False, "Invalid skill."

        action = plan.get("action")
        target = plan.get("target")
        profile = plan.get("profile")

        # OPEN
        if action == "open":

            success = self.launcher.open(
                target,
                profile
            )

            if success:

                if profile:
                    return True, f"Opening {target} {profile}."

                return True, f"Opening {target}."

            return False, f"Unable to open {target}."

        # CLOSE
        if action == "close":
            return False, "Close feature is not implemented yet."

        return False, "Unknown action."