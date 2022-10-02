let Stream;
$(document).ready(function () {
    $video = $('#video');
    $cameraContent = $('.camera-content');
    $('#camera').click(function(){ 
        
        $cameraContent.addClass('slide');
        vidOn($video);
        
    });
    $('#arrow-right-btn').click(function(){
        $cameraContent.removeClass('slide');
        vidOff($video);
    });
    listDevices();
    
});
function dataURItoBlob(dataURI) {
    // convert base64/URLEncoded data component to raw binary data held in a string
    var byteString;
    if (dataURI.split(',')[0].indexOf('base64') >= 0)
        byteString = atob(dataURI.split(',')[1]);
    else
        byteString = unescape(dataURI.split(',')[1]);

    // separate out the mime component
    var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

    // write the bytes of the string to a typed array
    var ia = new Uint8Array(byteString.length);
    for (var i = 0; i < byteString.length; i++) {
        ia[i] = byteString.charCodeAt(i);
    }

    return new Blob([ia], {type:mimeString});
}

function uploadFileCam(blob){
    
    showSpinner();
    $('#dropAreaSpinner').removeClass('hidden')
    previewFileCam(blob)
     
}
function previewFileCam(blob){
    let $rawImages = $("#raw");
    let fileName = `shutter-${Date.now()}.cam`

    $rawImages.append(
        `
        <div  class="file-content">
            <img src="${URL.createObjectURL(blob)}" alt="" class="image">
            <span class="image-name">${fileName}</span>
            <span id="${rawImageID}" class="close-image material-symbols-outlined">
                close
            </span>
        </div>                    
        `
    );
    $(`#${rawImageID}`).click(function (e) { 
        e.preventDefault();
        $(this).parent().remove();
        delete imageLoaded[$(this).attr('id')];
        delete coords[$(this).attr('id')];
        if(isEmpty($rawImages)){
            slideUp($('#filter'),200);
            slideUp($('#raw'),500);
            slideUp($('#remove_blur'),150);

        }
    });
    // blob = dataURItoBlob(blob)
    const newFile = new File([blob], fileName, {type:'image/jpeg'});
    console.log(newFile)
    // EXIF.getData(newFile, function () {
    //     const make = EXIF.getAllTags(newFile);
    //     console.log("All data", make);
    //     console.log(this.exifdata.GPSLongitude)
    // });
    
    imageLoaded.push(newFile);
    getAddress(function (cookie) {
        coords.push(JSON.stringify(cookie))
        if($('#raw.hidden').length){
            slideDown($('#raw'),500);
            slideDown($('#filter'),500);
            slideDown($('#remove_blur'),1000);
        }

        hideSpinner()
        $('#dropAreaSpinner').addClass('hidden')
    });  
    rawImageID++;
    
}

let videoConstraints = {
    facingMode : 'environment',
}
function vidOn($video){
    // Get access to the camera!
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ 
            audio: false,
            video: videoConstraints
        }).then(function(stream) {
            //video.src = window.URL.createObjectURL(stream);
            Stream = stream;
            $video.get(0).srcObject = stream;
            $video.get(0).play();

            $('#shutter').click(e => {

                // let stream_settings = stream.getVideoTracks()[0].getSettings();
                // var canvas = document.createElement('canvas');
                // let square = Math.min(stream_settings.width,stream_settings.height)
                // canvas.width = square;
                // canvas.height = square;
                // var ctx = canvas.getContext('2d');
                
                // ctx.drawImage( $video.get(0), 0, 0, canvas.width, canvas.height);
                
                const track = stream.getVideoTracks()[0];
                let imageCapture = new ImageCapture(track);
                imageCapture.takePhoto().then((blob) => {
                    uploadFileCam(blob)
                });


                //convert to desired file format
                // var dataURI = canvas.toDataURL('image/jpeg');
                // uploadFileCam(dataURI)
            })
           
        }).catch(function(err){
            $('.camera-content').hide()
            showAlert('#alert','<strong>Hi there!</strong> You should enable Camera Permission <br> go to home and search "Allow Camera".')

        });
    }
}
function vidOff($video) {

    $video.get(0).pause();
    $video.attr('src','');
    Stream.getTracks()[0].stop();
    $('#shutter').off('click')
}

function listDevices(){
    let $menu = $('#devices .dropdown-menu');
    
    navigator.mediaDevices.enumerateDevices().then(devices => {
        devices.forEach(device => {
            if(device.deviceId != ''){
                $menu.append(
                    `
                    <li>
                        <div id="${device.deviceId}" class="dropdown-item">
                            ${device.label}
                        </div>
                    </li>
                    `
                );


                $(`#${device.deviceId}`).click(function (e) { 
                    e.preventDefault();
                    videoConstraints = {
                        deviceId:device.deviceId,
                        facingMode:'environment',
                        width: 256,
                        height: 256
                    }
                    console.log(videoConstraints)
                    vidOff($('#video'))
                    vidOn($('#video'))
                });
            }

        });
    });
    
}

