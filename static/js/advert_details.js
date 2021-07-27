import {toggleWishlist} from "./wishlist_utils.js"


const callButton = document.getElementsByClassName('call-button')[0];
const wishlistToggleBtn = document.getElementById("toggleWishlistBtn");


thumbnailWrapper.disabled = true;
//Event Listeners



//Event listener for the call button
callButton.addEventListener('click',showPhoneNumber);


wishlistToggleBtn.addEventListener("click",toggleWishlist);

// On click if phone number is different from our default show the number else show Not provided
function showPhoneNumber(event){
    event.preventDefault();
    phoneNumber = callButton.getAttribute('data-number');
    if(phoneNumber === "00000000000" || phoneNumber === ''){
        callButton.innerText= 'Not provided';
        return;
    }
    callButton.innerText= phoneNumber;

}

//On click gets the target src and pass it to the setImage function
