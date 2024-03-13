import os
import gradio as gr

from openai import OpenAI

URL = "https://neural-magic-llm-poc-predictor-openvino.apps.cluster-h9jwq.dynamic.redhatworkshops.io"

def get_answer(question, url):
    client = OpenAI(base_url=url, api_key="EMPTY")
    model = client.models.list().data[0][1]
    print(f"Accessing model API '{model}'")

    completion = client.completions.create(model=model, prompt=question, max_tokens=100, temperature=0.2)
    return completion.choices[0].text

port = os.environ.get('FLASK_PORT') or 8080

iface = gr.Interface(fn=get_answer,
                     inputs=["text", gr.Dropdown(choices=[URL])],
                     outputs="text")

iface.launch(server_port=port)
