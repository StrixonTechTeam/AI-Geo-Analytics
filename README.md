# AI Geo Analytics

AI-powered geographic analytics application.

## Project Structure

```
AI-GEO-ANALYTICS/
├── app/
│   ├── main.py                 # Entry point
│   ├── config.py               # Configuration
│   ├── api/
│   │   └── routes.py           # API endpoints
│   ├── services/
│   │   ├── fetchers.py         # External API calls
│   │   ├── processor.py        # Data normalization + AI scoring
│   │   └── scheduler.py        # Periodic jobs
│   ├── models/
│   │   └── db_models.py        # Database models
│   ├── schemas/
│   │   └── pydantic_models.py  # Request/response validation
│   └── utils/
│       └── helpers.py          # Helper utilities
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── styles.css
├── data/
│   └── app.db                  # SQLite database
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── .github/
│   └── workflows/
│       └── ci-cd.yml           # CI/CD pipeline
└── README.md
```
