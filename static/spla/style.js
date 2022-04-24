
  // hoverとactiveをpcとタブレットで切り替える
$(function () {
  var userAgent = navigator.userAgent; // ユーザーエージェント判定
  var link = $('.js-link-hover'); // aタグ要素代入
  var block = $('.js-btn-hover , .js-div-hover , .js-img-hover'); // buttonタグ、divタグ、imgタグ要素代入
  var list = $('.js-li-hover'); // liタグ要素代入
  // aタグを踏んだ時の端末判定とhover装飾
  if (userAgent.indexOf("iPhone") >= 0 || userAgent.indexOf("iPad") >= 0 || userAgent.indexOf("Android") >= 0) {
    link.on("touchstart", function () {
      $(this).addClass("link-hover");
    });
    link.on("touchend", function () {
      $(this).removeClass("link-hover");
    });
  } else {
    link.hover(
      function () {
        $(this).addClass("link-hover");
      },
      function () {
        $(this).removeClass("link-hover");
      }
    );
  }
  // buttonタグ、divタグ、imgタグを踏んだ時の端末判定とhover装飾
  if (userAgent.indexOf("iPhone") >= 0 || userAgent.indexOf("iPad") >= 0 || userAgent.indexOf("Android") >= 0) {
    block.on("touchstart", function () {
      $(this).addClass("block-hover");
    });
    block.on("touchend", function () {
      $(this).removeClass("block-hover");
    });
  } else {
    block.hover(
      function () {
        $(this).addClass("block-hover");
      },
      function () {
        $(this).removeClass("block-hover");
      }
    );
  }
  // liタグを踏んだ時の端末判定とhover装飾
  if (userAgent.indexOf("iPhone") >= 0 || userAgent.indexOf("iPad") >= 0 || userAgent.indexOf("Android") >= 0) {
    list.on("touchstart", function () {
      $(this).addClass("list-hover");
    });
    list.on("touchend", function () {
      $(this).removeClass("list-hover");
    });
  } else {
    list.hover(
      function () {
        $(this).addClass("list-hover");
      },
      function () {
        $(this).removeClass("list-hover");
      }
    );
  }
});