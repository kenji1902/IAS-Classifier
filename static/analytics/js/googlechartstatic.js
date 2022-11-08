let $chartdata = null
$(document).ready(function () {

    $('#plantreport-list a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
    })

    google.charts.load('current', {
        packages: ['bar', 'corechart', 'table']
    });
    $chartdata = $("#chartdata")
    
    
    google.charts.setOnLoadCallback(() => plantCountChart(data.plants,'#PlantCount' ));
    google.charts.setOnLoadCallback(() => IASCountChart(data.ias, '#IASCount'));
    google.charts.setOnLoadCallback(() => plantAreaCountChart(data.locationMapping,'#PlantAreaCount'));
    plantneighborChart(data.neighborMapping,'#neighbors')
    
});



function plantneighborChart(data, area){
    // Set Data
    
    for (const [key, value] of Object.entries(data)) {

        $(area).append(
            `
            <div class="card  shadow1">
                <div class="card-header">
                    ${key} Estimated Affected Neighbor Per Plant
                </div>
                <div class="card-body chartWrapper">
                    <div id="${area.substring(1)}EstimatedAffectedNeighbor_${key.replace(/\s+/g, '')}" class="chart"></div>
                </div>
            </div>

            `
        );
        $chartdata.append(
            `

                <div style="margin-top:1rem; font-weight:bold;">
                    ${key} Estimated Affected Neighbor Per Plant
                </div>

                <div id="${area.substring(1)}-tableEstimatedAffectedNeighbor_${key.replace(/\s+/g, '')}" class="chart"></div>


            `
        )
        const chart = ()=>{
            let dataTable = new google.visualization.DataTable()
            console.log(key.replace(/\s+/g, ''));
            dataTable.addColumn('string', 'Neighbor')
            dataTable.addColumn('number', 'Counts')
            for (const [neighbor, count] of Object.entries(value)) {
                dataTable.addRow([neighbor, count])
            }
            let option = options
            option.legend= {
                position: 'top', alignment: 'left', textStyle: {color:'#607d8b', fontName: 'Roboto', fontSize: '12'} 
            }
            // option.isStacked = true
            option.width = "100%"
            if(Object.keys(value).length > 9){
                option.width = Object.keys(value).length * 60 
            }
            let chart = new google.visualization.AreaChart($(`#${area.substring(1)}EstimatedAffectedNeighbor_${key.replace(/\s+/g, '')}`)[0]);
            chart.draw(dataTable, option);

            
            let table = new google.visualization.Table($(`#${area.substring(1)}-tableEstimatedAffectedNeighbor_${key.replace(/\s+/g, '')}`)[0]);
            table.draw(dataTable,tableoptions);

        }
        
        google.charts.setOnLoadCallback(chart);
    }
}

function plantAreaCountChart(data,area){
    // Set Data
    
    let dataTable = new google.visualization.DataTable();
    dataTable.addColumn('string', 'Region')
    plant_List.forEach(element => {
        dataTable.addColumn('number', element)
    });
        
    
    for (const [key, value] of Object.entries(data)) {
        let row = [key]
        plant_List.forEach(plant => {
            if(value[plant])
                row.push(value[plant])
            else
                row.push(0)
        });
        
        console.log(row)
        dataTable.addRow(row)
        row = []
    
    }
    console.log(dataTable)
    // Option
    let option = options
    // option.isStacked = true
    option.legend= {
        position: 'top', alignment: 'left', textStyle: {color:'#607d8b', fontName: 'Roboto', fontSize: '12'} 
    }
    if(Object.keys(data).length > 2){
        option.width = `${Object.keys(data).length * 200}`
    }
    option.bar= {groupWidth: "100px" }
    //  Draw
    var chart = new google.visualization.ColumnChart($(area)[0]);
    chart.draw(dataTable, option);
    let table = new google.visualization.Table($(`#table${area.substring(1)}`)[0]);
    table.draw(dataTable,tableoptions);
}
function plantCountChart(data,area) {
    // Set Data
    let dataTable = new google.visualization.DataTable();
    dataTable.addColumn('string', 'Plants')
    dataTable.addColumn('number', 'Counts')
    for (const [key, value] of Object.entries(data)) {
        dataTable.addRow([key, value])
    }

    // Draw
    var chart = new google.visualization.PieChart($(area)[0]);
    chart.draw(dataTable, options);
    let table = new google.visualization.Table($(`#table${area.substring(1)}`)[0]);
    table.draw(dataTable,tableoptions);
}
function IASCountChart(data,area) {
    // Set Data
    let dataTable = new google.visualization.DataTable();
    dataTable.addColumn('string', 'Category')
    dataTable.addColumn('number', 'Counts')
    for (const [key, value] of Object.entries(data)) {
        dataTable.addRow([key, value])
    }

    // Draw
    var chart = new google.visualization.PieChart($(area)[0]);
    chart.draw(dataTable, options);
    let table = new google.visualization.Table($(`#table${area.substring(1)}`)[0]);
    table.draw(dataTable,tableoptions);
}

function Init(callback){
    $.get(`/api/iasdata/`,
        function (data, textStatus, jqXHR) {
            $.get("/api/plantinformation/",
                function (plants, textStatus, jqXHR) {
                    callback(data,plants) 
                },
                "json"
            );
        },
        "json"
    );
}