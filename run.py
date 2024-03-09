import bot
import info


class Manage:
    def __init__(self):
        ...
    def run(self):
        try:
            bot.client.run(bot.TOKEN)
        except Exception as ex:
            print(f'{ex}\nBot connection error. Check your internet connection.')


if __name__ == '__main__':
    manage = Manage()
    manage.run()
