# source-tree-exporter

Ein leichtgewichtiges Python-Tool zum Exportieren aller (oder gefilterter) Dateien
eines Projektverzeichnisses in **eine einzelne Textdatei**.  
Ideal für Code-Reviews, Dokumentation, Archivierung oder als Input für LLMs.

---

## Installation (lokal / Entwicklung)

```bash
git clone https://github.com/pepegiallo/source-tree-exporter.git
cd source-tree-exporter
pip install -e .
```

Nach der Installation steht der CLI-Befehl `source-tree-export` global zur Verfügung.

---

## Grundlegende Nutzung

```bash
source-tree-export .
```

Erzeugt im aktuellen Verzeichnis die Datei `_source.txt` mit allen Dateien.

---

## Wichtige Optionen

| Option | Beschreibung |
|------|-------------|
| `-o, --output` | Name oder Pfad der Ausgabedatei |
| `-t, --types` | Erlaubte Dateiendungen (ohne oder mit Punkt) |
| `--ignore-dirs` | Zu ignorierende Ordner (Patterns erlaubt) |
| `--ignore-files` | Zu ignorierende Dateien (Patterns erlaubt) |

---

## Beispielaufrufe nach Projekttyp

### 1. Reines Python-Projekt

```bash
source-tree-export . -o source.txt -t py --ignore-dirs .git .venv __pycache__
```

Exportiert ausschließlich Python-Dateien.

---

### 2. Webanwendung mit Flask

```bash
source-tree-export . -o flask_app_source.txt -t py html css js --ignore-dirs .git .venv node_modules __pycache__ --ignore-files config.py *.log
```

Geeignet für klassische Flask-Projekte mit Templates und Static-Files.

---

### 3. API-Projekt mit FastAPI

```bash
source-tree-export . -o fastapi_source.txt -t py --ignore-dirs .git .venv __pycache__ migrations tests
```

Fokussiert auf die eigentliche API-Logik.

---

### 4. Machine-Learning / Data-Science-Projekt

```bash
source-tree-export . -o ml_project_source.txt -t py ipynb yaml yml --ignore-dirs .git .venv data datasets models __pycache__
```

Typisch für Projekte mit Trainingscode und Konfigurationen.

---

### 5. Full-Stack Webprojekt (Backend + Frontend)

```bash
source-tree-export . -o fullstack_source.txt -t py js ts html css --ignore-dirs .git .venv node_modules dist build __pycache__
```

Ideal zur Gesamtübersicht eines Repositories.

---

## Nutzung als Python-Paket

```python
from source_tree_exporter import export_sources

export_sources(
    folder=".",
    output_name="source.txt",
    allowed_types=["py"],
    ignore_dirs=[".git", ".venv"],
    ignore_files=["README.md"]
)
```

---

## Typische Use-Cases

- Übergabe kompletter Codebasen an LLMs
- Code-Reviews ohne Repository-Zugriff
- Archivierung von Projektständen
- Audits / Dokumentation
- Analyse von Legacy-Code

---

## Lizenz

MIT License
