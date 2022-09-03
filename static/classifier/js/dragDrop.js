
let imageLoaded = new Array();
let rawImageID = 0;


function preventDefaults(events) {
    events.preventDefault();
    events.stopProagration();
}
function previewFile(files){
    $rawImages = $("#raw");
    let reader = new FileReader();
    reader.readAsDataURL(files);
    reader.onloadend = function() {
        // let img = document.createElement('img');
        // img.src = reader.result;
        $rawImages.append(
            `
            <div  class="file-content">
                <img src="${reader.result}" alt="" class="image">
                <span class="image-name">${files['name']}</span>
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
        });
        imageLoaded.push(files);
        rawImageID++;
    }

}

function uploadFile(files){
    $('#raw').removeClass('hidden')
    $('#filter').removeClass('hidden')

    for (let i = 0; i < files.length; i++){
        previewFile(files[i]);
    }
    
}

function progress () {
    var xhr = new window.XMLHttpRequest();
    xhr.upload.addEventListener("progress", function (evt) {
        if (evt.lengthComputable) {
            var percentComplete = evt.loaded / evt.total;
            $('#progress-percent .progress').text(
                percentComplete * 100 + '%'
                
            );
            if (percentComplete === 1) {
                $('#progress-percent').addClass('hidden');
            }
        }
    }, false);

    return xhr;
}
ppImageID = 0
function uploadFormData(form_data) {
    $('#progress-percent').removeClass('hidden');
    $.ajax({
        xhr: progress,
        url: "/classifier/filter/",
        dataType: 'json',
        method: "POST",
        data: form_data,
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": Cookies.get("csrftoken"), 
        },
        contentType: false,
        cache: false,
        processData: false,
        success: function (data) {
            data['images'].forEach(files => {
                $.ajax({
                    type: "GET",
                    headers: {
                        "X-Requested-With": "XMLHttpRequest",
                        "X-CSRFToken": Cookies.get("csrftoken"), 
                    },
                    url: `${window.location.origin}/blobstorage/${files}`,

                    success: function (response) {
                       filter(response)
                    }
                });
                
            });
        }
    });
}
let preprocessedImages = []
function filter(response){
    $image = $(response).find('.image');
    $ppImages = $("#preprocessed");
    let altName = $image['prevObject'][0]['alt'].split('.').at(-2)
    let extension = $image['prevObject'][0]['alt'].split('.').at(-1)
    $ppImages.append(
        `
        <div class="file-content">
            ${response}
            <span class="image-name">${altName}</span>
            <span id="${altName}"  class="close-image material-symbols-outlined">
                close
            </span>
        </div>                    
        `
    );
    
    $(`#${altName}`).click(function (e) { 
        e.preventDefault();
        $(this).parent().remove();
        var index = preprocessedImages.indexOf(altName+ '.' +extension);
        if (index !== -1) { 
            preprocessedImages.splice(index, 1);
        }
        console.log(preprocessedImages)
    });    
    preprocessedImages.push(altName + '.' +extension)
}

$(document).ready(function () {
    console.log(getCookie("csrftoken"));
    $dropArea = $(".drop-area");
    
    $progressPercent = $('#progress-percent .progress');
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
        $dropArea.on(eventName,preventDefaults,false);
        
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

    $('#filter').click(function(e){
        $('#preprocessed').removeClass('hidden')
        $('#classify').removeClass('hidden')
        let formData = new FormData();;
        for (let i = 0; i < imageLoaded.length; i++){
            formData.append('files[]',imageLoaded[i]);
        } 
        imageLoaded = [];
        uploadFormData(formData);

    });
    $('#classify').click(function(e){
        console.log(preprocessedImages)
        $.ajax({
            xhr: progress,
            url: "/classifier/classify/",
            dataType: 'json',
            method: "POST",
            data: {'images':preprocessedImages},
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": Cookies.get("csrftoken"), 
            },
            success: function (data) {
                console.log(data)
            }
        });
    });
    $('#file').click(function(){ $('#fileElem').trigger('click'); });
    // $('#camera').click(function(){ $('#cameraElem').trigger('click'); });
    
});