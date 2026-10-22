# Guia de longevidade para programadores · HowToLiveLonger

**Ajudar todas as pessoas a viver mais, com saúde e felicidade.**

[**Ler online →**](https://geekan.github.io/HowToLiveLonger/#lang=pt&view=table) · [Contribuir](../../CONTRIBUTING.md)

[English](../../README.md) · [简体中文](zh-CN.md) · [Español](es.md) · [Français](fr.md) · [Deutsch](de.md) · [Português](pt.md) · [日本語](ja.md) · [العربية](ar.md)

[![Guia de longevidade para programadores](../../assets/cover-social-v3.png)](https://geekan.github.io/HowToLiveLonger/#lang=pt&view=table)

Explore estudos sobre alimentação, movimento, sono e hábitos do dia a dia e encontre mudanças que se encaixem na sua vida.

- **Oito idiomas:** chinês, inglês, espanhol, francês, alemão, português, japonês e árabe.
- **Fácil de explorar:** pesquise temas, filtre por categoria ou nível de evidência e ordene clicando nos títulos das colunas. No celular, leia os cartões.
- **Pesquisas que você pode consultar:** 61 registros com resultados em linguagem clara, sugestões para o dia a dia e fontes originais. Passe o cursor sobre termos como HR, ou toque neles, para ver a explicação.
- **Guarde uma cópia:** exporte CSV, o JSON completo ou um cartão para compartilhar. Baixe o repositório e abra `index.html` para consultar o conteúdo sem conexão.

## Desenvolvimento local

Basta ter Python 3.10 ou mais recente. Não é preciso instalar pacotes adicionais nem um backend.

```sh
git clone https://github.com/geekan/HowToLiveLonger.git
cd HowToLiveLonger
python3 scripts/build.py
python3 scripts/validate.py --check-build
python3 -m http.server 8000
```

Acesse <http://localhost:8000>. Depois de alterar o modelo ou os dados, gere e valide o site novamente e inclua o `index.html` gerado no commit.

## Estrutura do projeto

| Diretório | Conteúdo |
| --- | --- |
| [`src/`](../../src/) | Código da página: `index.template.html` |
| [`data/`](../../data/) | Registros dos estudos, fontes e glossário |
| [`locales/`](../../locales/) | Traduções da interface e dos estudos; cartões de leitura em `readers/` |
| [`scripts/`](../../scripts/) | `build.py` gera o site; `validate.py` verifica os dados e a reprodução da versão gerada |
| [`assets/`](../../assets/) | Logotipo, ilustrações e arquivos de origem |
| [`docs/`](../../docs/) | Artigos originais, registros de revisões anteriores e READMEs traduzidos |
| [`index.html`](../../index.html) | Site gerado em um único arquivo para GitHub Pages e leitura sem conexão |

## Hospedagem e atualizações

O GitHub Pages publica a raiz de `main`. O arquivo `.nojekyll` permite servir diretamente os arquivos estáticos já gerados. Gere e valide o site localmente e depois envie as alterações. Não são necessários arquivos de workflow próprios.

Contribuições para os estudos, as traduções e a experiência de leitura são bem-vindas. Consulte o [guia de contribuição](../../CONTRIBUTING.md).

Criado por [geekan e os colaboradores](https://github.com/geekan/HowToLiveLonger/graphs/contributors) sob a [Unlicense](../../LICENSE). Os artigos e outros materiais vinculados mantêm seus próprios termos de uso.
