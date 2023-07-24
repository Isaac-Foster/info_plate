from dataclasses import dataclass


from httpx import Client

hc =  Client(http2=True, timeout=40)


@dataclass
class Plate:
    ano: int | str | None
    anoModelo: int | str | None
    chassi: str | None
    codigoRetorno: str | None
    codigoSituacao: str | None
    cor: str | None
    data: str | None
    dataAtualizacaoAlarme: str | None
    dataAtualizacaoCaracteristicasVeiculo: str | None
    dataAtualizacaoRouboFurto: str | None
    error: bool | None
    marca: str | None
    modelo: str | None
    municipio: str | None
    origem: str | None
    placa: str | None
    placa_alternativa: str | None
    sitiacao: str | None
    uf: str | None
    usedBackend: str | None


def search(plate: str) -> dict:
    resp = hc.get(
        url="https://infoplaca-api.amanoteam.com/" + plate
    )
    return resp.json()