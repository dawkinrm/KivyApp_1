from kivy.app import App
from kivy.core.audio import SoundLoader

class HelloWorldApp(App):
  def play_music(self):
    self.sound = SoundLoader.load('Jesse_Cook-Dance_Of_Spring.ogg')
    self.sound.play()
  def stop_music(self):
    self.sound.stop()

if __name__ == "__main__":
  HelloWorldApp().run()
