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
    let $startdate = $('#Startdate')
    let $enddate = $('#Enddate')
    $startdate.on('change',function(){
      $enddate[0].required = true
      if(this.value == "")
        $enddate[0].required = false
    })
    $enddate.on('change',function(){
      $startdate[0].required = true
      if(this.value == "")
        $startdate[0].required = false
    })

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
        startDate = data['Startdate']
        endDate = data['Enddate']
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
            data['username'],
            startDate,
            endDate
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
        startDate = data['Startdate']
        endDate = data['Enddate']
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
            data['username'],
            startDate,
            endDate
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
        startDate = data['Startdate']
        endDate = data['Enddate']
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
            data['username'],
            startDate,
            endDate
        )
    });
    getApiData(limit,offset)

});

function getApiData(limit,offset,requestnum='',scientificName='',localName='',invasiveType='',username='',start_date='',end_date=''){
    let $page = $('#page').empty()
    let $table = $('#table')
    
    // console.log(offset*limit)
    $.get(`/api/iasdata/?limit=${limit}&offset=${offset}&requestnum=${requestnum}&scientificName__scientificName=${scientificName}&scientificName__localName=${localName}&scientificName__invasiveType=${invasiveType}&requestnum__username__username=${username}&start_date=${start_date}&end_date=${end_date}`,
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
            let head = `
            <thead>
                <tr>
                    <th scope="col">ID</th>
                    <th scope="col">Filename</th>
                    <th style="white-space: nowrap;" scope="col">Scientific Name</th>
                    <th style="white-space: nowrap;" scope="col">Plant Type</th>   
                    <th scope="col">Latitude</th>
                    <th scope="col">Longtitude</th>
                    <th scope="col">#Link</th>   
                </tr>
            </thead>
            <tbody>
            `
            let body =``
            let promises = []
            data['results'].forEach((element,index) => {
           
                promises.push($.get(`/database/getvote/${element['id']}`,"json"));
                
                let scientificName = element['scientificName']['scientificName'].split(' ') 
                body +=`
                <tr data-bs-toggle="collapse" href="#collapse${element['id']}" role="button" aria-expanded="false" aria-controls="collapse${element['id']}">
                    <th scope="row">${element['id']}</th>
                    <td ><div class="cut-text"> ${element['filename']} </div></td>
                    <td class="cut-text">
                        <p style="display: inline ;font-style: italic;"> ${ scientificName[0] } ${ scientificName[1] }</p>
                    </td>
                    <td>${element['scientificName']['invasiveType']}</td>
                    <td>${element['latitude']}</td>
                    <td>${element['longtitude']}</td>
                    <td>
                        <a  href="/classifier/results/${element['requestnum']['id']}"> 
                            <span class="material-symbols-outlined bg-primary edit_data">
                                edit
                            </span> 
                        </a>
                    </td>
                </tr>
                
                <tr>

                <td colspan="${Object.keys(element).length}" class="py-0">        
                `
                if(index == 0)
                    body +=`
                    <div  class="collapse show" id="collapse${element['id']}">
                    `    
                else
                    body += `
                    <div class="collapse" id="collapse${element['id']}">   
                    `  
                    body += `
                        <div class="card mb-3" >
                            <div class="row g-0">

                                <div class="col-1 vote">

                                    <span id="up-${element['id']}" class="material-symbols-outlined up vote-icon">

                                        arrow_drop_up
                                        <div class="popup"> 
                                            Up vote if the <br>result is <b> Accurate </b>
                                        </div>
                                    </span>

                                    <span class="text"> 
                                        ${element['points']}
                                    </span>

                                    <span id="down-${element['id']}" class="material-symbols-outlined down vote-icon">
                                        arrow_drop_down
                                        <div class="popup"> 
                                            Down vote if the <br> result is <b> Inaccurate </b>
                                        </div>
                                    </span>
                                </div>
                                <div class="col-md-8 iasImageCol">
                                    <img src="${window.location.origin}/blobstorage/raw/${element['requestnum']['username']}/${element['filename']}" class="img-fluid rounded-start iasImage " alt="...">        
                                </div>
                                <div class="col-md">             
                                    <div class="card-body description">
                                        <h5 class="card-title plantName">  
                                        <p style="display: inline ;font-style: italic;"> ${ scientificName[0] } ${ scientificName[1] }</p> (${element['scientificName']['localName']})
                                        </h5>
                                        <p class="card-text justify">
                                            <span class="identifier">Family: </span>
                                            ${element['scientificName']['family']} <br>

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

                                            <span class="identifier">Link: </span>
                                            ${element['scientificName']['link']} <br>
                                        </p>
                                        <div class="plantWrapper">
                                        `
                                        element['scientificName']['images'].forEach(image => {              
                                            body+=
                                            `
                                                <div class=" plantImage">
                                                    <img src="/blobstorage/getplant/${image.plantInformation}/${image.filename}" class="card-img" alt="...">
                                                </div>
                                            `
                                        });

                                        body+=                        
                                        `</div>
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
                    </div>
                </td> 
            </tr>    
                `
            });
            let endBodyTag =`
            </tbody>
            `
            $table.html(() => {
                return head+ body + endBodyTag;
            });
            
            voteListener();


            $.when.apply($,promises).then(function(response){
                response.forEach(element => {
                    $(`#${element.type}-${element.iasdata_id}`).addClass('activate')
                });       
            })
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