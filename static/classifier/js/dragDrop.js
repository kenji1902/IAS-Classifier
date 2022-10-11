
let imageLoaded = new Array();
let rawImageID = 0;
let coords =  new Array();
let ppImageID = 0

$(document).ready(function () {
    navigator.permissions.query({ name: 'geolocation' }).then((result) => {
        if (result.state === 'denied') {
            console.log(result.state);
            $(".upload-box").hide();
            showAlert('#alert','<strong>Hi there!</strong> You should enable Geolocation Permission <br> go to home and search "Allow Location".')
        }
    })
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

    $dropArea.on('paste',function(e){
        e.preventDefault();
        e = e.originalEvent;
        let files = []
        for (var i = 0; i < e.clipboardData.items.length; i++) {
            let file = e.clipboardData.items[i]
            files.push(file.getAsFile())
        }
        console.log(files)
        uploadFile(files)

    });

    $('#preprocessed').hover(function () {
            // over
            window.helperHover = setTimeout(() => {
                $('#preproccesedhelper').addClass('hidden')
            }, 4000);
            $('#preproccesedhelper').removeClass('hidden')
        }, function () {
            // out
            clearTimeout(window.helperHover)
            $('#preproccesedhelper').addClass('hidden')

        }
    );
    //Touch
    $('#preprocessed').on('touchstart', function () {
        window.helperTouch = setTimeout(() => {
            $('#preproccesedhelper').addClass('hidden')
        }, 2000);
        $('#preproccesedhelper').removeClass('hidden')
    });
    //End
    $('#preprocessed').on('touchend', function () {
        clearTimeout(window.helperTouch)
        $('#preproccesedhelper').addClass('hidden')
    });

    $('#closeCarousel').click(function (e) { 
        e.preventDefault();
        $(this).parent().addClass('hidden')
    });
    $('#alertClose').click(function (e) { 
        e.preventDefault();
        $('#alert').removeClass('show')
        $('#alert').addClass('hide')
    });
    
    // $('#file').click(function(){ $('#fileElem').trigger('click'); });
    // $('#file').on('touchstart', function(){ $('#fileElem').trigger('click'); });
    // $('#camera').click(function(){ $('#cameraElem').trigger('click'); });
    
});

function classifyClick(e){
    $('#classify .spinnerCont').removeClass('hidden')
    $('#dropAreaSpinner').removeClass('hidden')
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
        },
        error: function(data){
            console.log(data)
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
            delete coords[$(this).attr('id')];
            if(isEmpty($rawImages)){
                slideUp($('#filter'),200);
                slideUp($('#raw'),500);
                slideUp($('#remove_blur'),150);
            }
        });
        imageLoaded.push(files);
        console.log('image loaded')
        rawImageID++;
        
    }

}
function slideUp($element,animate){
    $element.animate({
        bottom: '4rem',
        opacity: '0',
        height : '0',
        margin :'0',
        padding:'0'
    },animate);
    return setTimeout(() => {
        $element.addClass('hidden');
    }, animate + 200);
}
function slideDown($element,animate){
    return setTimeout(() => {
        $element.css({
            margin :'',
            padding:'',
            height:''
        })
        let height = $element.height()
        let margin = $element.css('margin')
        $element.css({
            margin :'0',
            height:'0'
        })
        $element.removeClass('hidden').animate({
            bottom: '0rem',
            opacity: '1',
            height:  height,
            margin :margin,
        },animate)
        
    }, animate + 200);
}

function showAlert(id,text){
    $(id).removeClass('hide')
    $(id).addClass('show')
    $(`${id} .text`).html(text)
    return setTimeout(() => {
        $(id).removeClass('show')
        $(id).addClass('hide')

    }, 5000);
}

let acceptableFileType = ['image/jpeg','image/jpg']
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
let invalidUploadFileFlag = null
function uploadFile(files){
    
    // let Files = files.originalEvent.dataTransfer.files;
    showSpinner();
    $('#dropAreaSpinner').removeClass('hidden')
    for (let i = 0; i < files.length; i++){
        if(files[i] == null){
            hideSpinner()
            continue
        }
            
        if(!acceptableFileType.includes(files[i]['type'])){
            clearTimeout(invalidUploadFileFlag);
            invalidUploadFileFlag = showAlert('#alert','<strong>Hi there!</strong> You should only use images with "jpeg/jpg" format.')
            hideSpinner()
            $('#dropAreaSpinner').addClass('hidden')
            continue
        }
        previewFile(files[i])
        getAddress(function (cookie) {
            coords.push(JSON.stringify(cookie))
            console.log('image GPS loaded')

            if(i == files.length - 1){

                if($('#raw.hidden').length){
                    slideDown($('#raw'),500);
                    slideDown($('#filter'),500);
                    slideDown($('#remove_blur'),1000);
                }
                hideSpinner()
                $('#dropAreaSpinner').addClass('hidden')
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

let renamedFormatFlag = null
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
            if(data['invalidFormatFlag'] == true){
                clearTimeout(renamedFormatFlag)
                renamedFormatFlag = showAlert('#alert','<strong>Hi there!</strong> An image was not uploaded, it might have been renamed with jpg extension <br> pls upload an image with "JPG/JPEG" format.')
            }
            data['images'].forEach(files => {    
                console.log('files: ',files)
                filter(files,`${window.location.origin}/blobstorage/filter/${files}`)      
            });
            
            $('#preprocessedSpinner').addClass('hidden')
            hideSpinner()
            if(data['invalidFormatFlag'] == true && $('#preprocessed.hidden').length){
                clearTimeout(preprocessedTimeout)
                clearTimeout(classifyTimeout)
                if($('#preprocessed.hidden').length == 0){
                    slideUp($('#classify'),200);
                    slideUp($('#preprocessed'),500);
                    console.log('hidden2')

                }
                preprocessedTimeout = null
                classifyTimeout = null
                console.log('hidden')
            }
            if(preprocessedTimeout != null && $('#preprocessed').has('.file-content').length == 0){
                slideUp($('#classify'),200);
                slideUp($('#preprocessed'),500);
                console.log('not hidden')

            }
        },
        
    });
}
let preprocessedTimeout = null
let classifyTimeout = null
function clickFilter(e){
    
    $('#preprocessedSpinner').removeClass('hidden')
    if($('#preprocessed.hidden').length){
        preprocessedTimeout = slideDown($('#preprocessed'),500);
        classifyTimeout = slideDown($('#classify'),500);
    }
    showSpinner();
    let formData = new FormData();
    for (let i = 0; i < imageLoaded.length; i++){
        formData.append('files[]',imageLoaded[i]);
        formData.append('coords[]',coords[i]);
    }
    const remove_blur =  $('#remove_blur_input').is(":checked")
    formData.append('remove_blur',remove_blur) 
    for (var key in imageLoaded) {
          delete imageLoaded[key];
          $(`#${key}`).parent().remove();
    }
    for (var key in coords) {
        delete coords[key];
    }
    uploadFormData(formData);

    slideUp($('#filter'),200);
    slideUp($('#raw'),500);
    slideUp($('#remove_blur'),150);


}
let preprocessedImages = []
function filter(file,response){
    $ppImages = $("#preprocessed");
    let altName = file.split('.').slice(0,-1).join("")
    let extension = file.split('.').at(-1)
    $ppImages.prepend(
        `
        <div id="file${ppImageID}" class="file-content">
            <img src="${response}" class="image" alt="${altName}">
            <span class="image-name">${altName}</span>
            <span id="pp${ppImageID}"  class="close-image material-symbols-outlined">
                close
            </span>
        </div>                    
        `
    );
    $preprocessedCarousel = $('#preprocessedCarousel');
    // $preprocessedCarousel.children('.carousel').children('.carousel-indicators').append(
    //     `
    //     <button id="indicator${ppImageID}" class="indicator" type="button" data-bs-target="#preprocessedPrev" data-bs-slide-to="${ppImageID}" aria-label="Slide ${ppImageID}"></button>
    //     `
    // )
    $preprocessedCarousel.children('.carousel').children('.carousel-inner').append(
        `
        <div id="item${ppImageID}" class="carousel-item">
            <div class="d-flex justify-content-center align-items-center" style="width:100%;height:100%;">
                <img src="${response}" class="" alt="${altName}">
            </div>
        </div>
        `
    );
    $(`#file${ppImageID}`).click(function (e) { 
        e.preventDefault();
        $preprocessedCarousel.parent().removeClass('hidden')
        let id = $(this).attr('id').match(/\d+/).join('');
        
        
        // $(`#preprocessedCarousel .indicator`).removeAttr("aria-current");
        // $(`#preprocessedCarousel .indicator`).removeClass("active");
        // $(`#indicator${id}`).attr("aria-current","true");
        // $(`#indicator${id}`).addClass('active');
        $('#preprocessedCarousel .carousel-item').removeClass('active')
        $(`#item${id}`).addClass('active')
    });

    $(`#pp${ppImageID}`).click(function (e) { 
        e.preventDefault();
        let id = $(this).attr('id').match(/\d+/).join('');
        $(this).parent().remove();
        $(`#item${id}`).remove();
        // $(`.indicator${id}`).remove();
        var index = preprocessedImages.indexOf(altName+ '.' +extension);
        if (index !== -1) { 
            preprocessedImages.splice(index, 1);
        }
        if($('#preprocessed').has('.file-content').length == 0){
            slideUp($('#classify'),200);
            slideUp($('#preprocessed'),500);
        }
    });    
    preprocessedImages.push(altName + '.' +extension)
    ppImageID++
}

