function formToJSON(f) {
    var fd = $(f).serializeArray();
    var d = [];
    let obj = {}
    fd.forEach((e,i) => {
        
        obj[e.name] = e.value
        if(i%3 == 2){
            d.push(obj)
            obj = {}
        }
    });
        
    return d;
}
$(document).ready(function () {
    $('form').on('submit',function (e) { 
        e.preventDefault();
        let serialize = formToJSON(this)
        data = []
        serialize.forEach(e => {
            const id = e.scientificName.split('-')[0];
            const scientificName = e.scientificName.split('-')[1]
            const latitude = e.latitude
            const longtitude = e.longtitude 
            data.push({
                'id':id,
                'scientificName':scientificName,
                'latitude':latitude,
                'longtitude':longtitude
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

    // let form = $( 'form' ).serialize().split('&');
    
    // form.forEach(e => {
    //     let element = e.split('=');
    //     element = element[1]
    //     const id = element.split('-')[0];
    //     $.getJSON(`/api/iasdata/?id=${id}`,
    //         function (data, textStatus, jqXHR) {
    //             const latitude = data[0].latitude
    //             const longtitude = data[0].longtitude
    //             const radius = 2000
    //             $.getJSON(`https://overpass.kumi.systems/api/interpreter?`+
    //                     `data=[out:json];%20(`+
    //                     `%20node(around:${radius},${latitude},%20${longtitude})[%22place%22=%22quarter%22];`+
    //                     `%20node(around:${radius},${latitude},%20${longtitude})[%22place%22=%22town%22];`+
    //                     `%20node(around:${radius},${latitude},%20${longtitude})[%22place%22=%22village%22];`+
    //                     `%20node(around:${radius},${latitude},%20${longtitude})[%22place%22=%22city%22];%20);`+
    //                     `%20out%20body;`,  
    //                 function (neighbors, textStatus, jqXHR) {
    //                     console.log(neighbors)
    //                 }
    //             );
    //         }
    //     );
    // });
    
    

    // $.get(`https://overpass.kumi.systems/api/interpreter?`+
    //         `data=[out:json];%20(`+
    //         `%20node(around:${radius},${features[i].position[0]},%20${features[i].position[1]})[%22place%22=%22quarter%22];`+
    //         `%20node(around:${radius},${features[i].position[0]},%20${features[i].position[1]})[%22place%22=%22town%22];`+
    //         `%20node(around:${radius},${features[i].position[0]},%20${features[i].position[1]})[%22place%22=%22village%22];`+
    //         `%20node(around:${radius},${features[i].position[0]},%20${features[i].position[1]})[%22place%22=%22city%22];%20);`+
    //         `%20out%20body;`, 
    //     function (data, textStatus, jqXHR) {
    //       // 
    //       data.elements.forEach(element => {

    //       });
    
    //     },
    //     "json"
    // )

});