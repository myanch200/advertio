const profileBtn = document.getElementById('profileBtn');
const profileOptions = document.getElementsByClassName('profile-options')[0];
const arrowIcon = document.getElementById('arrowIcon');
profileBtn.addEventListener('click', menuToggle);

function menuToggle(event) {
    event.preventDefault();
    profileOptions.classList.toggle('hidden');
    profileOptions.classList.contains('hidden') ? arrowIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path d="M4 9L12 17L20 9" stroke="#001A72" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </svg>
    ` :
        arrowIcon.innerHTML = `<svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M20 15L12 7L4 15" stroke="#001A72" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </svg>
        `;
}
console.log(profileBtn);