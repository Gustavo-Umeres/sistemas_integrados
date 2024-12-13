// Configuración del gráfico de área
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Función para generar datos aleatorios
function generarDatos(cantidad) {
    return Array.from({ length: cantidad }, () => Math.floor(Math.random() * 15000));
}

// Inicialización del gráfico de área
var ctxArea = document.getElementById("myAreaChart").getContext('2d');
var myLineChart = new Chart(ctxArea, {
    type: 'line',  // Tipo inicial
    data: {
        labels: ["January", "February", "March", "April", "May", "June"],
        datasets: [{
            label: "Sessions",
            backgroundColor: "rgba(2,117,216,0.2)",  // Fondo inicial
            borderColor: "rgba(2,117,216,1)",  // Color del borde
            pointBackgroundColor: "rgba(2,117,216,1)",  // Color de los puntos
            data: generarDatos(6)  // Datos iniciales
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

// Función para actualizar el gráfico de área con nuevos datos aleatorios y diseño
function actualizarGraficoArea() {
    // Generar nuevos datos aleatorios
    var nuevosDatosArea = generarDatos(6);

    // Cambiar diseño del gráfico (tipo, colores)
    var coloresAleatorios = [
        "rgba(255, 99, 132, 0.2)",
        "rgba(54, 162, 235, 0.2)",
        "rgba(255, 159, 64, 0.2)",
        "rgba(75, 192, 192, 0.2)",
        "rgba(153, 102, 255, 0.2)",
        "rgba(255, 159, 64, 0.2)"
    ];
    var nuevoColor = coloresAleatorios[Math.floor(Math.random() * coloresAleatorios.length)];

    // Actualizar los datos y el diseño del gráfico
    myLineChart.data.datasets[0].data = nuevosDatosArea;
    myLineChart.data.datasets[0].backgroundColor = nuevoColor;
    myLineChart.data.datasets[0].borderColor = nuevoColor.replace("0.2", "1");
    myLineChart.data.datasets[0].pointBackgroundColor = nuevoColor.replace("0.2", "1");
    myLineChart.options.scales.yAxes[0].ticks.max = Math.floor(Math.random() * 20000);  // Cambiar el valor máximo del eje Y aleatoriamente

    // Redibujar el gráfico
    myLineChart.update();

    // Log para depuración
    console.log("Gráfico actualizado con datos:", nuevosDatosArea);
}

// Agregar eventos de clic a las tarjetas
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('click', () => {
        console.log("Se hizo clic en una tarjeta.");  // Para depuración
        actualizarGraficoArea();
    });
});
