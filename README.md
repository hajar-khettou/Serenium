# Dossier 3 — Automatisation IHM (Selenium WebDriver)

## Projet : Restful-Booker Platform
**Équipe :** Lyna · Rawane · Hajar · Christina  
**Responsables IHM :** Hajar (Happy Paths) · Christina (Negative Paths)

---

## Architecture du projet

Le projet suit le **Page Object Model (POM)** pour séparer clairement les localisateurs, les actions et les tests.

```
dossier3_selenium/
├── config.py                  # Configuration centralisée (URLs, données de test)
├── requirements.txt           # Dépendances Python
├── README.md                  # Ce fichier
├── pages/                     # Page Objects
│   ├── base_page.py           # Classe parente (méthodes réutilisables)
│   ├── home_page.py           # Page d'accueil (chambres, réservation, contact)
│   ├── login_page.py          # Page de connexion admin
│   └── admin_page.py          # Back-office admin (chambres, messages)
└── tests/                     # Scripts de test
    ├── conftest.py            # Fixtures pytest (setup/teardown navigateur)
    ├── test_happy_path.py     # Scénarios de succès (Hajar)
    └── test_negative_path.py  # Scénarios d'erreurs (Christina)
```

## Prérequis

- **Python 3.10+**
- **Google Chrome** (dernière version)
- **pip** (gestionnaire de paquets Python)

## Installation et configuration

### 1. Cloner ou extraire le dossier

```bash
cd dossier3_selenium
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
```

### 3. Activer l'environnement virtuel

**Windows :**
```bash
venv\Scripts\activate
```

**macOS / Linux :**
```bash
source venv/bin/activate
```

### 4. Installer les dépendances

```bash
pip install -r requirements.txt
```

## Exécution des tests

### Lancer tous les tests

```bash
pytest tests/ -v
```

### Lancer uniquement les Happy Paths

```bash
pytest tests/test_happy_path.py -v
```

### Lancer uniquement les Negative Paths

```bash
pytest tests/test_negative_path.py -v
```

### Lancer un test spécifique

```bash
pytest tests/test_happy_path.py::TestBookingHappyPath::test_valid_booking -v
```

### Générer un rapport HTML (optionnel)

```bash
pip install pytest-html
pytest tests/ -v --html=report.html --self-contained-html
```

## Principes techniques respectés

| Exigence du sujet | Implémentation |
|---|---|
| Page Object Model (POM) | Séparation pages/ (localisateurs + actions) et tests/ (scripts) |
| Attentes explicites uniquement | WebDriverWait + Expected Conditions partout, aucun `time.sleep` |
| Pas de données hardcodées | Toutes les données dans `config.py` |
| Happy Paths | `test_happy_path.py` — réservation, contact, login, CRUD chambres |
| Negative Paths | `test_negative_path.py` — champs vides, email invalide, mauvais login |

## Cas de test automatisés

| ID | Scénario | Type | Fichier |
|---|---|---|---|
| TC-003 | Réservation valide | Happy Path | test_happy_path.py |
| TC-011 | Message contact valide | Happy Path | test_happy_path.py |
| TC-015 | Connexion admin valide | Happy Path | test_happy_path.py |
| TC-019 | Création de chambre | Happy Path | test_happy_path.py |
| TC-021 | Suppression de chambre | Happy Path | test_happy_path.py |
| TC-024 | Accès réservations admin | Happy Path | test_happy_path.py |
| TC-004 | Réservation sans prénom | Negative Path | test_negative_path.py |
| TC-005 | Réservation sans email | Negative Path | test_negative_path.py |
| TC-006 | Réservation email invalide | Negative Path | test_negative_path.py |
| TC-012 | Contact sans nom | Negative Path | test_negative_path.py |
| TC-014 | Contact sans email | Negative Path | test_negative_path.py |
| TC-016 | Login mot de passe incorrect | Negative Path | test_negative_path.py |