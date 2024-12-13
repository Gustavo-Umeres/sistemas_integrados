// Configuración global de Chart.js
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

// Función para generar colores aleatorios
function generarColoresAleatorios(cantidad) {
  const colores = [];
  for (let i = 0; i < cantidad; i++) {
    colores.push(`rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 0.2)`);
  }
  return colores;
}

// Función para generar datos aleatorios
function generarDatos(cantidad) {
  return Array.from({ length: cantidad }, () => Math.floor(Math.random() * 15000));
}

// Función para crear y actualizar el gráfico
function crearGrafico(ctx, tipo = 'line', datos = generarDatos(6), colores = generarColoresAleatorios(1)) {
  const myChart = new Chart(ctx, {
    type: tipo,
    data: {
      labels: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
      datasets: [{
        label: 'Mis Datos',
        data: datos,
        backgroundColor: colores[0],
        borderColor: colores[0].replace('0.2', '1'),
        borderWidth: 1
      }]
    },
    options: {
      scales: {
        xAxes: [{ gridLines: { display: false } }],
        yAxes: [{
          ticks: { min: 0, max: Math.max(...datos) * 1.2, maxTicksLimit: 5 }
        }]
      },
      legend: { display: false }
    }
  });
  return myChart;
}

// Obtener el contexto del canvas
const ctx = document.getElementById('myChart').getContext('2d');

// Crear el gráfico inicial
let myChart = crearGrafico(ctx);

// Agregar evento de clic a una tarjeta (ejemplo)
document.getElementById('card-body').addEventListener('click', () => {
  // Actualizar el gráfico con nuevos datos y tipo aleatorio
  const nuevoTipo = ['line', 'bar', 'radar'][Math.floor(Math.random() * 3)];
  myChart.destroy();
  myChart = crearGrafico(ctx, nuevoTipo);
});