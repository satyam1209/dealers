$(".AddFavHeart").click(function () {
    var carid = $(this).attr("data-cid");
    var page =  $(this).attr("data-page");
    $.ajax({
      type: "GET",
      url: "/add_favourite_car/" + carid,
      dataType: "json",
      data:{
          p : page
      },
      success: function (res) {
          $("#filteredcars").html(res.data);
      },
    });
  });
  
  $(".RemFavHeart").click(function () {
    var carid = $(this).attr("data-cid");
    var page =  $(this).attr("data-page");
    $.ajax({
      type: "GET",
      url: "/delete_from_favourite/" + carid,
      data:{
          p : page
      },
      dataType: "json",
      success: function (res) {
          $("#filteredcars").html(res.data);
      },
    });
  });
  
  $(".card-pic").click(function(){
      var id = $(this).attr("data-cid")
      $.ajax({
      type: "GET",
      url: "/getImage/"+id+"/",
      dataType: "json",
      success: function (res) {
          $(".modal-body").html(res.data)
          $("#detailBtn").click(function(){
              window.location.href ="/viewdetails/"+id
          })
      },
    });
  })
  
  $(".page").click(function(){
      var page = $(this).attr("data-page");
      $(".page").removeClass("border-bottom")
      $(".page").removeClass("border-bottom")
      $(this).addClass("border-bottom")
      $(this).addClass("border-primary")
  
    $.ajax({
      type: "GET",
      url: "/dashboard/",
      dataType: "json",
      data:{
          p : page
      },
      success: function (res) {
          $("#filteredcars").html(res.data);
      },
    });
  })
  