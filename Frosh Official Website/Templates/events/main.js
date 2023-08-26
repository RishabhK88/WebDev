jQuery(document).ready(function( $ ) {

  // Header fixed on scroll
  $(window).scroll(function() {
    if ($(this).scrollTop() > 100) {
      $('#header').addClass('header-scrolled');
    } else {
      $('#header').removeClass('header-scrolled');
    }
  });

  if ($(window).scrollTop() > 100) {
    $('#header').addClass('header-scrolled');
  }

  // Real view height for mobile devices
  if (window.matchMedia("(max-width: 767px)").matches) {
    $('#intro').css({ height: $(window).height() });
  }

  // Initiate the wowjs animation library
  new WOW().init();

  // Initialize Venobox
  $('.venobox').venobox({
    bgcolor: '',
    overlayColor: 'rgba(6, 12, 34, 0.85)',
    closeBackground: '',
    closeColor: '#fff'
  });

  // Initiate superfish on nav menu
  $('.nav-menu').superfish({
    animation: {
      opacity: 'show'
    },
    speed: 400
  });
 
  // Smooth scroll for the menu and links with .scrollto classes
  $('.nav-menu a, #mobile-nav a, .scrollto').on('click', function() {
    if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
      var target = $(this.hash);
      if (target.length) {
        var top_space = 0;

        if ($('#header').length) {
          top_space = $('#header').outerHeight();

          if( ! $('#header').hasClass('header-fixed') ) {
            top_space = top_space - 20;
          }
        }

        $('html, body').animate({
          scrollTop: target.offset().top - top_space
        }, 1500, 'easeInOutExpo');

        if ($(this).parents('.nav-menu').length) {
          $('.nav-menu .menu-active').removeClass('menu-active');
          $(this).closest('li').addClass('menu-active');
        }

        if ($('body').hasClass('mobile-nav-active')) {
          $('body').removeClass('mobile-nav-active');
          $('#mobile-nav-toggle i').toggleClass('fa-times fa-bars');
          $('#mobile-body-overly').fadeOut();
        }
        return false;
      }
    }
  });

  const width = 100;
const height = 62;
const size = 1050;
const CONTAINER = document.getElementById("container");
let ROW_COUNTER = 0;
const FINAL_COLORS = ["FFE285", "FFE99C", "FFE285", "FFD95C", "FFE285", "FFE99C", "FFE285", "FFE99C"];
const TOP_COLORS = ["B5E48C","D9ED92","FFC400", "FFCF33", 'FFE99C', "FFD95C", "FFE285", "FFE285"]
const MIDDLE_COLORS = ["52B69A", "76C893", "99D98C", "FFE285", "B5E48C", "D9ED92", "FFE99C", "EEBA0B"];
const BASE_COLORS = ["184E77", "1E6091", "1A759F", "52B69A","168AAD", "34A0A4", "B5E48C", "FFE99C"];

function generateTriangles(num) {
  for (let i = 0; i < num; i += 1) {
    let svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
    let path = document.createElementNS("http://www.w3.org/2000/svg", "path");
    path.setAttribute("d", "M 42.333333,232.83333 H 169.33333 l -63.5,-79.375 z");
    svg.setAttribute("viewBox","42.33333206176758 153.4583282470703 127 79.375");
    svg.style.left = (width/2 * i) % size;
    if ((width/2 * i) % size === 0 && i !== 0) {
      ROW_COUNTER += height;
    }
    svg.style.top = ROW_COUNTER;

    if(i % 2 !== 0) {
      svg.setAttribute("class",`rotated id-${i}`);
    } else {
      svg.setAttribute("class",`id-${i}`);
    }

    let idx = getRandomIdx();
    if ((width/2 * i) % size <= 300) {
      path.setAttribute("style", `fill: #${BASE_COLORS[idx]}; stroke: #${BASE_COLORS[idx]}`);
    } else if ((width/2 * i) % size < 600) {
      path.setAttribute("style", `fill: #${MIDDLE_COLORS[idx]}; stroke: #${MIDDLE_COLORS[idx]}`);
    } else if ((width/2 * i) % size < 800){
      path.setAttribute("style", `fill: #${TOP_COLORS[idx]}; stroke: #${TOP_COLORS[idx]}`);
    } else {
      path.setAttribute("style", `fill: #${FINAL_COLORS[idx]}; stroke: #${FINAL_COLORS[idx]}`);
    }
    svg.appendChild(path);
    CONTAINER.appendChild(svg);
  }
}

function getRandomIdx() {
  return Math.floor(Math.random() * 8);
}

generateTriangles(300);

// custom code

});
