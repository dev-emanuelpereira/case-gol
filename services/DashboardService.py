from model.MercadoModel import MercadoModel
import plotly.express as px
import plotly.io as pio

class MercadoService:
    def filtrarDados(mercado, mes_inicio, ano_inicio, mes_fim, ano_fim):
        df = MercadoModel.find_by_filters(mercado, mes_inicio, ano_inicio, mes_fim, ano_fim)
        dashboard = px.line(df, x="data", y="rpk", title=f"RPK para o mercado que contém {mercado}")
        dashboard.update_layout(
        xaxis = dict(
            tickmode='array',
            tickvals=df["data"].unique(),
            ticktext=[date.strftime("%m/%Y") for date in df["data"].unique()]
        )
    )
        grafico_html = pio.to_html(dashboard, full_html=False)
        return grafico_html