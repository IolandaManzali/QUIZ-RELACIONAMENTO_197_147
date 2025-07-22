from datetime import datetime
import streamlit as st

def registrar_evento(session_state, tipo, detalhe=""):
    if "eventos" not in session_state:
        session_state["eventos"] = []
    session_state["eventos"].append({
        "datahora": datetime.now().isoformat(),
        "tipo": tipo,
        "detalhe": detalhe
    })
