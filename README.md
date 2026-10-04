# Sistema de Recomendação de Smartphones

Sistema de recomendação de smartphones desenvolvido para recomendar dispositivos Samsung de acordo com as preferências, necessidades e orçamento do usuário.

O projeto utiliza Inteligência Artificial para interpretar diretamente as respostas fornecidas pelo usuário em um formulário e auxiliar no processo de recomendação. Os critérios objetivos de filtragem são tratados pela aplicação e pelo banco de dados.

## Objetivo

Facilitar a escolha de um smartphone Samsung por meio de recomendações personalizadas.

O sistema considera informações como:

* Uso principal do dispositivo
* Prioridades do usuário
* Perfil tecnológico
* Orçamento disponível
* Principais necessidades ou dificuldades
* Especificações dos smartphones disponíveis

## Funcionamento

O fluxo principal da aplicação é:

```text
Usuário
   ↓
Formulário de preferências
   ↓
Agente de IA
   ↓
Interpretação das preferências
   ↓
Filtros de produtos
   ↓
Produtos compatíveis
   ↓
Recomendações
```

O formulário preenchido pelo usuário é enviado diretamente ao agente de Inteligência Artificial. Não existe uma etapa intermediária de criação ou armazenamento de uma persona.

O agente interpreta as respostas e auxilia na definição dos critérios utilizados para a recomendação.

Os critérios objetivos, como preço, armazenamento, RAM, bateria e câmera, são tratados pela aplicação por meio de filtros no banco de dados.

Essa separação mantém os critérios técnicos previsíveis e reduz a possibilidade de a IA gerar informações que não existem nos produtos cadastrados.

## Tecnologias

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* PydanticAI
* PostgreSQL
* Supabase

### Inteligência Artificial

* PydanticAI
* Google Gemini

### Banco de Dados

O projeto utiliza PostgreSQL hospedado no Supabase.

### Usuários

Os principais dados relacionados aos usuários incluem:

* `user_id`
* `main_usage`
* `priorities`
* `tech_profile`
* `budget`
* `pain_point`

### Produtos

Os produtos possuem informações como:

* `name`
* `rating`
* `price`
* `camera`
* `display_type`
* `display_size`
* `battery`
* `storage`
* `ram`
* `weight`
* `processor`
* `image_url`

## Estrutura do Projeto

```text
SistemaRecomendacao/
│
├── Agente/
│   └── ...
│
├── Produtos/
│   ├── Model/
│   ├── Repository/
│   ├── Service/
│   └── ...
│
├── Usuarios/
│   ├── Model/
│   ├── Repository/
│   ├── Service/
│   └── ...
│
├── database/
│   └── ...
│
├── .env
├── requirements.txt
└── main.py
```

## Recomendação de Produtos

Os produtos são filtrados de acordo com os requisitos identificados a partir das respostas do usuário.

Por exemplo:

```text
Preço máximo: R$ 2.500
Câmera mínima: 50 MP
Bateria mínima: 4.500 mAh
Armazenamento mínimo: 128 GB
RAM mínima: 6 GB
```

Após a aplicação dos filtros, os produtos compatíveis podem ser selecionados de forma aleatória para variar as recomendações apresentadas.

## Agente de Inteligência Artificial

O agente recebe diretamente os dados preenchidos no formulário.

Exemplo de entrada:

```json
{
  "main_usage": "Fotografia e redes sociais",
  "priorities": [
    "Câmera",
    "Bateria"
  ],
  "tech_profile": "Intermediário",
  "budget": 2500,
  "pain_point": "Meu celular atual trava"
}
```

A partir dessas informações, o agente interpreta as necessidades do usuário e auxilia na definição dos critérios de recomendação.

A aplicação utiliza esses critérios para consultar os produtos disponíveis no banco de dados e apresentar as opções mais adequadas ao perfil informado.

## Configuração

Clone o projeto:

```bash
git clone <URL_DO_REPOSITORIO>
cd SistemaRecomendacao
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente:

### Linux/macOS

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente:

```env
DATABASE_URL=...
GOOGLE_API_KEY=...
```

Execute a aplicação:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```text
http://localhost:8000
```

## Samsung Innovation Campus

Este projeto foi desenvolvido com base em um exercício proposto no **Samsung Innovation Campus**, tendo como objetivo aplicar conceitos de desenvolvimento de software, banco de dados e Inteligência Artificial na construção de um sistema de recomendação de produtos.

A aplicação foi desenvolvida e expandida a partir da proposta original do exercício, incorporando uma arquitetura de backend, persistência de dados e integração com um agente de Inteligência Artificial.
