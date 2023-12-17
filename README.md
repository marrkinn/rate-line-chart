# Rate Line Chart

## Desenvolvimento de um Sistema de Monitoramento de Cotações
Esse é um sistema que armazene as cotações do dólar em relação ao real, euro e iene e as exiba de maneira visual em um gráfico, no qual foi implementado uma solução robusta e eficiente.

## Configuração do Docker Compose

Este é um guia simples para rodar a aplicação Django com Docker Compose, usando o Redis como cache. Certifique-se de ter o Docker e o Docker Compose instalados no seu sistema antes de começar.

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

## Objetivos do Sistema

# Armazenamento de Cotações:

Implementar um mecanismo de armazenamento confiável para as cotações do dólar em relação ao real, euro e iene.
Utilizar uma estrutura de banco de dados eficiente para garantir o acesso rápido e seguro às informações.

# Exibição em Gráfico:

Desenvolver uma interface gráfica intuitiva para a visualização das cotações ao longo do tempo.
Incorporar ferramentas de interatividade no gráfico para uma análise mais dinâmica.

# Atualizações em Tempo Real:

Integrar uma funcionalidade de atualização automática das cotações para garantir que os dados exibidos estejam sempre sincronizados com as últimas informações de mercado.

# Personalização e Análise:

Oferecer recursos de personalização para os usuários, permitindo a escolha de períodos específicos para análise detalhada. Nesta atividade travamos em 5 dias úteis o intervalo máximo que o usuário pode selecionar


## Tecnologias Propostas
Linguagem de Programação: Python (Django para o backend)
Cache: Redis confiagurado para 15 minutos de cache para cada cotação
Frontend: JavaScript (Algumas bibliotecas em JavaScript foram necessárias) e HTML
Gráficos: Highcharts.js
Docker e docker-compose
Utilização de algumas bibliotecas no Python para pequenas funcionalidades