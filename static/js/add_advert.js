const advertForm = document.getElementById("addAdvertForm");
const title = document.getElementById("id_title");
const category = document.getElementById("id_category");
const description = document.getElementById("id_description");
const price = document.getElementById("id_price");
const currency = document.getElementById("id_currency");
const location = document.getElementById("id_location");
const imagesSubmit = document.getElementById("submitImages");
const advert_csrf = document.getElementsByName('csrfmiddlewaretoken')[1];
const url = ""
const alertBox = document.getElementById("alertBox");
alertBox.innerHTML = "";




Dropzone.autoDiscover = false;

function handleAlert(type,text){
    alertBox.classList += ` ${type}`;
    alertBox.innerText = text;
}
const myDropze = new Dropzone("#myDropzone",{
    url: "/ads/drop_image",
    maxFiles: 10,
    maxFilesize: 20,
    parallelUploads: 10,
    acceptedFiles: ".png , .jpg , .jpeg",
    autoProcessQueue: false,




});


advertForm.addEventListener('submit', e=>{
    e.preventDefault()

    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', advert_csrf.value)
    fd.append('title', title.value)
    fd.append('description', description.value)
    fd.append('category', category.value)
    fd.append('currency', currency.value)
    fd.append('location', location.value)
    fd.append('price', price.value)

    $.ajax({
        type: 'POST',
        url: url,
        enctype: 'multipart/form-data',
        data: fd,
        success: function(response){
            console.log(response)
            const sText = `${response.message}`
            myDropze.processQueue()
            handleAlert("success", sText)
            setTimeout(()=>{
                            window.location.replace("/")

            },5000)

        },
        error: function(error){
            console.log(error)
            alert(error.message)
        },
        cache: false,
        contentType: false,
        processData: false,
    })
})


