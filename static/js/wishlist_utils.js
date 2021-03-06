import { getCookie } from "./utilities.js";
const csrftoken = getCookie('csrftoken');

let wishListTable = document.getElementById("wishlistTable");
let emptyHeart = `  <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <g clip-path="url(#clip0)">
                            <path d="M17.516 3C19.898 3 22.003 4.564 22.003 7.712C22.003 12.675 15.475 16.009 12 19.647C8.52501 16.009 1.99801 12.676 1.99801 7.713C1.99801 4.658 4.00601 3 6.48501 3C9.66501 3 11.331 6.644 12 8.312C12.667 6.646 14.333 3 17.516 3ZM17.516 1C15.342 1 13.17 2.062 12 4.419C10.83 2.062 8.65801 1 6.48501 1C3.08201 1 0.00100708 3.39 0.00100708 7.689C0.00100708 14.959 9.90401 18.627 12 23C14.096 18.627 24 14.959 24 7.689C24 3.103 20.586 1 17.516 1Z" fill="#696868"/>
                        </g>
                        <defs>
                        <clipPath id="clip0">
                        <rect width="24" height="24" fill="white"/>
                        </clipPath>
                        </defs>
                        <span class="wishlist-tooltip">Add to wishlist</span>
                    </svg>`;

let filledHeart = ` <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
<path d="M12 4.24801C8.852 -1.15399 0 0.423009 0 7.19201C0 11.853 5.571 16.619 12 23C18.43 16.619 24 11.853 24 7.19201C24 0.40001 15.125 -1.11399 12 4.24801Z" fill="#CC3030"/>
<span class="wishlist-tooltip">Remove from wishlist  </span>
                           </svg>`;

export function toggleWishlist(event){
    event.preventDefault();
    //get the id for each advert
    let id  = event.target.getAttribute("data-id")
    let get_url = `/ads/toggle_to_wishlist/${id}/`
    $.ajax({
        url: get_url ,
        type: 'post',
        data: {
            'csrfmiddlewaretoken':csrftoken
        },

        // This is the default though, you don't actually need to always mention it
        success: function(data) {
            
           if(data.message ==="Advert removed"){
               changeSVG(event.target,emptyHeart);

           }else{
            changeSVG(event.target,filledHeart)
           }

           
           document.getElementById("navbarCounter").innerText = data.wishlistCount;
          
        },
        failure: function(data) { 
            alert('Got an error dude');
        }
    }); 
}

function changeSVG(element,newSVG){
    let elementClassList = element.className.split(' ');
    if(elementClassList.includes("wishlist-remove")){
        element.parentElement.parentElement.remove()
    }else{
        element.innerHTML = newSVG;
    }
}