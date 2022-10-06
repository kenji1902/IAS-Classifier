let totalRecord = 0;
let pages = 0
let limit = 5
let offset = 0
let currPage = 1
let map = null;
let infoWindow = null;
let markers = []
var markerIcon = null;
$(document).ready(function () {
  initMap()
});


function initMap(){

    let $queryBtn = $('#queryBtn')
    let $option = $('#option')
    let $queryContent =  $('#queryContent')
    let $exit = $('#exit')
    
    markerIcon = L.Icon.extend({
      options: {
          iconSize:     [32, 32],
          iconAnchor:   [16, 32],
          popupAnchor:  [-3, -16]
      }
    });

    map = L.map('map').setView([12.61969527323028, 121.25304181469903],6);
    L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }).addTo(map);

  

    $option.click(function (e) { 
        e.preventDefault();
        $queryContent.addClass('d-flex')
    });
    $exit.click(function (e) { 
        e.preventDefault();
        $queryContent.removeClass('d-flex')
    });
    $('#next').click(function (e) { 
        e.preventDefault();
        let form = $( '#query' ).serialize().split('&');
        let data = {}
        form.forEach(e => {
            let element = e.split('=');
            data[element[0]] = element[1] 
        });

        data['offset'] = parseInt(data['offset']) + 1
        limit = data['limit'];
        currPage = data['offset']
        offset = ( parseInt(data['offset']) - 1) * limit ;
        if(offset >= totalRecord)
            return
        
        getApiData(limit,offset,
            data['requestnum'],
            data['scientificName'],
            data['localName'],
            data['type'],
            data['username']
        )
    });
    $('#prev').click(function (e) { 
        e.preventDefault();
        let form = $( '#query' ).serialize().split('&');
        let data = {}
        form.forEach(e => {
            let element = e.split('=');
            data[element[0]] = element[1] 
        });

        data['offset'] = parseInt(data['offset']) - 1
        limit = data['limit'];
        currPage = data['offset']
        offset = ( parseInt(data['offset']) - 1) * limit ;
        if(offset > totalRecord)
            offset = 0
        if(offset < 0)
            return
        getApiData(limit,offset,
            data['requestnum'],
            data['scientificName'],
            data['localName'],
            data['type'],
            data['username']
        )
    });
    $( "form" ).on( "submit", function( event ) {
        event.preventDefault();
        let form = $( this ).serialize().split('&');
        let data = {}
        form.forEach(e => {
            let element = e.split('=');
            data[element[0]] = element[1]
            
            
        });
        
        limit = data['limit'];
        currPage = data['offset']
        offset = (parseInt(data['offset']) - 1) * limit ;
        if(offset > totalRecord)
            offset = 0
        
        getApiData(limit,offset,
            data['requestnum'],
            data['scientificName'],
            data['localName'],
            data['type'],
            data['username']
        )
    });
    getApiData(limit,offset)

}
function deleteMarkers(){
  markers.forEach(element => {
    map.removeLayer(element)
  });
  markers = []
}




function addMarkers(position,icon,label){
   
    // console.log(inCoord(position,recorded_position))

    const marker = L.marker(position, {icon: icon});
    
    marker.bindPopup(
      `
      <div class="card" style="width: 18rem; position:relative; overflow:hidden">
        <img src="${label.img}" class="card-img-top d-flex justify-content-center" alt="...">
        <div class="card-body">
          <h5 class="card-title" style="font-size:10pt">${label.plantName}</h5>
          <h6 class="card-subtitle mb-2 text-muted">${position[0]}, ${position[1]}</h6>
          <a href="${label.link}" class="btn btn-primary">Link</a>
          <p class="mb-2 text-muted">limited to the owner</p>
        </div>
      </div>
      `
    )
    marker.on('click',function (e) {
        // over
        // console.log(e.latlng)
        this.openPopup();

      });
    marker.addTo(map)
    markers.push(marker)
}

function addCircle(position,label = null,color='blue',fillColor='#F4D400',radius=50){
    const circle = L.circle(position, {
        color: color,
        fillColor: fillColor,
        fillOpacity: 0.1,
        radius: radius
    });
    if(label != null)
      circle.bindPopup(`
        <div class="card" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">${label.name}</h5>
            <h6 class="card-subtitle mb-2 text-muted">${position[0]}, ${position[1]}</h6>
            <p class="card-text">
              place: ${label.place} <br>
              population: ${label.population} <br>
              population date:  ${label["population:date"]} <br>
              source:  ${label['source:population']} <br>
            </p>
          </div>
        </div>

      `)
    circle.addTo(map)
    markers.push(circle)
}

function getApiData(limit,offset,requestnum='',scientificName='',localName='',invasiveType='',username=''){
  $.get(`/api/iasdata/?limit=${limit}&offset=${offset}&requestnum=${requestnum}&scientificName__scientificName=${scientificName}&scientificName__localName=${localName}&scientificName__invasiveType=${invasiveType}&requestnum__username__username=${username}`,
  function (data, textStatus, jqXHR) {
      
      deleteMarkers()
      let $page = $('#page').empty()
      totalRecord = data['count']
        if(totalRecord >= limit){
            pages = Math.ceil( totalRecord/limit );
            for (let i = 0; i < pages; i++) {
                if(currPage == i+1){
                    $page.append(`<option selected value="${i+1}">${i+1}</option>`)
                    continue
                }

                $page.append(`<option value="${i+1}">${i+1}</option>`)
                
            }
        }
        else $page.append(`<option value="${1}">${1}</option>`)


      $.get("/api/plantinformation/",
        function (plants, textStatus, jqXHR) {
          getData(data,plants)
        },
        "json"
      );
    },
    "json"
  );
}



function getData(data,plants) {


    const iconUrl = '/blobstorage/icon/'
    let icons = {};
    plants.forEach(element => {
      icons[element['scientificName']] = 
      {
        icon : new markerIcon({
          iconUrl: `${iconUrl}${element['icon']}`
        }),
        color : element['icon'].split('.')[0]       
      }
    });

    let features = []
    data['results'].forEach(element => {
      features.push({
        position: [element['latitude'], element['longtitude']],
        type: element['scientificName']['scientificName'],
        label : {
          img : `/blobstorage/raw/${element.requestnum.username}/${element.filename}` ,
          plantName: `${element['scientificName']['scientificName']} (${element['scientificName']['localName']})`,
          link: `/classifier/results/${element.requestnum.id}`
        },
        id: element['id'],
        neighbors: JSON.parse(element['seedlingDispersionAffectedAreas'])
        }
      );
    });
    
    let plantLoc = []
    let neighborLoc = []
    for (let i = 0; i < features.length; i++) {
      // console.log(features[i].position)
      addMarkers(features[i].position, icons[features[i].type].icon , features[i].label)
      let marker = features[i].position
      marker.push(icons[features[i].type].color)
      plantLoc.push(marker)

      if(features[i].neighbors != null){
        let neighbors = features[i].neighbors
        for (const [key, value] of Object.entries(neighbors)) {
          neighborLoc.push([value.lat,value.lng,value.tags])
          // console.log(value.tags)
        }
      
      }
        
    }
    // Add a marker clusterer to manage the markers.
    // new markerClusterer.MarkerClusterer({ map, markers });
    plantLoc = getUnique(plantLoc)
    neighborLoc = getUnique(neighborLoc)

    plantLoc.forEach(element => {
      addCircle([
        parseFloat(element[0]),parseFloat(element[1])],null,
        `#${element[2]}`,`#${element[2]}`,2000)
    });
    neighborLoc.forEach(element => {
      addCircle([parseFloat(element[0]),parseFloat(element[1])],element[2])
    });

  }
  
  function getUnique(arr_){
    let temp = ''
    return arr_.sort().filter(r => {
      if (r.join("") != temp) {
        temp = r.join("")
        return true
      }
    })
  }


  // window.initMap = initMap;