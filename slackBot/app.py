import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACKBOT_TOKEN"))

@app.message("hello")
def message_hello(message,say):
    say(f"Hey there <@{message['user']}>!")

@app.message("test")
def test(client,message):
    channel_id=message["channel"]
    client.admin_emoji_add(
        name="test",
        url="https://emoji-gen.ninja/emoji_download?align=center&amp;back_color=00000000&amp;color=FF0000FF&amp;font=notosans-mono-bold&amp;locale=ja&amp;public_fg=true&amp;size_fixed=false&amp;stretch=true&amp;text=test"
    )

# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACKAPP_TOKEN"]).start()

