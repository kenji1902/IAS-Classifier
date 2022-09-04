

function getCoordinates() {
    return new Promise(function(resolve, reject) {
      navigator.geolocation.getCurrentPosition(resolve, reject);
    });
}
async function getAddress() {
    const position = await getCoordinates(); 
    return {
        lat: position.coords.latitude,
        lng: position.coords.longitude
    }  
}