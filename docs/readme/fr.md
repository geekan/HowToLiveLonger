# Guide de longévité pour les développeurs · HowToLiveLonger

**Aider chacun à vivre plus longtemps, en meilleure santé et plus heureux.**

[**Lire en ligne →**](https://geekan.github.io/HowToLiveLonger/#lang=fr&view=table) · [Contribuer](../../CONTRIBUTING.md)

[English](../../README.md) · [简体中文](zh-CN.md) · [Español](es.md) · [Français](fr.md) · [Deutsch](de.md) · [Português](pt.md) · [日本語](ja.md) · [العربية](ar.md)

[![Guide de longévité pour les développeurs](../../assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/#lang=fr&view=table)

Découvrez les études sur l’alimentation, le mouvement, le sommeil et les habitudes quotidiennes, et trouvez des changements adaptés à votre vie.

- **Huit langues :** chinois, anglais, espagnol, français, allemand, portugais, japonais et arabe.
- **Une exploration simple :** recherchez un sujet, filtrez par catégorie ou niveau de preuve et triez en cliquant sur les en-têtes de colonne. Sur téléphone, parcourez les fiches.
- **Des études à consulter :** 61 fiches présentent les résultats en langage courant, des pistes pour le quotidien et les sources originales. Survolez un terme comme HR, ou touchez-le, pour en lire l’explication.
- **Gardez une copie :** exportez un CSV, le JSON complet ou une fiche à partager. Téléchargez le dépôt et ouvrez `index.html` pour consulter le site hors ligne.

## Développement local

Python 3.10 ou une version ultérieure suffit. Aucun paquet supplémentaire ni serveur applicatif n’est nécessaire.

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

Ouvrez <http://localhost:8000>. Après avoir modifié le modèle ou les données, générez et validez à nouveau le site, puis incluez le fichier `index.html` généré dans le commit.

## Organisation du projet

| Dossier | Rôle |
| --- | --- |
| [`src/`](../../src/) | Source de la page : `index.template.html` |
| [`data/`](../../data/) | Études, sources et glossaire |
| [`locales/`](../../locales/) | Traductions de l’interface et des études ; fiches de lecture dans `readers/` |
| [`scripts/`](../../scripts/) | `build.py` génère le site ; `validate.py` vérifie les données et la reproductibilité |
| [`assets/`](../../assets/) | Logo, illustrations et fichiers sources |
| [`docs/`](../../docs/) | Articles d’origine, anciens comptes rendus de vérification et README traduits |
| [`index.html`](../../index.html) | Site généré en un seul fichier pour GitHub Pages et la consultation hors ligne |

## Hébergement et mises à jour

GitHub Pages publie la racine de `main`. Le fichier `.nojekyll` permet de servir directement les fichiers statiques déjà générés. Générez et validez le site en local, puis poussez les modifications. Aucun fichier de workflow personnalisé n’est nécessaire.

Les contributions aux études, aux traductions et au confort de lecture sont les bienvenues. Consultez le [guide de contribution](../../CONTRIBUTING.md).

Créé par [geekan et les contributeurs](https://github.com/geekan/HowToLiveLonger/graphs/contributors) sous licence [Unlicense](../../LICENSE). Les articles et autres documents liés conservent leurs propres conditions d’utilisation.
