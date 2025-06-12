// RadarChart.js
import {
    Chart as ChartJS,
    Filler,
    LineElement,
    PointElement,
    RadialLinearScale,
    Tooltip
} from 'chart.js';
import { Radar } from 'react-chartjs-2';
  
  ChartJS.register(
    RadialLinearScale,
    PointElement,
    LineElement,
    Filler,
    Tooltip
  );
  
  function RadarChart({ labels, dataPoints }) {
    const data = {
      labels: labels,
      datasets: [
        {
          data: dataPoints,
          backgroundColor: 'rgb(77, 6, 43)',
          borderColor: 'rgb(109, 10, 61)',
          borderWidth: 4,
          pointBackgroundColor: 'rgb(120, 11, 67)'
        }
      ]
    };
  
    const options = {
      scales: {
        r: {
          angleLines: {
            color: 'rgb(31, 2, 2)'  // Lines from center out
          },
          grid: {
            color: 'rgba(172, 24, 103, 0.3)',  // Circular grid lines
            lineWidth: 2
          },
          pointLabels: {
            color: 'rgb(189, 159, 113)',
            font: {
              weight: 'bold',
              size: 14
            },
            padding: 10
          },
          ticks: {
            display: false,       // Hides the tick text (like 90, 80, etc.)
            backdropColor: 'transparent', // Removes gray background boxes
            showLabelBackdrop: false,     // Removes backdrop completely
            color: 'transparent',         // Extra: hides just in case
            stepSize: 20
          }
        }
      },
      
      plugins: {
        tooltip: {
          enabled: false  // This disables the hover boxes
        },
        legend: {
          labels: {
            color: 'white'
          }
        }
      }
    };
  
    return (
      <div style={{ width: '500px', height: '500px', margin: '0 auto' }}>
        <Radar data={data} options={options} />
      </div>
    );
  }
  
  export default RadarChart;