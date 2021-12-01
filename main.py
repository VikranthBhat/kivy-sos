from kivy.app import  App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from plyer import vibrator,camera

Builder.load_file("design.kv")

class LoginScreen(Screen):
    def setMessage(self):
        self.manager.current = "set message"

    def sendSOS(self):
        print("SOS sent")
        self.ids.status.text = "SOS sent"
        vibrator.vibrate(10)
        camera.take_picture()

class SetMessage(Screen):
    def save_message(self, message_data):
        with open("critical_message.txt","w") as f:
            f.write(message_data)

class RootWidget(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    MainApp().run()
