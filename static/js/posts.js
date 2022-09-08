/////////////////////////
// JavaScript for Posts page
///////////////////////

$(function (){
    // Executed when js-menu-icon is clicked
    $('.js-menu-icon').click(function() {
        // $(this) : self element, namely div.js-menu-icon
        // next() : next to div.js-menu-icon, namely div.menu
        // toggle() : switch show to hide
        $(this).next().toggle();
    })
})

const btnHeart = document.getElementById('btnHeart');
let index = 0;
const colors = ['red', 'black']

btnHeart.addEventListener('click', function onClick() {
    btnHeart.style.color = colors[index];
    index = index >= colors.length - 1 ? 0 : index + 1;
});