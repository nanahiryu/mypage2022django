// ドロップダウンメニューを動かす
$(function () {
    $('.header-nav ul li').hover(function(){
        $(this).children(".menuSub:not(:animated)", this).slideDown();
    }, function(){
        $(this).children(".menuSub", this).slideUp();
    });
});

// hamburger
$(function () {
  $('.hamburger-bar').click(function(){
    if ($(".header-nav").css('display') === 'none') {
      $(this).parent().next(".header-nav:not(:animated)").slideDown();
    }
    else {
      $(this).parent().next(".header-nav").slideUp();
    }
  })
});


$(window).on("resize", function() {
  var w = $(window).width();
  if (w > 767) {  // ブレークポイント（単位：px）
    $(".header-nav").css('display','block')
  }
  else {
    $(".header-nav").css('display','none')
  }
});


  // hoverとactiveをpcとタブレットで切り替える
$(function () {
  var userAgent = navigator.userAgent; // ユーザーエージェント判定
  var header_nav_ul_li = $('.header-nav ul li');
  var menuSub_li = $('.menuSub li');
  var logo_name = $('.header-logo-name');

// タグ踏んだときのタブレットとpcの挙動を変える
  if (userAgent.indexOf("iPhone") >= 0 || userAgent.indexOf("iPad") >= 0 || userAgent.indexOf("Android") >= 0) {
    menuSub_li.on("touchstart", function () {
      $(this).addClass("bg_hover_red");
      }
    );
    menuSub_li.on("touchend", function () {
      $(this).removeClass("bg_hover_red");
    });
  } else {
    menuSub_li.hover(
      function () {
        $(this).addClass("bg_hover_red");
      },
      function () {
        $(this).removeClass("bg_hover_red");
      }
    );
  }

  if (userAgent.indexOf("iPhone") >= 0 || userAgent.indexOf("iPad") >= 0 || userAgent.indexOf("Android") >= 0) {
    header_nav_ul_li.on("touchstart", function () {
      $(this).children(".header-nav-top-link").addClass("bg_hover_red");
    });
    header_nav_ul_li.on("touchend", function () {
      $(this).children(".header-nav-top-link").removeClass("bg_hover_red");
    });
  } else {
    header_nav_ul_li.hover(
      function () {
        $(this).children(".header-nav-top-link").addClass("bg_hover_red");
      },
      function () {
        $(this).children(".header-nav-top-link").removeClass("bg_hover_red");
      }
    );
  }

  if (userAgent.indexOf("iPhone") >= 0 || userAgent.indexOf("iPad") >= 0 || userAgent.indexOf("Android") >= 0) {
    logo_name.on("touchstart", function () {
      $(this).parent(".header-logo").addClass("hover_opacity_08");
      $(this).parent(".header-logo").addClass("hover_nondecoration");
    });
    logo_name.on("touchend", function () {
      $(this).parent(".header-logo").removeClass("hover_opacity_08");
      $(this).parent(".header-logo").removeClass("hover_nondecoration");
    });
  } else {
    logo_name.hover(
      function () {
        $(this).parent(".header-logo").addClass("hover_opacity_08");
        $(this).parent(".header-logo").addClass("hover_nondecoration");
      },
      function () {
        $(this).parent(".header-logo").removeClass("hover_opacity_08");
        $(this).parent(".header-logo").removeClass("hover_nondecoration");
      }
    );
  }  

});