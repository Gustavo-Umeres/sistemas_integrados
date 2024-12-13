Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

function generarDatos(cantidad) {
    return Array.from({ length: cantidad }, () => Math.floor(Math.random() * 15000));
}

var ctxArea = document.getElementById("myAreaChart").getContext('2d');
var myLineChart = new Chart(ctxArea, {
    type: 'line',
    data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [{
            label: "Sessions",
            backgroundColor: "rgba(2,117,216,0.2)",
            borderColor: "rgba(2,117,216,1)",
            pointBackgroundColor: "rgba(2,117,216,1)",
            data: generarDatos(6) // Datos iniciales
        }]
    },
    options: {
        scales: {
            xAxes: [{ gridLines: { display: false } }],
            yAxes: [{
                ticks: { min: 0, max: 15000, maxTicksLimit: 5 }
            }]
        },
        legend: { display: false }
    }
});

function actualizarGraficoArea() {
    var nuevosDatosArea = generarDatos(6);

    myLineChart.data.datasets[0].data = nuevosDatosArea;

    // Redibujar el gráfico
    myLineChart.update();
    console.log("Gráfico actualizado con datos:", nuevosDatosArea); // Para depuración
}

// Agregar eventos de clic a las tarjetas
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('click', () => {
          actualizarGraficoArea();
      });
  });
});