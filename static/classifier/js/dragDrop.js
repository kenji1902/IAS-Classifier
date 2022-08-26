
let imageLoaded = new Array();
let imageID = 0;
console.log(typeof( images));

function preventDefaults(events) {
    events.preventDefault();
    events.stopProagration();
}
function previewFile(files){

    let reader = new FileReader();
    reader.readAsDataURL(files);
    reader.onloadend = function() {
        // let img = document.createElement('img');
        // img.src = reader.result;
        $loadedImages.append(
            `
            <div id="${imageID}" class="file-content">
                <img src="${reader.result}" alt="" class="image">
                <span class="image-name">${files['name']}</span>
                <span class="close-image material-symbols-outlined">
                    close
                </span>
            </div>                    
            `
        );
        $(`#${imageID}`).click(function (e) { 
            e.preventDefault();
            $(this).remove();
            delete imageLoaded[$(this).attr('id')];
            console.log($(this).attr('id'));
            console.log(imageLoaded);
        });
        imageLoaded.push(files);
        imageID++;
    }

}

function uploadFile(files){
    for (let i = 0; i < files.length; i++){
        previewFile(files[i]);
    }
    console.log(imageLoaded);
    
}  
function uploadFormData(form_data) {
    $('#progress-percent').removeClass('hidden');
    $.ajax({
        xhr: function () {
            var xhr = new window.XMLHttpRequest();
            xhr.upload.addEventListener("progress", function (evt) {
                if (evt.lengthComputable) {
                    var percentComplete = evt.loaded / evt.total;
                    console.log(percentComplete);
                    $('#progress-percent .progress').text(
                        percentComplete * 100 + '%'
                        
                    );
                    if (percentComplete === 1) {
                        $('#progress-percent').addClass('hidden');
                    }
                }
            }, false);

            return xhr;
        },
        url: "/classifier/post/",
        dataType: 'json',
        method: "POST",
        data: form_data,
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": getCookie("csrftoken"),  // don't forget to include the 'getCookie' function
        },
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            console.log(data);
        }
    });
}

$(document).ready(function () {
    console.log(getCookie("csrftoken"));
    $dropArea = $(".drop-area");
    $loadedImages = $(".loaded-images");
    $progressPercent = $('#progress-percent .progress');
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        $dropArea.on(eventName,preventDefaults,false);
        console.log(eventName);
        
    });

    ['dragenter', 'dragover'].forEach(eventName => {
        $dropArea.on(eventName, function(){
            $(this).addClass('highlight');
            return false;
        });
    });

    ['dragleave', 'drop'].forEach(eventName => {
        $dropArea.on(eventName, function(){
            $(this).removeClass('highlight');
            return false
        });
    })

    $dropArea.on('drop',function(e){
        e.preventDefault();
        let files = e.originalEvent.dataTransfer.files;
        uploadFile(files);   
        return false;
    });

    $('#upload').click(function(e){
        e.preventDefault();

        let formData = new FormData();;
        for (let i = 0; i < imageLoaded.length; i++){
            formData.append('files[]',imageLoaded[i]);
        } 
        uploadFormData(formData);
    });

    $('#file').click(function(){ $('#fileElem').trigger('click'); });
    // $('#camera').click(function(){ $('#cameraElem').trigger('click'); });
    
});