import gradio as gr
import pandas as pd
import random

# Деректерді жүктеу
df = pd.read_csv("car_models.csv")

def predict_car_brand(car_type):
    filtered = df[df["Тип"].str.lower() == car_type.lower()]
    if len(filtered) == 0:
        return "Мұндай тип табылмады. Басқа енгізіп көріңіз."
    return random.choice(filtered["Марка"].tolist())

demo = gr.Interface(
    fn=predict_car_brand,
    inputs=gr.Dropdown(
        ["седан", "пикап", "гибрид", "универсал", "внедорожник", "купе", "кабриолет", "минивэн", "хэтчбек"],
        label="Көлік типін таңдаңыз"
    ),
    outputs="text",
    title="🚗 Көлік маркасын болжау моделі",
    description="Тип енгізіңіз (мысалы: седан, пикап, гибрид) — модель сәйкес марканы болжайды."
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=8080)
