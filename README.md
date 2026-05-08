# AutoCyberSecNews-SK

Plne automatický Cyber News pipeline pre tvoj osobný LinkedIn (slovenčina).

**Funkcie:**
- Denný ingest z 20+ zdrojov
- Deduplikácia + impact scoring (zero-day, CVSS, EU relevance)
- Streamlit dashboard – 1 klik 2× týždenne (utorok + štvrtok)
- AI generuje perfektné slovenské LinkedIn posty (actionable)
- Presné plánovanie: 8:45, 11:15, 13:22, 15:56 (CEST)

**Náklady:** 0 € (okrem tvojho Hetzner VPS)

## Rýchle spustenie
```bash
git clone https://github.com/tvoj-username/AutoCyberSecNews-SK.git /opt/autocybersec
cd /opt/autocybersec
cp .env.example .env
docker compose up -d --build
