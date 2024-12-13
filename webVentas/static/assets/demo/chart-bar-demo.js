// Función para generar datos aleatorios
function generarDatos(cantidad) {
  return Array.from({ length: cantidad }, () => Math.floor(Math.random() * 15000));
}

// Configuración inicial para el gráfico de áreas
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
          data: generarDatos(6)
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

// Configuración inicial para el gráfico de barras
var ctxBar = document.getElementById("myBarChart").getContext('2d');
var myBarChart = new Chart(ctxBar, {
  type: 'bar',
  data: {
      labels: ["January", "February", "March", "April", "May", "June"],
      datasets: [{
          label: "Revenue",
          backgroundColor: "rgba(2,117,216,1)",
          data: generarDatos(6)
      }]
  },
  options: {
      scales: {
          xAxes: [{
              gridLines: { display: false },
              ticks: { maxTicksLimit: 6 }
          }],
          yAxes: [{
              ticks: { min: 0, max: 15000, maxTicksLimit: 5 }
          }]
      },
      legend: { display: false }
  }
});

// Función para actualizar las gráficas
function actualizarGraficas() {
  // Generar nuevos datos para ambas gráficas
  var nuevosDatosArea = generarDatos(6);
  var nuevosDatosBar = generarDatos(6);

  // Actualizar gráfico de área
  myLineChart.data.datasets[0].data = nuevosDatosArea;
  myLineChart.update();

  // Actualizar gráfico de barras
  myBarChart.data.datasets[0].data = nuevosDatosBar;
  myBarChart.update();
}

// Agregar eventos de clic a las tarjetas
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('click', () => {
      actualizarGraficas();
  });
});
