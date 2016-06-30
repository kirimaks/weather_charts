$(function () {
    Highcharts.setOptions({                                            // This is for all plots, change Date axis to local timezone
        global : {
            useUTC : false
        }
    });

    $('#container').highcharts({
        chart: {
            //type: 'spline'
            type: 'area'

            
        },
        title: {
            text: 'Black Sea Temperature'
        },
        subtitle: {
            text: '30 hours'
        },
        xAxis: {
            type: 'datetime',
        },
        yAxis: {
            title: {
                text: 'Temperature(°C)'
            },
            min: 15
        },

        plotOptions: {
            spline: {
                marker: {
                    //enabled: true
                    enabled: false
                }
            },
            area: {
                //pointStart: 1940,
                marker: {
                    enabled: false,
                    symbol: 'circle',
                    radius: 2,
                    states: {
                        hover: {
                            enabled: true
                        }
                    }
                }
            }
        },

        series: [{
            name: 'worldseatemp',
            data: data1
        }, {
            name: 'yandex',
            data: data2,
            color: "rgba(46, 255, 0, 0.5)"
        }, {
            name: 'sochicamera',
            data: data3,
            color: "rgba(255, 0, 0, 0.2)"
        }]
    });

});

