
$(document).ready(function () {

    $('#plantreport-list a').on('click', function (e) {
        e.preventDefault()
        $(this).tab('show')
      })



    google.charts.load('current', {
        packages: ['bar', 'corechart', 'table']
      });

    plants = {};
    ias = {}
    locationMapping = {};
    plant_List = []
    neighborMapping = {}
    Init(function (data,plantList){
        plantList.forEach(element => {
            plant_List.push(element.scientificName)
        });
        data.forEach(element => {
            let scientificName = element.scientificName.scientificName
            let region  = JSON.parse(element.reverseGeoLoc).address.region
            let neighbors = JSON.parse(element.seedlingDispersionAffectedAreas)
            // Plant Count
            if(!plants[scientificName])
                plants[scientificName] = 1
            else
                plants[scientificName] += 1;
            
            // IAS Count
            if(!ias[element.scientificName.invasiveType])
                ias[element.scientificName.invasiveType] = 1
            else
                ias[element.scientificName.invasiveType] += 1;

            // Plant per Region
            if(!locationMapping[region])
                locationMapping[region] = {}
            if(!locationMapping[region][scientificName])
                locationMapping[region][scientificName] = 1
            else
                locationMapping[region][scientificName] += 1

            // if(neighborMapping)
            for (const [key, value] of Object.entries(neighbors)) {
                let neighbor = value.tags.name
                if(!neighborMapping[region])
                    neighborMapping[region] = {}
                if(!neighborMapping[region][neighbor])
                    neighborMapping[region][neighbor] = 1
                else
                    neighborMapping[region][neighbor] += 1
            }


        });
        google.charts.setOnLoadCallback(() => plantCountChart(plants,'#PlantCount' ));
        google.charts.setOnLoadCallback(() => IASCountChart(ias, '#IASCount'));
        google.charts.setOnLoadCallback(() => plantAreaCountChart(locationMapping,'#PlantAreaCount'));
        plantneighborChart(neighborMapping,'#neighbors')
        // google.charts.setOnLoadCallback(plantneighborChart(neighborMapping));

    });
    
    
    
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
    console.log("Object Count: ",Object.keys(locationMapping).length)
    if(Object.keys(locationMapping).length > 2){
        option.width = `${Object.keys(locationMapping).length * 200}`
    }
    option.bar= {groupWidth: "100px" }
    //  Draw
    var chart = new google.visualization.ColumnChart($(area)[0]);
    chart.draw(dataTable, option);
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