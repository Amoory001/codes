from guizero import App, Text, PushButton
def say_hello():
        text.value ="3D"
app = App(title="Hello world")
text = Text(app, text="Welcome to the Hello world app!")
button = PushButton(app, command=say_hello)
app.display()
