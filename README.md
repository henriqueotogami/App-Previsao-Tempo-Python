# App de Previsão do Tempo - Python

> Aplicação de previsão do tempo desenvolvida como back-end do curso de Python 3 na Udemy (Junho/2020), utilizando APIs de geolocalização e clima.

<div align="center">
<img src="https://img.shields.io/github/release-date/henriqueotogami/App-Previsao-Tempo-Python">
</div>
<br>
<div align="center">
<img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/henriqueotogami/App-Previsao-Tempo-Python">
<img src="https://img.shields.io/github/issues/henriqueotogami/App-Previsao-Tempo-Python">
</div>
<br>
<div align="center">
<img src="https://img.shields.io/github/forks/henriqueotogami/App-Previsao-Tempo-Python?style=flat">
<img src="https://img.shields.io/github/stars/henriqueotogami/App-Previsao-Tempo-Python?style=flat">
<img src="https://img.shields.io/github/license/henriqueotogami/App-Previsao-Tempo-Python">
</div>

---

## 📋 Sobre o Projeto

Este projeto contém uma aplicação em Python para consulta de previsão do tempo, desenvolvida durante o curso de Python 3 na Udemy. Os scripts consomem APIs externas para obter localização (por IP ou por nome da cidade), clima atual e previsão para cinco dias. O código inclui versões progressivas das aulas (clima atual, previsão 5 dias e pesquisa por local).

**Professor do curso:** Ivan Lourenço Gomes.

## 📁 Estrutura do Projeto

### Scripts por funcionalidade

| Arquivo | Descrição |
|--------|-----------|
| **Aula30 - Previsao Atual.py** | Clima atual com base na localização do IP |
| **Aula37 - Previsao 5 Dias.py** | Clima atual + previsão para 5 dias (localização por IP) |
| **Aula43-Pesquisa-do-Local.py** | Aplicação completa: IP + 5 dias + busca por cidade e Estado |

### Estrutura do repositório

```
LICENSE
README.md
requirements.txt
Aula30 - Previsao Atual.py    # clima atual (IP)
Aula37 - Previsao 5 Dias.py   # clima atual + 5 dias (IP)
Aula43-Pesquisa-do-Local.py   # app completo com busca por cidade
```

## 🛠️ Tecnologias Utilizadas

- **Python 3** — Linguagem de programação
- **requests** — Requisições HTTP às APIs
- **Geoplugin** — Geolocalização por IP (latitude/longitude)
- **AccuWeather** — Condições atuais e previsão (geoposition, currentconditions, forecasts)
- **Mapbox** — Geocoding (busca por nome da cidade e Estado)

## 📝 APIs Utilizadas

| API | Uso |
|-----|-----|
| **Geoplugin** (JSON) | Obter latitude e longitude a partir do IP |
| **AccuWeather – geoposition** | Obter código do local a partir de lat/long |
| **AccuWeather – currentconditions** | Clima atual pelo código do local |
| **AccuWeather – forecasts** | Previsão para 5 dias |
| **Mapbox – geocoding** | Coordenadas a partir de cidade e Estado |

## 🚀 Como Executar

### 1. Clonar e entrar no projeto

```bash
git clone https://github.com/henriqueotogami/App-Previsao-Tempo-Python.git
cd App-Previsao-Tempo-Python
```

### 2. Criar ambiente virtual (recomendado)

```bash
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# ou: venv\Scripts\activate  # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Configurar chaves de API

Nos arquivos `.py`, substitua:

- `accuweatherAPIKey = 'INSERT YOUR KEY HERE'` pela sua chave em [AccuWeather](https://developer.accuweather.com/).
- No **Aula43-Pesquisa-do-Local.py**: `mapboxToken = "INSERT YOUR MAPBOX TOKEN HERE"` pelo seu token em [Mapbox](https://www.mapbox.com/).

### 5. Executar

```bash
# Clima atual (localização por IP)
python "Aula30 - Previsao Atual.py"

# Clima atual + previsão 5 dias (localização por IP)
python "Aula37 - Previsao 5 Dias.py"

# App completo (IP + 5 dias + busca por cidade e Estado)
python Aula43-Pesquisa-do-Local.py
```

## ⚙️ Como Funciona

### Fluxo geral (Aula43 – versão completa)

1. **Localização inicial:** Requisição ao Geoplugin retorna latitude e longitude do IP.
2. **Código do local:** AccuWeather (geoposition) devolve o código e nome do local.
3. **Clima atual:** AccuWeather (currentconditions) retorna condição e temperatura.
4. **Previsão 5 dias:** AccuWeather (forecasts) retorna mínima, máxima e descrição por dia.
5. **Busca por cidade:** O usuário informa cidade e Estado; Mapbox (geocoding) retorna coordenadas; em seguida repete-se o fluxo AccuWeather (passos 2–4).

### Funções principais (Aula37 / Aula43)

- `pegarCoordenadas()` — Coordenadas via Geoplugin (IP).
- `pegarCodigoLocal(lat, long)` — Código e nome do local no AccuWeather.
- `pegarTempoAgora(codigoLocal, nomeLocal)` — Condição e temperatura atuais.
- `pegarPrevisao5Dias(codigoLocal)` — Previsão diária (mín, máx, descrição).
- `pesquisarLocal(local)` — (Aula43) Coordenadas via Mapbox a partir de texto (cidade/Estado).

## 📚 Conteúdos Abordados

- Requisições HTTP em Python (`requests`)
- Leitura e manipulação de JSON
- Tratamento de erros e códigos de status
- Organização em funções reutilizáveis
- Uso de APIs REST (geolocalização e clima)
- Entrada do usuário e fluxo interativo (previsão 5 dias, busca por cidade)

## 📄 Licença

Este projeto está licenciado sob a MIT License — veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📖 Referências

- Curso Python 3 — Udemy (Prof. Ivan Lourenço Gomes)
- [Geoplugin](http://www.geoplugin.net/) — API de geolocalização por IP
- [AccuWeather API](https://developer.accuweather.com/) — Clima e previsão
- [Mapbox Geocoding](https://docs.mapbox.com/api/search/geocoding/) — Busca por endereço/local

---

<img width="auto" src="https://github.com/henriqueotogami/App-Previsao-Tempo-Python/blob/master/Weather-App.png?raw=true">

<br>

<img width="auto" src="https://github.com/henriqueotogami/App-Previsao-Tempo-Python/blob/master/App-Weather.gif?raw=true">

---

### Hashtags

#Python #PrevisaoTempo #WeatherApp #API #AccuWeather #Mapbox #Geoplugin #REST #OpenSource #GitHub #Udemy #Programming #Geolocalizacao #Clima

---

<div align="center">
<a href="https://ko-fi.com/seu_usuario" target="_blank"><img src="https://cdn.ko-fi.com/cdn/kofi3.png?v=3" alt="Buy Me a Coffee at ko-fi.com" width="200"></a>
</div>

---

**Desenvolvido por Henrique Matheus Alves Pereira**
