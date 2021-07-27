
import {toggleWishlist} from "./wishlist_utils.js"
let toggleWishlistButtons = document.getElementsByClassName('toggle-wishlist');
//Event listener for each button
for(let i = 0; i <= toggleWishlist.length;i++){
    toggleWishlistButtons[i].addEventListener("click",toggleWishlist);
}




