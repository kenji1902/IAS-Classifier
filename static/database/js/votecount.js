function voteListener(){
    $.each($('.up'), function (indexInArray, valueOfElement) { 
        let that = this;
        
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

function sendData(type,obj){
    let id = $(obj).attr('id').split('-')[1]
    $.ajax({
        type: "POST",
        url: "/classifier/votecount/",
        data: {'type':type,'id':id},
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": Cookies.get("csrftoken"), 
        },
        success: function (response) {
            $(obj).siblings('.text').html(response['result'] +"ASDASDASD")
        }
    });
}