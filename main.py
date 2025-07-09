import chainlit as cl
import requests
import json

API_URL = "https://crud-ai-agent.vercel.app/agent/"


@cl.on_chat_start
async def on_chat_start():
    await cl.Message(content="👋 Welcome to the XapRise AI Agent! Ask anything below.").send()


@cl.on_message
async def on_message(message: cl.Message):
    user_input = message.content

    try:
        headers = {'Content-Type': 'application/json'}
        payload = {"user_input": user_input}

        response = requests.post(API_URL, data=json.dumps(payload), headers=headers)

        print("RAW RESPONSE:", response.text)

        if response.status_code == 200:
            # Try parsing JSON
            try:
                data = response.json()
                reply = str(data)
            except Exception:
                reply = response.text
        else:
            reply = f"❌ Error {response.status_code}:\n{response.text}"

    except Exception as e:
        reply = f"⚠️ Exception:\n{str(e)}"

    await cl.Message(content=reply).send()
