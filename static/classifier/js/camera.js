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

function uploadFileCam(files){
    
   
    previewFileCam(files)
    getAddress(function (cookie) {
        coords = JSON.stringify(cookie)
    });   
   
    slideDown($('#raw'),500,200);
    slideDown($('#filter'),500,1000);
}
function previewFileCam(files){
    let $rawImages = $("#raw");
    let fileName = `shutter-${Date.now()}.jpeg`
    $rawImages.append(
        `
        <div  class="file-content">
            <img src="${files}" alt="" class="image">
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
        if(isEmpty($rawImages)){
            slideUp($('#filter'),200,1000);
            slideUp($('#raw'),500,1000);
        }
    });
    let blob = dataURItoBlob(files)
    var file = new File( [blob], fileName, { type: 'image/jpeg' } );
    imageLoaded.push(file);
    rawImageID++;
    
}

function vidOn($video){
    // Get access to the camera!
    if(navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
        navigator.mediaDevices.getUserMedia({ 
            audio: false,
            video: {
                facingMode: 'environment'
            } 
        }).then(function(stream) {
            //video.src = window.URL.createObjectURL(stream);
            Stream = stream;
            $video.get(0).srcObject = stream;
            $video.get(0).play();

            $('#shutter').click(e => {
                let stream_settings = stream.getVideoTracks()[0].getSettings();
                var canvas = document.createElement('canvas');
                canvas.width = stream_settings.width;
                canvas.height = stream_settings.height;
                var ctx = canvas.getContext('2d');
                
                ctx.drawImage( $video.get(0), 0, 0, canvas.width, canvas.height);
        
                //convert to desired file format
                var dataURI = canvas.toDataURL('image/jpeg');
                uploadFileCam(dataURI)
            })
        
        }).catch(function(err){
            alert(err);
        });
    }
}
function vidOff($video) {

    $video.get(0).pause();
    $video.attr('src','');
    Stream.getTracks()[0].stop();
    $('#shutter').off('click')
  }