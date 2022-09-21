$(document).ready(function () {
    InitWrap()
    $('#search').on("input",function(){
        const search = $(this).val()
        if(search.length == 0)
            InitWrap()
        else
            InitWrap(search)
    })
    

});
function InitWrap(search=''){
    Init((instruction,image)=>{
        let body = ''
        body +=
        `
        <div id="${instruction.instruction_order}" class="instruction">
            <div class="card">
                <h5 class="card-header">${instruction.title}</h5>
                <div class="card-body">
                <p class="card-text">${instruction.description}</p>
                </div>
                <div class="carousel_wrapper">
                <div id="carousel_${instruction.instruction_order}" class="carousel carousel-dark slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                    `
                    image.forEach((element,i) => {
                        body+=
                        ` 
                        <button type="button" data-bs-target="#carousel_${i}" data-bs-slide-to="${i}" class="active indicator" aria-current="true" aria-label="Slide ${i}"></button>
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
                    <button class="carousel-control-prev" type="button" data-bs-target="#carousel_${instruction.instruction_order}" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carousel_${instruction.instruction_order}" data-bs-slide="next">
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
    $.get(`api/instruction/?ordering=instruction_order&search=${search}`,
        function (instruction, textStatus, jqXHR) {
            let promises = [];
            instruction.forEach(element => {
                let request = $.get(`api/instructionimages/?instruction=${element.instruction_order}&ordering=step`,
                    "json"
                );
                promises.push(request)
            });
            
            $.when.apply(null, promises).done(function(){
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
