from guizero import App, Text, TextBox, PushButton

def update_message():
    name = name_input.value
    message.value = f"Hello, {name}!" if name else "Hello, world!"

app = App(title="Hello App")

message = Text(app, text="Welcome to the app")
name_input = TextBox(app, width=30, placeholder="Enter your name")
button = PushButton(app, command=update_message, text="Greet Me")

app.display()
