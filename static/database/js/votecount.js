$(document).ready(function () {
    $('#alertClose').click(function (e) { 
        e.preventDefault();
        $('#alert').removeClass('show')
        $('#alert').addClass('hide')
    });
});

// Points Live Updater
let scoreListener = []
let liveupdate = false

function voteListener(){
    if(liveupdate)
        scoreListener.forEach(element => {
            clearInterval(element)
        });
    $.each($('.up'), function (indexInArray, valueOfElement) { 
        let that = this;

        let id = $(this).attr('id').split('-')[1]
        // $.get(`/database/refreshvotepoints/${id}`,
        //     function (_, textStatus, jqXHR) {
        //         $.get(`/api/iasdata/?id=${id}`,
        //             function (data, textStatus, jqXHR) {
        //                 $(that).siblings('.text').html(data[0].points)
        //             },
        //             "json"
        //         );
        //     },
        //     "json"
        // );

        if(liveupdate){
            let interval = setInterval(() => {
                $.get(`/api/iasdata/?id=${id}`,
                    function (data, textStatus, jqXHR) {
                        $(that).siblings('.text').html(data[0].points)
                    },
                    "json"
                );
            }, 2000);
            scoreListener.push(interval)
        }
         
        $(this).click(function (e) { 
            e.preventDefault();
            sendData('up',this)

        });
    });
    $.each($('.down'), function (indexInArray, valueOfElement) { 
        let that = this;
        $(this).click(function (e) { 
            e.preventDefault();
            
            sendData('down',this)
        });
    });
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
function sendData(type,obj){
    let id = $(obj).attr('id').split('-')[1]
    
    $.ajax({
        type: "POST",
        url: "/database/votecount/",
        data: {'type':type,'id':id},
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": Cookies.get("csrftoken"), 
        },
        success: function (response) {
            $(obj).siblings('.text').html(response['status'])
            $(obj).siblings().removeClass('activate')
            if($(obj).hasClass('activate'))
                $(obj).removeClass('activate')
            else
                $(obj).addClass('activate')
        },
        error: function(response){
            showAlert('#alert','<strong>Hi there!</strong> Authentication Warning: Pls. authenticate your account to vote')
        }
        
    });
}