
$(document).ready(function () {
    google.charts.load('current',{packages:['corechart']});
    google.charts.load('current', {packages:['bar']});

    plants = {};
    locationMapping = {};
    plant_List = []
    Init(function (data,plantList){
        plantList.forEach(element => {
            plant_List.push(element.scientificName)
        });
        data.forEach(element => {
            let scientificName = element.scientificName.scientificName
            let region  = JSON.parse(element.reverseGeoLoc).address.region
            if(!plants[scientificName])
                plants[scientificName] = 1
            else
                plants[scientificName] += 1;

            if(!locationMapping[region])
                locationMapping[region] = {}
            else if(!locationMapping[region][scientificName])
                locationMapping[region][scientificName] = 1
            else
                locationMapping[region][scientificName] += 1
        });
        google.charts.setOnLoadCallback(plantCountChart(plants));
        google.charts.setOnLoadCallback(plantAreaCountChart(locationMapping,plant_List));
    });
    
    
    
});
function plantAreaCountChart(data,plantList){
    // Set Data
    
    let dataTable = new google.visualization.DataTable();
    dataTable.addColumn('string', 'Region')
    plantList.forEach(element => {
        dataTable.addColumn('number', element)
    });
        
    
    for (const [key, value] of Object.entries(data)) {
        let row = [key]
        plantList.forEach(plant => {
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
    option.bar= {groupWidth: "80" }

    //  Draw
    var chart = new google.visualization.ColumnChart($('#PlantAreaCount')[0]);
    chart.draw(dataTable, option);
}
function plantCountChart(data) {
    // Set Data
    let dataTable = new google.visualization.DataTable();
    dataTable.addColumn('string', 'Plants')
    dataTable.addColumn('number', 'Counts')
    for (const [key, value] of Object.entries(data)) {
        dataTable.addRow([key, value])
    }

    // Draw
    var chart = new google.visualization.PieChart($('#PlantCount')[0]);
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