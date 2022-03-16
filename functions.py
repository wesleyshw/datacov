import requests


def dados():
    response = requests.get(
        "https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeralApi"
    ).json()
    if response["planilha"]:
        del response["planilha"]
    if response["dt_updated"]:
        del response["dt_updated"]
    return response


def dt_updated():
    headers = {"x-parse-application-id": "unAFkcaNDeXajurGB7LChj8SgQYS2ptm"}
    response = requests.get(
        "https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod/PortalGeral",
        headers=headers,
    ).json()
    return response["results"][0]["dt_atualizacao"]


def regioes():
    url_base = "https://xx9p7hp1p7.execute-api.us-east-1.amazonaws.com/prod"
    headers = {"x-parse-application-id": "unAFkcaNDeXajurGB7LChj8SgQYS2ptm"}
    regiao = requests.get(
        f"{url_base}/PortalSinteseSep", headers=headers
    ).json()[1]
    sul = requests.get(
        f"{url_base}/PortalSinteseSepUfSul", headers=headers
    ).json()
    sudeste = requests.get(
        f"{url_base}/PortalSinteseSepUfSudeste", headers=headers
    ).json()
    norte = requests.get(
        f"{url_base}/PortalSinteseSepUfNorte", headers=headers
    ).json()
    nordeste = requests.get(
        f"{url_base}/PortalSinteseSepUfNordeste", headers=headers
    ).json()
    centro_oeste = requests.get(
        f"{url_base}/PortalSinteseSepUfCentroOeste", headers=headers
    ).json()

    pais, regioes = [], []
    for i in regiao:
        if i["_id"] == "Brasil":
            pais.append(i)
        else:
            if i["_id"] == "Centro-Oeste":
                i["count"] = centro_oeste
                regioes.append(i)
            if i["_id"] == "Sudeste":
                i["count"] = sudeste
                regioes.append(i)
            if i["_id"] == "Sul":
                i["count"] = sul
                regioes.append(i)
            if i["_id"] == "Nordeste":
                i["count"] = nordeste
                regioes.append(i)
            if i["_id"] == "Norte":
                i["count"] = norte
                regioes.append(i)

    return {"Brasil": pais, "Regioes": regioes}
