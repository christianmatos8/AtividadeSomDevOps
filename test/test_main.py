
from src.main import *
from fastapi.testclient import TestClient

client = TestClient(app)

def test_gerar_nome_valido():
    nome = gerar_nome()
    assert any(nome.startswith(pref) for pref in prefixos)
    assert any(nome.endswith(suf) for suf in sufixos)

def test_escolher_categoria_valida():
    categoria = escolher_categoria()
    assert categoria in categorias

def test_read_root():
    data = client.get("/").json()
    assert data == {"message": "Olá!"}

def test_endpoint_nome():
    data = client.get("/nome").json()
    assert "nome" in data
    assert any(data["nome"].startswith(pref) for pref in prefixos)
    assert any(data["nome"].endswith(suf) for suf in sufixos)

def test_endpoint_categoria():
    data = client.get("/categoria").json()
    assert "categoria" in data
    assert data["categoria"] in categorias
#teste 