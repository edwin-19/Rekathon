var chart;
var secondChart;
var thirdChart;

/**
 * Request data from the server, add it to the graph and set a timeout
 * to request again
 */
 function requestTemp() {
    $.ajax({
        url: '/getTemp?temperature=10.20',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20
            // add the point
            chart.series[0].addPoint(point, true, shift);
            // call it again after one second
            setTimeout(requestTemp, 1000);
        },
        cache: false
    });
}

function requestHumidity() {
    $.ajax({
        url: '/getHumidity?humidity=20.20',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            secondChart.series[0].addPoint(point, true, shift);
            // call it again after one second
            setTimeout(requestHumidity, 1000);
        },
        cache: false
    });
}

function requestSoil() {
    $.ajax({
        url: '/getSoil?soil=30.20',
        success: function(point) {
            var series = chart.series[0],
                shift = series.data.length > 20; // shift if the series is
                                                 // longer than 20

            // add the point
            thirdChart.series[0].addPoint(point, true, shift);
            // call it again after one second
            setTimeout(requestSoil, 1000);
        },
        cache: false
    });
}


$(document).ready(function() {
    chart = new Highcharts.Chart({
        chart: {
            renderTo: 'data-container',
            defaultSeriesType: 'spline',
            events: {
                load: requestTemp
            }
        },
        title: {
            text: 'Live random data'
        },
        xAxis: {
            type: 'datetime',
            tickPixelInterval: 150,
            maxZoom: 20 * 1000
        },
        yAxis: {
            minPadding: 0.2,
            maxPadding: 0.2,
            title: {
                text: 'Value',
                margin: 80
            }
        },
        series: [{
            name: 'Temperature',
            data: []
        }]
    });


    Highcharts.setOptions({
        global: {
            useUTC: false
        }
    });

    secondChart = Highcharts.chart('chartB', {
     chart: {
        renderTo: 'data-container',
        defaultSeriesType: 'spline',
        events: {
            load: requestHumidity
        }
    },
    title: {
        text: 'Live random data'
    },
    xAxis: {
        type: 'datetime',
        tickPixelInterval: 150,
        maxZoom: 20 * 1000
    },
    yAxis: {
        minPadding: 0.2,
        maxPadding: 0.2,
        title: {
            text: 'Value',
            margin: 80
        }
    },
    series: [{
        name: 'Humidity',
        data: []
    }]
});

    thirdChart = Highcharts.chart('chartC', {
     chart: {
        renderTo: 'data-container',
        defaultSeriesType: 'spline',
        events: {
            load: requestSoil
        }
    },
    title: {
        text: 'Live random data'
    },
    xAxis: {
        type: 'datetime',
        tickPixelInterval: 150,
        maxZoom: 20 * 1000
    },
    yAxis: {
        minPadding: 0.2,
        maxPadding: 0.2,
        title: {
            text: 'Value',
            margin: 80
        }
    },
    series: [{
        name: 'Soil Moisture',
        data: []
    }]
});
});