# Trend Analizi Scripti (ayrı dosya: trend_analysis.py)
import streamlit as st
from datetime import date
from pytrends.request import TrendReq
import torch

pytrends = TrendReq()

def get_trend_data(keywords, timeframe):
  pytrends.build_payload(keywords, timeframe=timeframe)
  df = pytrends.interest_over_time()
  del df["isPartial"]
  return df

# Gradio Arayüzü (main.py)
import gradio as gr

# Trend analiz fonksiyonunu ayrı scriptten çağır
def analyze_trends(keywords, timeframe):
  df = get_trend_data(keywords, timeframe)
  return df

# Gradio arayüz bileşenleri
interface = gr.Interface(
  fn=analyze_trends,
  inputs=[gr.Textbox("Python","R","C++","Java","HTML"), gr.Textbox("today 5-y")],
  outputs=gr.Dataframe()
)

# Gradio arayüzünü başlat
interface.launch()