import {toggleWishlist} from "./wishlist_utils.js"
const wishlistToggleBtn = document.getElementById("toggleWishlistBtn");
const thumbnailWrapper = document.getElementsByClassName('thumbnail-wrapper')[0];
const callButton = document.getElementById("callButton")

thumbnailWrapper.disabled = true;
//Event Listeners



//Event listener for the call button
callButton.addEventListener('click',showPhoneNumber);


wishlistToggleBtn.addEventListener("click",toggleWishlist);

// On click if phone number is different from our default show the number else show Not provided
function showPhoneNumber(event){
    let blanks = ["00000000000",'',null]
    event.preventDefault();
    let phoneNumber = callButton.getAttribute('data-number');
    if(phoneNumber in blanks){
        callButton.innerText= 'Not provided';
        return;
    }
    callButton.innerText= phoneNumber;

}

//On click gets the target src and pass it to the setImage function
