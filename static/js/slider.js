const images = document.getElementsByClassName('img-item');
const thumbail = document.getElementById("thumbnailImg");
const leftArrow = document.getElementById("leftArrow");
const rightArrow = document.getElementById("rightArrow");

[leftArrow,rightArrow].forEach(item =>{
    item.addEventListener("click",changeImage)
})

//Adding event listener for each of the images
for( let j = 0 ; j < images.length;j++){
    images[j].addEventListener('click',selectImage)
}
let counter = 0 ;
let index =0;
export function selectImage(event){

    setImage(event.target.src)
}

/*
    I created setImage function rather that invoking setAttribute in both selectImage and Change image
    In this way we don't need to know which function is called all we do is set the src attribute to be the path passed as parameter.
*/
 function setImage(path){
    
    thumbail.setAttribute('src',path);
    thumbail.classList= 'fade-in';
    //Remove the animation class once the animation is completed 
    thumbail.onanimationend = function(){
        thumbail.classList = '';
    }
}



/* 
    Change image takes and event for paramater 
    and based on which arrow is pressed increments or decrements the counter variable.
    Which then we use to acces a image from the images array.
    I manage to cover some of the edge cases , but have a lot to test ,yet.
*/


export function changeImage(event){

        if(event.target === rightArrow){
            counter++;
            counter = counter % images.length;
        }

        if(event.target === leftArrow){
            counter--;
            
            if(counter < 0 ){
                counter = images.length -1
            }           
        }
        index = counter ;
        setImage(images[index].src)

   


}
