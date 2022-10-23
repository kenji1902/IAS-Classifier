function showAlert(id,text){
    $(id).removeClass('hide')
    $(id).addClass('show')
    $(`${id} .text`).html(text)
    return setTimeout(() => {
        $(id).removeClass('show')
        $(id).addClass('hide')

    }, 5000);
}

$(document).ready(function () {
    $('#alertClose').click(function (e) { 
        e.preventDefault();
        $('#alert').removeClass('show')
        $('#alert').addClass('hide')
    });
    $('form').submit(function (e) { 
        e.preventDefault();
        let serialized = $(this).serializeArray()
        let file = $('#file')[0].files[0]
        console.log(file)
        let formData = new FormData();
        formData.append('eduAttainment',serialized[0].value)
        formData.append('file',file)
        console.log(formData)
        $.ajax({
            type: "POST",
            url: "/accounts/credentials/",
            data: formData,
            dataType: "json",
            contentType: false,
            cache: false,
            processData: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": Cookies.get("csrftoken"), 
            },
            success: function (response) {
                showAlert('#alert','File Uploaded Successfully ')
            }
        });
    });
    
});