
import {toggleWishlist} from "./wishlist_utils.js"
let toggleWishlistButtons = document.querySelectorAll('.toggle-wishlist');
for (let item of toggleWishlistButtons) {
    item.addEventListener("click",toggleWishlist)
}





