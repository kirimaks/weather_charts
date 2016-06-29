$(function () {
    Highcharts.setOptions({                                            // This is for all plots, change Date axis to local timezone
        global : {
            useUTC : false
        }
    });

    $('#container').highcharts({
        chart: {
            type: 'spline'
        },
        title: {
            text: 'Black Sea Temperature'
        },
        subtitle: {
            text: 'Irregular time data in Highcharts JS'
        },
        xAxis: {
            type: 'datetime',
        },
        yAxis: {
            title: {
                text: 'Tempecature (C)'
            },
            min: 15
        },

        plotOptions: {
            spline: {
                marker: {
                    enabled: true
                }
            }
        },

        series: [{
            name: 'worldseatemp',
            data: data1
        }, {
            name: 'yandex',
            data: data2
        }, {
            name: 'sochicamera',
            data: data3
        }]
    });

});

