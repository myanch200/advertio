const images = document.getElementsByClassName('img-item');
let thumbail = document.getElementById("thumbnailImg");
const leftArrow = document.getElementById("leftArrow");
const rightArrow = document.getElementById("rightArrow");
let counter = 0 ;

//Event Listeners

[leftArrow,rightArrow].forEach(item =>{
    item.addEventListener("click",changeImage)
})

for(i =0 ; i < images.length;i++){
    images[i].addEventListener('click',selectImage)
}

function selectImage(event){
    setImage(event.target.src)
}


function setImage(path){
    thumbail.setAttribute('src',path)
    console.log("Executed")
}



function changeImage(event){
    let index =0;
    if(event.target=== leftArrow){
        counter--;
        if(counter < 0){
            counter = images.length -1
        }
        index = counter;
        console.log(images[index])
        
    }else{
        counter++;
        index = counter% images.length;
        console.log(images[index])

       

    }
    setImage(images[index].src);

}