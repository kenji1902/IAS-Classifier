

// function getCoordinates() {
//     return new Promise(function(resolve, reject) {
//       navigator.geolocation.getCurrentPosition(resolve, reject);
//     });
// }
// async function getAddress() {
//     const position = await getCoordinates(); 
//     return {
//         lat: position.coords.latitude,
//         lng: position.coords.longitude
//     }  
// }



function getAddress(callback) {
    navigator.geolocation.getCurrentPosition(
        function (position) {
            var returnValue = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            }
            var serializeCookie = returnValue;
            callback(serializeCookie);
        }
    )
}