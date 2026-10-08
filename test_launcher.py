from skills.launcher import Launcher

launcher = Launcher()

while True:

    app = input("Open : ").strip().lower()

    if app == "exit":
        break

    if app.startswith("chrome "):

        profile = app.replace("chrome", "").strip()

        ok = launcher.open(
            "chrome",
            profile
        )

    else:

        ok = launcher.open(app)

    print(ok)