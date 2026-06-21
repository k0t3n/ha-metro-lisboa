DOMAIN = "metro_lisboa"
API_URL = "https://app.metrolisboa.pt/status/getLinhas.php"
SCAN_INTERVAL = 1  # minutes

LINES: dict[str, str] = {
    "amarela": "Linha Amarela",
    "azul": "Linha Azul",
    "verde": "Linha Verde",
    "vermelha": "Linha Vermelha",
}

LINE_MSG_KEYS: dict[str, str] = {
    "amarela": "tipo_msg_am",
    "azul": "tipo_msg_az",
    "verde": "tipo_msg_vd",
    "vermelha": "tipo_msg_vm",
}
