// Recupera os dados JSON do campo input hidden e formatando conforme a nossa necessidade
var jsonDataInput = $("#jsonDataInput").val();
jsonDataInput = jsonDataInput.replace(/'/g, '"');
var jsonData = JSON.parse(jsonDataInput);
console.log("jsonData", jsonData);

// Pegando a moeda selecionada
var moeda = $("#moeda").val();
console.log("moeda", moeda);

// Seria da cotação a ser exibidada
var serie = [];
var categories = [];
jsonData.forEach(element => {
    categories.push(element.date)
    serie.push(parseFloat(element.rates[moeda].toFixed(3)))
});

const chart = Highcharts.chart('container', {

    title: {
        text: '',
        align: 'left'
    },

    subtitle: {
        text: 'Fonte: <a href="https://www.vatcomply.com/" target="_blank" style="color: #007bff">VATcomply</a>.',
        align: 'left'
    },

    yAxis: {
        title: {
            text: 'Valor de 1 USD em ' + moeda
        }
    },

    xAxis: {
        categories: categories,
    },

    series: [{
        name: 'Cotação USD - ' + moeda,
        data: serie
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
        }]
    }

});

// Animação de carregamento
let isLoading = false;
document.getElementById('button').addEventListener('click', e => {
    if (!isLoading) {
        chart.showLoading("");
        e.target.innerHTML = 'loading...';
    } else {
        chart.hideLoading("");
    }
    isLoading = !isLoading;
});

// Ativar botão somente quando todos os campos estiverem preenchidos
var campo1 = document.getElementById('id_dia_inicio');
var campo2 = document.getElementById('id_dia_fim');
var campo3 = document.getElementById('id_moeda');
var botao = document.getElementById('button');

// Ouvinte de evento de entrada a cada campo
campo1.addEventListener('input', habilitarBotao);
campo2.addEventListener('input', habilitarBotao);
campo3.addEventListener('input', habilitarBotao);

// Função para verificar se todos os campos estão preenchidos
function habilitarBotao() {
    if (campo1.value !== '' && campo2.value !== '' && campo3.value !== '') {
        botao.removeAttribute('disabled');
    } else {
        botao.setAttribute('disabled', 'true');
    }
}