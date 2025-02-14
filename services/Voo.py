from model.Voo import VooModel
import plotly.express as px
import plotly.io as pio
import pandas as pd

class VooService:
    def filtrarDados(mercado, ano_inicio, ano_fim, mes_inicio, mes_fim):
        df = VooModel.find_by_filters(mercado, ano_inicio, ano_fim, mes_inicio, mes_fim)
        dashboard = px.line(df, x="data", y="rpk", title=f"RPK para o mercado que contém {mercado}")
        dashboard.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=df["data"],
                ticktext=[date.strftime("%m/%Y") for date in df["data"]]
            )
        )

        grafico_html = pio.to_html(dashboard, full_html=False)
        return grafico_html