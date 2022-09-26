let totalRecord = 0;
let pages = 0
let limit = 5
let offset = 0
let currPage = 1
$(document).ready(function () {
    
    
    let $queryBtn = $('#queryBtn')
    let $option = $('#option')
    let $queryContent =  $('#queryContent')
    let $exit = $('#exit')


    $option.click(function (e) { 
        e.preventDefault();
        $queryContent.addClass('d-flex')
    });
    $exit.click(function (e) { 
        e.preventDefault();
        $queryContent.removeClass('d-flex')
    });
    $('#next').click(function (e) { 
        e.preventDefault();
        let form = $( '#query' ).serialize().split('&');
        let data = {}
        form.forEach(e => {
            let element = e.split('=');
            data[element[0]] = element[1] 
        });

        data['offset'] = parseInt(data['offset']) + 1
        limit = data['limit'];
        currPage = data['offset']
        offset = ( parseInt(data['offset']) - 1) * limit ;
        if(offset >= totalRecord)
            return
        
        getApiData(limit,offset,
            data['requestnum'],
            data['scientificName'],
            data['localName'],
            data['type'],
            data['username']
        )
    });
    $('#prev').click(function (e) { 
        e.preventDefault();
        let form = $( '#query' ).serialize().split('&');
        let data = {}
        form.forEach(e => {
            let element = e.split('=');
            data[element[0]] = element[1] 
        });

        data['offset'] = parseInt(data['offset']) - 1
        limit = data['limit'];
        currPage = data['offset']
        offset = ( parseInt(data['offset']) - 1) * limit ;
        if(offset > totalRecord)
            offset = 0
        if(offset < 0)
            return
        getApiData(limit,offset,
            data['requestnum'],
            data['scientificName'],
            data['localName'],
            data['type'],
            data['username']
        )
    });
    $( "form" ).on( "submit", function( event ) {
        event.preventDefault();
        let form = $( this ).serialize().split('&');
        let data = {}
        form.forEach(e => {
            let element = e.split('=');
            data[element[0]] = element[1]
            
            
        });
        
        limit = data['limit'];
        currPage = data['offset']
        offset = (parseInt(data['offset']) - 1) * limit ;
        if(offset > totalRecord)
            offset = 0
        
        getApiData(limit,offset,
            data['requestnum'],
            data['scientificName'],
            data['localName'],
            data['type'],
            data['username']
        )
    });
    getApiData(limit,offset)
    
});

function getApiData(limit,offset,requestnum='',scientificName='',localName='',invasiveType='',username=''){
    let $page = $('#page').empty()
    let $table = $('#table')
    // console.log(offset*limit)
    $.get(`/api/iasdata/?limit=${limit}&offset=${offset}&requestnum=${requestnum}&scientificName__scientificName=${scientificName}&scientificName__localName=${localName}&scientificName__invasiveType=${invasiveType}&requestnum__username__username=${username}`,
        function (data, textStatus, jqXHR) {
            
            totalRecord = data['count']
            if(totalRecord >= limit){
                pages = Math.ceil( totalRecord/limit );
                for (let i = 0; i < pages; i++) {
                    if(currPage == i+1){
                        $page.append(`<option selected value="${i+1}">${i+1}</option>`)
                        continue
                    }

                    $page.append(`<option value="${i+1}">${i+1}</option>`)
                    
                }
            }
            else $page.append(`<option value="${1}">${1}</option>`)

            $table.html(() => {
                let head = `
                <thead>
                    <tr>
                        <th scope="col">ID</th>
                        <th scope="col">Filename</th>
                        <th scope="col">Scientific Name</th>
                        <th scope="col">Invasive Type</th>   
                        <th scope="col">Latitude</th>
                        <th scope="col">Longtitude</th>
                        <th scope="col">#Link</th>   
                    </tr>
                </thead>
                <tbody>
                `
                
                let body =``
                data['results'].forEach((element,index) => { 
                    body +=`
                    <tr data-bs-toggle="collapse" href="#collapse${element['id']}" role="button" aria-expanded="false" aria-controls="collapse${element['id']}">
                        <th scope="row">${element['id']}</th>
                        <td class="tdCut"><div class="cut-text"> ${element['filename']} </div></td>
                        <td>${element['scientificName']['scientificName']}</td>
                        <td>${element['scientificName']['invasiveType']}</td>
                        <td>${element['latitude']}</td>
                        <td>${element['longtitude']}</td>
                        <td>
                            <a href="/classifier/results/${element['requestnum']['id']}"> 
                                <span class="material-symbols-outlined bg-primary edit_data">
                                    edit
                                </span> 
                            </a>
                        </td>
                    </tr>    
                    `
                    if(index == 0)
                        body +=`
                        <tr  class="collapse show" id="collapse${element['id']}">
                        `    
                    else
                        body += `
                        <tr class="collapse" id="collapse${element['id']}">   
                        `  
                    body += `
                        <td colspan="${Object.keys(element).length}">        
                            <div class="card mb-3" >
                                <div class="row g-0">
                                    <div class="col-md-8 iasImageCol">
                                        <img src="${window.location.origin}/blobstorage/raw/${element['requestnum']['username']}/${element['filename']}" class="img-fluid rounded-start iasImage " alt="...">        
                                    </div>
                                    <div class="col-md">             
                                        <div class="card-body description">
                                            <h5 class="card-title plantName">${element['scientificName']['scientificName']} (${element['scientificName']['localName']})</h5>
                                            <p class="card-text justify">
                                                <span class="identifier">Description: </span>
                                                ${element['scientificName']['description']} <br>
            
                                                <span class="identifier">Habitat: </span>
                                                ${element['scientificName']['habitat']} <br>
            
                                                <span class="identifier">Propagation: </span>
                                                ${element['scientificName']['propagation']} <br>
            
                                                <span class="identifier">Native Range: </span>
                                                ${element['scientificName']['nativeRange']} <br>
            
                                                <span class="identifier">Comments: </span>
                                                ${element['scientificName']['comments']} <br>
            
                                                <span class="identifier">Control: </span>
                                                ${element['scientificName']['control']} <br>
                                            </p>
                                            <p class="card-text date">
                                                <small class="text-muted">
                                                    Uploaded: ${element['requestnum']['date']}
                                                </small>
                                            </p>
                                            <p class="card-text date">    
                                                <small class="text-muted">
                                                    Last Updated: ${element['scientificName']['date']}
                                                </small>
                                            </p>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </td> 
                    </tr>
                    `
                });
                let endBodyTag =`
                </tbody>
                `
                return head+ body + endBodyTag;
            });
        },
        "json"
    ).fail(function(){
        $('#table').html(`
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Filename</th>
                    <th scope="col">Scientific Name</th>
                    <th scope="col">Latitude</th>
                    <th scope="col">Longtitude</th>   
                </tr>
            </thead>
            
        
        `)
    });
}