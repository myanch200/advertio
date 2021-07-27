const usernameField = document.getElementById('id_username');
let resultSpan = document.getElementById("resultSpan");
usernameField.addEventListener('input',(event)=>{
    let get_url =`/check_username/${event.target.value}`;
    $.ajax({
        url: get_url ,
        type: 'get',
        // This is the default though, you don't actually need to always mention it
        success: function(data) {
            if(data.exists){
                resultSpan.innerText = "Username alredy taken";
                resultSpan.classList = "username-taken";
            }
            if(!data.exists){
                resultSpan.innerText = "Username available";
                resultSpan.classList = "username-available";

            }
           
        },
        failure: function(data) { 
            alert('Got an error dude');
        }
    }); 
});

 