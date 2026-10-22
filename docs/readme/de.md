# Leitfaden zur Langlebigkeit für Programmierer · HowToLiveLonger

**Allen Menschen helfen, länger, gesünder und glücklicher zu leben.**

[**Online lesen →**](https://geekan.github.io/HowToLiveLonger/#lang=de&view=table) · [Mitwirken](../../CONTRIBUTING.md)

[English](../../README.md) · [简体中文](zh-CN.md) · [Español](es.md) · [Français](fr.md) · [Deutsch](de.md) · [Português](pt.md) · [日本語](ja.md) · [العربية](ar.md)

[![Leitfaden zur Langlebigkeit für Programmierer](../../assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/#lang=de&view=table)

Entdecken Sie Forschung zu Ernährung, Bewegung, Schlaf und Alltagsgewohnheiten und finden Sie Veränderungen, die zu Ihrem Leben passen.

- **Acht Sprachen:** Chinesisch, Englisch, Spanisch, Französisch, Deutsch, Portugiesisch, Japanisch und Arabisch.
- **Einfach erkunden:** Themen suchen, nach Kategorie oder Evidenzniveau filtern und durch Klick auf die Spaltenüberschrift sortieren. Auf dem Smartphone erscheinen die Einträge als Karten.
- **Nachvollziehbare Forschung:** 61 Einträge mit verständlichen Ergebnissen, Anregungen für den Alltag und Originalquellen. Begriffe wie HR werden beim Darüberfahren oder Antippen erklärt.
- **Eine Kopie behalten:** CSV, die vollständigen JSON-Daten oder eine Karte zum Teilen herunterladen. Das Repository lässt sich auch herunterladen und durch Öffnen von `index.html` offline lesen.

## Lokal entwickeln

Python 3.10 oder neuer genügt. Zusätzliche Pakete oder ein Backend sind nicht erforderlich.

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

Öffnen Sie <http://localhost:8000>. Nach Änderungen an Vorlage oder Daten die Seite neu erstellen und prüfen; die erzeugte `index.html` gehört ebenfalls in den Commit.

## Projektstruktur

| Verzeichnis | Inhalt |
| --- | --- |
| [`src/`](../../src/) | Seitenvorlage: `index.template.html` |
| [`data/`](../../data/) | Studieneinträge, Quellen und Glossar |
| [`locales/`](../../locales/) | Übersetzungen von Oberfläche und Studien; lesefreundliche Karten unter `readers/` |
| [`scripts/`](../../scripts/) | `build.py` erstellt die Website; `validate.py` prüft Daten und Reproduzierbarkeit |
| [`assets/`](../../assets/) | Logo, Illustrationen und Quelldateien |
| [`docs/`](../../docs/) | Originalartikel, frühere Prüfberichte und übersetzte READMEs |
| [`index.html`](../../index.html) | Erzeugte Website in einer Datei für GitHub Pages und die Offline-Nutzung |

## Hosting und Aktualisierungen

GitHub Pages veröffentlicht das Stammverzeichnis von `main`. Mit `.nojekyll` werden die bereits erzeugten statischen Dateien direkt bereitgestellt. Die Website lokal erstellen und prüfen, dann die Änderungen pushen. Eigene Workflow-Dateien sind nicht nötig.

Beiträge zu Forschung, Übersetzungen und Lesbarkeit sind willkommen. Weitere Informationen stehen im [Leitfaden für Beiträge](../../CONTRIBUTING.md).

Erstellt von [geekan und den Mitwirkenden](https://github.com/geekan/HowToLiveLonger/graphs/contributors) unter der [Unlicense](../../LICENSE). Für verlinkte Studien und andere Materialien gelten deren eigene Nutzungsbedingungen.
