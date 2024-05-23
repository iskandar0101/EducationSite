let menu = document.querySelector('#menu');
let navbar = document.querySelector('.navbar');

menu.onclick = () =>{
  menu.classList.toggle('fa-times');
  navbar.classList.toggle('active');
}

window.onscroll = () =>{
  menu.classList.remove('fa-times');
  navbar.classList.remove('active');
}

document.addEventListener('DOMContentLoaded', function() {
  const courseImage = document.getElementById('courseImage');

  courseImage.addEventListener('click', function() {
    const lightbox = document.createElement('div');
    lightbox.id = 'lightbox';
    document.body.appendChild(lightbox);

    const img = document.createElement('img');
    img.src = courseImage.src;
    lightbox.appendChild(img);

    lightbox.addEventListener('click', function() {
      lightbox.remove();
    });
  });
});
