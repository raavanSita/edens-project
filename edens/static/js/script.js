const images = document.querySelectorAll(".newImg > img");
const price = document.querySelectorAll('.product-description > h4')

images.forEach(image => {
    image.addEventListener("click", e => {
        $('#popImg img').attr('src', image.src)
    })
}, price => {
    price.addEventListener('click', e => {
        $('.quickview_pro_des > .title').append(price)
    })
})


$(document).ready(function() {
    $('.flipTimer').flipTimer({

        // count up or countdown
        direction: 'down',

        // the target <a href="https://www.jqueryscript.net/time-clock/">date</a>
        date: 'march 20, 2021 08:30:30',

        // callback works only with direction = "down"
        callback: function() { alert('times up!'); }

    });
});