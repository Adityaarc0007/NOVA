"""
NOVA Brain
"""

from ai.provider import AIProvider
from ai.planner import Planner


class Brain:

    def __init__(self):

        self.provider = AIProvider()
        self.planner = Planner()

    def ask(self, command):

        plan = self.planner.plan(command)

        if plan["type"] == "skill":
            return plan

        if plan["type"] == "memory":
            return plan

        if plan["type"] == "automation":
            return plan

        return {
            "type": "ai",
            "response": self.provider.ask(command)
        }