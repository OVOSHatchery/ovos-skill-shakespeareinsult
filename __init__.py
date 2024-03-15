from ovos_workshop.skills import OVOSSkill
from ovos_workshop.decorators import intent_handler


class ShakespeareInsult(OVOSSkill):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @intent_handler('shakespeareinsult.intent')
    def handle_shakespeareinsult(self, message):
        self.speak_dialog('shakespeareinsult')
