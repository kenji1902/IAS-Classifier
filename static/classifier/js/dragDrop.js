
let imageLoaded = new Array();
let rawImageID = 0;
let coords = []


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
        uploadFile(e.originalEvent.dataTransfer.files);   
        return false;
    });

    
    
    $('#file').click(function(){ $('#fileElem').trigger('click'); });
    // $('#camera').click(function(){ $('#cameraElem').trigger('click'); });
    
});

function classifyClick(e){
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
            window.location.assign(`/classifier/results/${data['id']}`)
        }
    });
    
}
function isEmpty( el ){
    return !$.trim(el.html())
}
function preventDefaults(events) {
    events.preventDefault();
    events.stopProagration();
}

function previewFile(files){
    let $rawImages = $("#raw");
    let reader = new FileReader();
    reader.readAsDataURL(files); 

    reader.onloadend = function() {
        
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
            if(isEmpty($rawImages)){
                slideUp($('#filter'),200,1000);
                slideUp($('#raw'),500,1000);
            }
        });
        imageLoaded.push(files);
        rawImageID++;
    }

}
function slideUp($element,animate,timeout){
    $element.animate({
        bottom: '4rem',
        opacity: '0'
    },animate);
    setTimeout(() => {
        $element.addClass('hidden');
    }, timeout);
}
function slideDown($element,animate,timeout){
    setTimeout(() => {
        $element.removeClass('hidden').animate({
            bottom: '0rem',
            opacity: '1'
        },animate);
    }, timeout);
}

function showAlert(id){
    $(id).removeClass('hide')
    $('#alert').addClass('show')
    setTimeout(() => {
        $('#alert').removeClass('show')
        $('#alert').addClass('hide')

    }, 5000);
}

let acceptableFileType = ['jpeg','jpg']
function showSpinner(){
    $('#filter').off('click');
    $('#filter .spinnerCont').removeClass('hidden')
    $('#classify').off('click');
    $('#classify .spinnerCont').removeClass('hidden')
}
function hideSpinner(){
    $('#filter').click( clickFilter);
    $('#filter .spinnerCont').addClass('hidden')
    $('#classify').click(classifyClick);
    $('#classify .spinnerCont').addClass('hidden')
}
function uploadFile(files){
    
    // let Files = files.originalEvent.dataTransfer.files;
    showSpinner();
    $('#dropAreaSpinner').removeClass('hidden')
    for (let i = 0; i < files.length; i++){
        let extension = files[i]['name'].split('.').at(-1);
        if(!acceptableFileType.includes(extension)){
            showAlert('#alert')
            $('#dropAreaSpinner').addClass('hidden')
            continue
        }
        previewFile(files[i])
        getAddress(function (cookie) {
            coords = JSON.stringify(cookie)
            if(i == files.length - 1){
                slideDown($('#raw'),500,200);
                slideDown($('#filter'),500,1000);
                hideSpinner()
                $('#dropAreaSpinner').addClass('hidden')
                console.log(coords)
            }
        });   
    }
    
}

function progress () {
    var xhr = new window.XMLHttpRequest();
    xhr.upload.addEventListener("progress", function (evt) {
        if (evt.lengthComputable) {
            var percentComplete = evt.loaded / evt.total;
            $('#progress-percent .progress_').text(
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
            let fileCount = 0
            data['images'].forEach(files => {    
                if(fileCount == data['images'].length - 1)
                    $('#preprocessedSpinner').addClass('hidden')
                filter(files,`${window.location.origin}/blobstorage/filter/${files}`)      
                fileCount++;        
            });
        },
        
    });
}
function clickFilter(e){
    
    
    $('#preprocessedSpinner').removeClass('hidden')
    slideDown($('#preprocessed'),500,200);
    slideDown($('#classify'),500,1000);
    let formData = new FormData();
    console.log(imageLoaded)
    for (let i = 0; i < imageLoaded.length; i++){
        formData.append('files[]',imageLoaded[i]);
        formData.append('coords[]',coords);
    } 
    uploadFormData(formData);
    

}
let preprocessedImages = []
function filter(file,response){
    console.log(response)
    $ppImages = $("#preprocessed");
    let altName = file.split('.').slice(0,-1).join("")
    let extension = file.split('.').at(-1)
    console.log(altName,extension)
    $ppImages.prepend(
        `
        <div class="file-content">
            <img src="${response}" class="image" alt="${altName}">
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
        if(isEmpty($('#preprocessed'))){
            slideUp($('#classify'),200,1000);
            slideUp($('#preprocessed'),500,1000);
        }
    });    
    preprocessedImages.push(altName + '.' +extension)
}

