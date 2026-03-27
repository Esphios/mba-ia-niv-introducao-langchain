# AGENTS.md

## Visão Geral

Este repositório é um material introdutório de LangChain organizado por módulos
numerados. O foco é pedagógico: cada script demonstra um conceito isolado ou uma
composição pequena.

## Tecnologias Principais

| Categoria | Tecnologia | Evidência | Uso |
| --- | --- | --- | --- |
| Runtime | Python | `requirements.txt` | execução dos exemplos |
| Framework LLM | LangChain | `requirements.txt`, módulos `1-5` | chains, agentes e memória |
| Provedores | OpenAI e Google GenAI | `.env.example`, exemplos com `ChatOpenAI` | modelos de linguagem |
| Vetor store | PostgreSQL + pgvector | `docker-compose.yaml`, `5-loaders-e-banco-de-dados-vetoriais/` | exemplos de RAG |
| Parsing | BeautifulSoup, PyPDF | `requirements.txt`, loaders do módulo 5 | web/PDF loaders |

## Estrutura Principal

- `1-fundamentos/`: exemplos básicos de modelos, prompts e chat prompts.
- `2-chains-e-processamento/`: chains, pipelines, runnables e sumarização.
- `3-agentes-e-tools/`: tools customizadas, agentes ReAct e Prompt Hub.
- `4-gerenciamento-de-memoria/`: histórico de conversa e trimming de contexto.
- `5-loaders-e-banco-de-dados-vetoriais/`: loaders, PDF, ingestão e busca com pgvector.
- `docker-compose.yaml`: serviços auxiliares para exemplos com banco vetorial.
- `requirements.txt`: dependências compartilhadas do repositório.

## Setup e Comandos

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
docker compose up -d
python .\1-fundamentos\1-hello-world.py
python .\3-agentes-e-tools\1-agente-react-e-tools.py
python .\5-loaders-e-banco-de-dados-vetoriais\3-ingestion-pgvector.py
```

## Configuração

- O repositório usa `python-dotenv` e espera `.env` baseado em `.env.example`.
- Exemplos com modelos usam `OPENAI_API_KEY` e, quando aplicável, `GOOGLE_API_KEY`.
- Os exemplos do módulo 5 também usam `PGVECTOR_URL` e `PGVECTOR_COLLECTION`.
- O README também documenta instalação manual dos pacotes principais como alternativa ao `requirements.txt`.

## Diretrizes de Trabalho

- Trate cada arquivo numerado como um exemplo executável relativamente independente.
- Prefira mudanças localizadas no módulo correspondente ao conceito ensinado.
- Preserve a numeração e os nomes dos arquivos; eles fazem parte da sequência didática.
- Não edite `venv/`; é ambiente local e não faz parte da fonte do projeto.
- Se adicionar variáveis de ambiente, atualize `.env.example`.
- Quando corrigir ou evoluir um exemplo, preserve o objetivo pedagógico do arquivo.
- Não introduza abstrações compartilhadas entre módulos sem necessidade clara.

## Tópicos Cobertos

O material do README explicita estes grupos de conteúdo:

- fundamentos básicos de integração com LLMs;
- LCEL, chains e pipelines multietapas;
- agentes, tools e Prompt Hub;
- gerenciamento de memória;
- loaders, RAG e banco vetorial.

## Peculiaridades do Projeto

- O repositório é um curso, não uma aplicação única; não tente centralizar tudo em uma arquitetura compartilhada.
- Há mistura de exemplos simples e exemplos com infraestrutura local como pgvector.
- O histórico de commits é curto e informal, compatível com material didático.
