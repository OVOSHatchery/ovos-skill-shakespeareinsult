from mycroft import MycroftSkill, intent_file_handler


class ShakespeareInsult(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('shakespeareinsult.intent')
    def handle_shakespeareinsult(self, message):
        self.speak_dialog('shakespeareinsult')


def create_skill():
    return ShakespeareInsult()

