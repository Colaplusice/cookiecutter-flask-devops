from flask_script import Command, Manager, Shell

from app import create_app
from migrate import run

app = create_app()
manager = Manager(app)

manager.add_command("shell", Shell())
manager.add_command("migrate", Command(run))

if __name__ == "__main__":
    manager.run()
