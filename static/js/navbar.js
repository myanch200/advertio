const profileBtn = document.getElementById('profileBtn');
const profileOptions = document.getElementsByClassName('profile-options')[0];
const arrowIcon = document.getElementById('arrowIcon');
profileBtn.addEventListener('click', menuToggle);

function menuToggle(event) {
    event.preventDefault();
    profileOptions.classList.toggle('hidden');
    profileOptions.classList.contains('hidden') ? arrowIcon.classList = 'fa fa-caret-down' :
        arrowIcon.classList = 'fa fa-caret-up';
}
console.log(profileBtn);