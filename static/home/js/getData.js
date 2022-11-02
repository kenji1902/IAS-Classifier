$(document).ready(function () {
    InitWrap()
    $('#search').on("input",function(){
        const search = $(this).val()
        if(search.length == 0){
            clearTimeout(window.swingIn)
            InitWrap()
        }
        else{
            $('.instruction').addClass('swing-out-top-bck')
            clearTimeout(window.swingIn)
            window.swingIn = setTimeout(() => {
                $('.instruction').removeClass('swing-out-top-bck')
                InitWrap(search)
            }, 1000);
        }
            
    })
    

});
function InitWrap(search=''){
    Init((instruction,image)=>{
        let body = ''
        body +=
        `
        <div id="${instruction.id}" class="instruction swing-in-top-fwd">
            <div class="card">
                <h5 class="card-header">${instruction.title}</h5>
                <div class="card-body">
                <p class="card-text">${instruction.description}</p>
                </div>
                <div class="carousel_wrapper">
                <div id="carousel_${instruction.id}" class="carousel carousel-dark slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                    `
                    image.forEach((element,i) => {
                        if(i == 0)
                        body+=
                        ` 
                        <button type="button" data-bs-target="#carousel_${instruction.id}" data-bs-slide-to="${i}" class="active indicator" aria-current="true" aria-label="Slide ${i}"></button>
                        `
                        else
                        body+=
                        ` 
                        <button type="button" data-bs-target="#carousel_${instruction.id}" data-bs-slide-to="${i}" class="indicator" aria-current="true" aria-label="Slide ${i}"></button>
                        `
                    });
                    body +=            
                    `
                    </div>
                    <div class="carousel-inner">
                    `
                    image.forEach((element,i) => {
                        if(i == 0)
                        body+=
                        `  
                        <div class="carousel-item active">
                        `
                        else
                        body+=
                        `
                        <div class="carousel-item">
                        `
                        body+=
                        `                        
                            <div class="d-flex justify-content-center align-items-center" style="width:100%;height:100%;">
                                <img src="/blobstorage/instruction/${element.image}"  alt="...">
                            </div>
                        </div>
                        `
                    });
                    body+=
                    `    
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carousel_${instruction.id}" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carousel_${instruction.id}" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                    </div>
                </div>
            </div>
        </div>`
        return body
    },search);

}

function Init(callback,search){
    let $instructionWrapper = $('.instructionWrapper')
    $instructionWrapper.html('')
    $.get(`api/instruction/?ordering=order&search=${search}`,
        function (instruction, textStatus, jqXHR) {
            let promises = [];
            instruction.forEach(element => {
                let request = $.get(`api/instructionimages/?instruction=${element.id}&ordering=step`,
                    "json"
                );
                promises.push(request)
            });
            
            $.when.apply($, promises).then(function(response){
                
                instruction.forEach((element,i) => {
                    const image = promises[i].responseJSON
                    const body = callback(element,image)
                    $($instructionWrapper).append(body);
                });                
             })
        },
        "json"
    );
}
