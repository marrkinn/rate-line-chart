# Rate Line Chart

Este é um guia simples para rodar a aplicação Django com Docker Compose, usando o Redis como cache. Certifique-se de ter o Docker e o Docker Compose instalados no seu sistema antes de começar.

## Configuração do Docker Compose

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/marrkinn/rate-line-chart.git
   cd rate-line-chart

2. **Construa as imagens e inicie os contêineres:**
    ```bash
    docker-compose up --build

3. **Acesse a aplicação através do link:**
    ```bash
    http://localhost:8000/