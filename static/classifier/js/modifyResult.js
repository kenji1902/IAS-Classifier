$(document).ready(function () {
    $('form').on('submit',function (e) { 
        e.preventDefault();
        let form = $( this ).serialize().split('&');
        let data = []
        form.forEach(e => {
            let element = e.split('=');
            element = element[1]
            const id = element.split('-')[0];
            const scientificName = element.split('-')[1] 
            data.push({
                'id':id,
                'scientificName':scientificName
            })
        });
      
        let formData = new FormData();
        formData.append("update", JSON.stringify(data));
        $.ajax({
            method: "POST",
            url: "/classifier/modifyresults/",
            data: formData,
            cache: false,
            contentType: false,
            processData: false,
            headers: {
                "X-Requested-With": "XMLHttpRequest",
                "X-CSRFToken": Cookies.get("csrftoken"), 
            },
            success: function (response) {
                console.log(response)
                location.reload()   
            }
        });
    });
});