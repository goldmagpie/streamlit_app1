import json
import streamlit as st
from pathlib import Path
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo

st.set_page_config(layout = "wide")

with st.sidebar:
    st.title("🗓️ #30DaysOfStreamlit")
    st.header("Day 27 - Streamlit Elements")
    st.write("Streamlit Elements를 사용하여 드래그 가능하고 크기 조절 가능한 대시보드 만들기.")
    st.write("---")
    
    media_url = st.text_input("미디어 URL", value="https://www.youtube.com/watch?v=vIQQR_yq-8I")

if "data" not in st.session_state:
    st.session_state.data = Path("pages/data.json").read_text()

layout = [
    dashboard.Item("editor", 0, 0, 6, 3),
    dashboard.Item("chart", 6, 0, 6, 3),
    dashboard.Item("media", 0, 2, 12, 4),
]

with elements("demo"):
    with dashboard.Grid(layout, draggableHandle=".draggable"):
        with mui.Card(key="editor",sx={"display":"flex","flexDirection":"column"}):
            mui.CardHeader(title="Editor",className="draggable")
            with mui.CardContent(sc={"flex":1,"minHeight":0}):
                editor.Monaco(
                    defaultValue=st.session_state.data,
                    laguage="json",
                    onChange=lazy(sync("data"))
                )
            with mui.CardActions:
                mui.Button("변경 사항 적용", onClick=sync())
        with mui.Card(key="chart", sx={"display":"flex","flexDirection":"column"}):
            mui.CardHeader(title="차트", className = "draggable")
            with mui.CardContent(sx={"flex":1, "minHeight":0}):
                nivo.Bump(
                    data=json.loads(st.session_state.data),
                    colors={ "scheme": "spectral" },
                    lineWidth=3,
                    activeLineWidth=6,
                    inactiveLineWidth=3,
                    inactiveOpacity=0.15,
                    pointSize=10,
                    activePointSize=16,
                    inactivePointSize=0,
                    pointColor={ "theme": "background" },
                    pointBorderWidth=3,
                    activePointBorderWidth=3,
                    pointBorderColor={ "from": "serie.color" },
                    axisTop={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": -36
                    },
                    axisBottom={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "",
                        "legendPosition": "middle",
                        "legendOffset": 32
                    },
                    axisLeft={
                        "tickSize": 5,
                        "tickPadding": 5,
                        "tickRotation": 0,
                        "legend": "ranking",
                        "legendPosition": "middle",
                        "legendOffset": -40
                    },
                    margin={ "top": 40, "right": 100, "bottom": 40, "left": 60 },
                    axisRight=None,
                )
        with mui.Card(key="media", sx={"display": "flex", "flexDirection": "column"}):
            mui.CardHeader(title="미디어 플레이어", className="draggable")
            with mui.CardContent(sx={"flex": 1, "minHeight": 0}):
                media.Player(url=media_url, width="100%", height="100%", controls=True)

