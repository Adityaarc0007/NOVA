import psutil


class SystemMonitor:

    @staticmethod
    def cpu():

        return f"{psutil.cpu_percent()} %"

    @staticmethod
    def ram():

        return f"{psutil.virtual_memory().percent} %"

    @staticmethod
    def battery():

        battery = psutil.sensors_battery()

        if battery:

            return f"{int(battery.percent)} %"

        return "N/A"

    @staticmethod
    def security():

        return "Safe"