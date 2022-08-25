var filesDone = 0;
var filestoDo = 0;
function preventDefaults(events) {
    events.preventDefault();
    events.stopProagration();
}
function initializeProgress($progressPercent, fileSize){
    $progressPercent.text("");
    filesDone = 0;
    filestoDo = fileSize;
}
function previewFile(files){
    let reader = new FileReader();
        reader.readAsDataURL(files);
        reader.onloadend = function() {
            // let img = document.createElement('img');
            // img.src = reader.result;
            $loadedImages.append(
                `
                <div class="file-content">
                    <img src="${reader.result}" alt="" class="image">
                    <span class="image-name">${files['name']}</span>
                </div>                    
                `
            );
        }
}
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
      const cookies = document.cookie.split(";");
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + "=")) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
function handleFiles(files) {
    ([...files]).forEach(uploadFile);
    ([...files]).forEach(previewFile);
    uploadFile(files);
}
function uploadFile(files){
    let formData = new FormData();
    for (let i = 0; i < files.length; i++){
        formData.append('files[]',files[i]);
    } 

    uploadFormData(formData);
    return formData;
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
        let formData = uploadFile(files);
        formData.forEach(previewFile);
        return false;
    });
    

    $('#file').click(function(){ $('#fileElem').trigger('click'); });
    $('#camera').click(function(){ $('#cameraElem').trigger('click'); });
});