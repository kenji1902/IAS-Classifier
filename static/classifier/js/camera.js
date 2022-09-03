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
        }).catch(function(err){
            alert(err);
        });
    }
}
function vidOff($video) {

    $video.get(0).pause();
    $video.attr('src','');
    Stream.getTracks()[0].stop();
  }