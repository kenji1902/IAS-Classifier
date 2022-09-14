function initMap(){

  $.get(`/api/iasdata/`,
    function (data, textStatus, jqXHR) {
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

    const map = new google.maps.Map(document.getElementById("map"), {
      zoom: 6,
      center: { lat: 12.61969527323028, lng:  121.25304181469903 }
    });
    const infoWindow = new google.maps.InfoWindow({
      content: "",
      disableAutoPan: true,
    });
    

    const iconUrl = '/blobstorage/icon/'
    let icons = {};
    plants.forEach(element => {
      icons[element['scientificName']] = {icon : `${iconUrl}${element['icon']}`}
    });

    let features = []
    data.forEach(element => {
      features.push({
        position: new google.maps.LatLng(element['latitude'], element['longtitude']),
        type: element['scientificName']['scientificName']
        }
      );
    });

    for (let i = 0; i < features.length; i++) {
      new google.maps.Marker({
        position: features[i].position,
        map: map,
        icon:icons[features[i].type].icon,

      });
    
      // markers can only be keyboard focusable when they have click listeners
      // open info window when marker is clicked
      // marker.addListener("click", () => {
      //   // infoWindow.setContent(label);
      //   infoWindow.open(map, marker);
      // });
      // return marker;
    }
    // Add a marker clusterer to manage the markers.
    // new markerClusterer.MarkerClusterer({ map, markers });
  }
  
  const locations = [
    {name: 'plantName', lat:  15.468469351628467 , lng:  120.28624499371662 },
    {name: 'plantName', lat:  16.334865017382548 , lng:  121.15965803085416 },
    {name: 'plantName', lat:  15.383745058306776 , lng:  121.14867170334296 },
    {name: 'plantName', lat:  15.139971222639247 , lng:  121.2255759959211 },
    {name: 'plantName', lat:  15.071027520340268 , lng:  121.45628887365555 },
    {name: 'plantName', lat:  15.187688338888115 , lng:  121.14317853958738 },
    {name: 'plantName', lat:  14.076872234641746 , lng:  120.83006820551923 },
    {name: 'plantName', lat:  14.210038438564679 , lng:  120.84105453303039 },
    {name: 'plantName', lat:  14.092856292557963 , lng:  120.81358871425249 },
    {name: 'plantName', lat:  14.050229653747575 , lng:  120.92345198936412 },
    {name: 'plantName', lat:  14.050229653747575 , lng:  121.45628887365555 },
    {name: 'plantName', lat:  13.959621717214787 , lng:  121.39586407234415 },
    {name: 'plantName', lat:  14.092856292557963 , lng:  121.36290508981067 },
    {name: 'plantName', lat:  13.991605068644557 , lng:  121.318959779766 },
  ];
  
  window.initMap = initMap;