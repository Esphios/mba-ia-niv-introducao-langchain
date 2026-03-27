# Introdução ao LangChain

Este curso é destinado a quem quer ter o primeiro contato com o LangChain. A seguir, apresentamos as instruções para configurar o ambiente utilizando `venv`, instalar as dependências necessárias e ter uma visão geral dos principais tópicos abordados.

## Configuração do Ambiente

Para configurar o ambiente e instalar as dependências do projeto, siga os passos abaixo:

1. **Criar e ativar um ambiente virtual (`venv`):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar as dependências:**

   **Opção A - A partir do `requirements.txt`:**
   ```bash
   pip install -r requirements.txt
   ```

   **Opção B - Instalação direta dos pacotes principais:**
   ```bash
   pip install langchain langchain-openai langchain-google-genai langchain-community langchain-text-splitters langchain-postgres psycopg[binary] python-dotenv beautifulsoup4 pypdf && pip freeze > requirements.txt
   ```
   Este comando também instalará todas as dependências automaticamente e gerará o arquivo `requirements.txt`.

3. **Configurar as variáveis de ambiente:**

   - Duplique o arquivo `.env.example` e renomeie para `.env`
   - Abra o arquivo `.env` e substitua os valores pelas suas chaves de API reais, obtidas conforme as instruções abaixo

## Principais Tópicos Abordados

### Fundamentos Básicos
- **Introdução ao LangChain:** conceitos básicos e primeira integração com modelos de linguagem
- **Integração com OpenAI:** como usar o ChatOpenAI para interações básicas
- **Integração com Google Gemini:** configuração e uso do modelo Gemini via Google GenAI
- **Templates de Prompt:** criação de templates simples e avançados para prompts
- **Chat Prompts:** implementação de sistemas de conversação com templates estruturados

### Chains e Processamento Avançado
- **LCEL (LangChain Expression Language):** sintaxe de pipe (`|`) para conectar componentes
- **Chains Básicas:** criação de pipelines simples de pergunta e resposta
- **Chains Complexas:** pipelines multietapas com tradução e sumarização
- **Runnables Customizados:** decorador `@chain` e `RunnableLambda` para funções personalizadas
- **Text Splitters:** divisão de textos longos em chunks para processamento
- **Summarization Chains:** técnicas `stuff` e `map_reduce` para sumarização de documentos
- **Structured Output:** extração de dados estruturados usando modelos Pydantic

### Agentes e Tools
- **Custom Tools:** criação de ferramentas personalizadas com o decorador `@tool`
- **ReAct Agents:** implementação de agentes que raciocinam e agem
- **Agent Executors:** orquestração de agentes com múltiplas ferramentas
- **Prompt Hub:** uso de prompts predefinidos da comunidade LangChain

### Gerenciamento de Memória
- **Chat History:** implementação de histórico de conversação persistente
- **Message Memory:** armazenamento e recuperação de mensagens em sessões
- **Memory Trimming:** técnicas de janela deslizante para gerenciar contexto limitado
- **Session Management:** gerenciamento de múltiplas sessões de conversa

### Document Loaders e RAG
- **Web Loaders:** carregamento de conteúdo de páginas web
- **PDF Loaders:** processamento e extração de texto de documentos PDF
- **Document Chunking:** estratégias de divisão de documentos para processamento eficiente
- **RAG Foundations:** conceitos básicos para Retrieval-Augmented Generation

## Requisitos para Execução dos Códigos

Para executar os códigos fornecidos no curso, é necessário criar chaves de API para os serviços da OpenAI e do Google Gemini. Abaixo, fornecemos instruções detalhadas para a criação dessas chaves.

### Criando uma API Key na OpenAI

1. **Acesse o site da OpenAI:**

   [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

2. **Faça login ou crie uma conta:**

   - Se já possuir uma conta, clique em "Log in" e insira suas credenciais.
   - Caso contrário, clique em "Sign up" para criar uma nova conta.

3. **Navegue até a seção de API Keys:**

   - Após o login, clique em "API Keys" no menu lateral esquerdo.

4. **Crie uma nova API Key:**

   - Clique no botão "Create new secret key".
   - Dê um nome para a chave que a identifique facilmente.
   - Clique em "Create secret key".

5. **Copie e armazene sua API Key:**

   - A chave será exibida uma única vez. Copie-a e cole no arquivo `.env` na variável `OPENAI_API_KEY`.

Para mais detalhes, consulte o tutorial completo: [Como Gerar uma API Key na OpenAI?](https://hub.asimov.academy/tutorial/como-gerar-uma-api-key-na-openai/)

### Criando uma API Key no Google Gemini

1. **Acesse o Google AI Studio:**

   [https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR)

2. **Faça login com sua conta Google:**

   - Utilize sua conta Google para acessar o AI Studio.

3. **Navegue até a seção de chaves de API:**

   - No painel de controle, clique em "API Keys" ou "Chaves de API".

4. **Crie uma nova API Key:**

   - Clique em "Create API Key" ou "Criar chave de API".
   - Dê um nome para a chave que a identifique facilmente.
   - A chave será gerada e exibida na tela.

5. **Copie e armazene sua API Key:**

   - Copie a chave gerada e cole no arquivo `.env` na variável `GOOGLE_API_KEY`.

Para mais informações, consulte a documentação oficial: [Como usar chaves da API Gemini](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-BR)

**Nota:** Certifique-se de não compartilhar suas chaves de API publicamente e de armazená-las em locais seguros, pois elas concedem acesso aos serviços correspondentes.
