from flask import flash

from model.MercadoModel import MercadoModel
import plotly.express as px
import plotly.io as pio

class MercadoService:
    def filtrarDados(empresa_sigla, mercado, mes_inicio, ano_inicio, mes_fim, ano_fim):
        df = MercadoModel.find_by_filters(
            empresa_sigla=empresa_sigla,
            mercado=mercado,
            mes_inicio=mes_inicio,
            ano_inicio=ano_inicio,
            mes_fim=mes_fim,
            ano_fim=ano_fim
        )

        if df is None:
            return df

        dashboard = px.line(df, x="data", y="rpk", title=f"RPK para a empresa {empresa_sigla} e o mercado que contém {mercado}",
                            line_shape="spline",
                            markers=True)

        dashboard.update_traces(line=dict(width=3, color='#ff5a00'))
        dashboard.update_layout(
            title=dict(
                font=dict(size=18, family="Arial", color="black"),
                xanchor='center',
                x=0.5,
                y=0.9
            ),

            xaxis = dict(
                    title="Data",
                    tickmode='array',
                    tickvals=df["data"].unique(),
                    ticktext=[date.strftime("%m/%Y") for date in df["data"].unique()],
                    tickangle=-45,
                    showgrid=True,
                    gridcolor="lightgray"
                ),

            yaxis = dict(
                title="RPK",
                showgrid=True,
                gridcolor="lightgray"
            ),

            plot_bgcolor = "white",
            paper_bgcolor = "white",

            font = dict(
                size=12, family="Arial", color="black"
            )
        )


        grafico_html = pio.to_html(dashboard, full_html=False)
        return grafico_html