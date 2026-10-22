# Guía de longevidad para programadores · HowToLiveLonger

**Ayudar a todas las personas a vivir más tiempo, con salud y felicidad.**

[**Leer en línea →**](https://geekan.github.io/HowToLiveLonger/#lang=es&view=table) · [Contribuir](../../CONTRIBUTING.md)

[English](../../README.md) · [简体中文](zh-CN.md) · [Español](es.md) · [Français](fr.md) · [Deutsch](de.md) · [Português](pt.md) · [日本語](ja.md) · [العربية](ar.md)

[![Guía de longevidad para programadores](../../assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/#lang=es&view=table)

Explora estudios sobre alimentación, movimiento, sueño y hábitos cotidianos, y encuentra cambios que encajen en tu vida.

- **Ocho idiomas:** chino, inglés, español, francés, alemán, portugués, japonés y árabe.
- **Fácil de explorar:** busca temas, filtra por categoría o nivel de evidencia y ordena pulsando los encabezados de las columnas. En el móvil, lee las fichas.
- **Estudios que puedes consultar:** 61 registros con resultados en lenguaje claro, ideas para el día a día y fuentes originales. Pasa el cursor sobre términos como HR, o tócalos, para ver su explicación.
- **Llévate una copia:** exporta CSV, el JSON completo o una tarjeta para compartir. Descarga el repositorio y abre `index.html` para consultar el contenido sin conexión.

## Desarrollo local

Necesitas Python 3.10 o posterior. No hay paquetes adicionales ni servidor de aplicaciones que instalar.

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

Abre <http://localhost:8000>. Tras modificar la plantilla o los datos, vuelve a generar y validar el sitio e incluye el `index.html` generado en el commit.

## Estructura del proyecto

| Directorio | Contenido |
| --- | --- |
| [`src/`](../../src/) | Código de la página: `index.template.html` |
| [`data/`](../../data/) | Registros de estudios, fuentes y glosario |
| [`locales/`](../../locales/) | Traducciones de la interfaz y de los estudios; fichas para lectores en `readers/` |
| [`scripts/`](../../scripts/) | `build.py` genera el sitio; `validate.py` comprueba los datos y la reproducibilidad |
| [`assets/`](../../assets/) | Logotipo, ilustraciones y archivos originales |
| [`docs/`](../../docs/) | Artículos originales, revisiones históricas y README traducidos |
| [`index.html`](../../index.html) | Sitio generado en un solo archivo para GitHub Pages y la lectura sin conexión |

## Alojamiento y actualizaciones

GitHub Pages publica la raíz de `main`. El archivo `.nojekyll` permite servir directamente los archivos estáticos ya generados. Genera y valida el sitio en local y después sube los cambios. No hacen falta archivos de workflow propios.

Puedes aportar estudios, mejorar las traducciones o facilitar la lectura. Consulta la [guía de contribución](../../CONTRIBUTING.md).

Creado por [geekan y sus colaboradores](https://github.com/geekan/HowToLiveLonger/graphs/contributors) con la licencia [Unlicense](../../LICENSE). Los artículos y demás materiales enlazados conservan sus propias condiciones de uso.
