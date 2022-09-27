let totalRecord = 0;
let pages = 0
let limit = 5
let offset = 0
let currPage = 1
let map = null;
let infoWindow = null;
let markers = []

const styles = {
  default: [],
  hide: [
    {
      featureType: "poi.business",
      stylers: [{ visibility: "off" }],
    },
    {
      featureType: "transit",
      elementType: "labels.icon",
      stylers: [{ visibility: "off" }],
    },
  ],
};

function initMap(){

    let $queryBtn = $('#queryBtn')
    let $option = $('#option')
    let $queryContent =  $('#queryContent')
    let $exit = $('#exit')
    
    map = new google.maps.Map(document.getElementById("map"), {
      zoom: 6,
      center: { lat: 12.61969527323028, lng:  121.25304181469903 }
    });
    infoWindow = new google.maps.InfoWindow({
      content: "",
      disableAutoPan: true,
    });
     // Add controls to the map, allowing users to hide/show features.
    map.setOptions({ styles: styles["hide"] });
    // Apply new JSON when the user chooses to hide/show features.
    $("#hide-poi").click( () => {
      map.setOptions({ styles: styles["hide"] });
    });
    $("#show-poi").click( () => {
      map.setOptions({ styles: styles["default"] });
    });
  

  

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
    element.setMap(null)
  });
  markers = []
}
function addMarkers(position,icon,label){
  const marker = new google.maps.Marker({
    position: position,
    map: map,
    icon:icon,

  });
  marker.addListener("mouseover", () => {
      infoWindow.setContent(label);
      infoWindow.open(map, marker);
  });
  marker.addListener("mouseout", () => {
    infoWindow.close();
  });
  markers.push(marker)
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
      icons[element['scientificName']] = {icon : `${iconUrl}${element['icon']}`}
    });

    let features = []
    data['results'].forEach(element => {
      features.push({
        position: new google.maps.LatLng(element['latitude'], element['longtitude']),
        type: element['scientificName']['scientificName'],
        label : `${element['scientificName']['scientificName']} (${element['scientificName']['localName']})`,
        }
      );
    });

    for (let i = 0; i < features.length; i++) {
      addMarkers(features[i].position, icons[features[i].type].icon, features[i].label)

    }
    // Add a marker clusterer to manage the markers.
    // new markerClusterer.MarkerClusterer({ map, markers });
  }
  
  window.initMap = initMap;