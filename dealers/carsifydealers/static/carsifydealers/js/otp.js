$("#signupBtn").click(function(){
    var otp = $("#otp").val();
    $.ajax({
      method:"POST",
      url:"/checkOTP/",
      dataType:"json",
      data:{
        otp : otp,
        csrfmiddlewaretoken: '{{ csrf_token }}'
        },
        success:function(res){
          if(res.data == 1){
            $.ajax({
              url:"/signup/",
              dataType:"json",
              method:"POST",
              data:{
                'name': $("#name").val(),
                'email' : $("#email").val(),
                'number': $("#number").val(),
                'password' : $("#password").val(),
              }
            })
          }
          if(res.data == 0){
          alert("Invalid OTP");}
      }
    })
  });

  function CheckFields(){
    var name = $("#name").val();
    var email = $("#email").val();
    var number = $("#number").val();
    var password = $("#password").val();
    if(name == "" || email == "" || number == "" || password.trim() == ""){
      console.log(name," ",email," ",number," ",password);
      return false;
    }
    return true;
}  

var password = document.querySelector("#password");
password.on("keyup",function(e){
  if(e.keyCode == 13){
    $("#OTPBtn").click();
  }
});

function OTPSending(){
  var email = document.querySelector("#email").value;
  if(CheckFields()){
    $.ajax({
      url: "/mailOTP/",
      type: "POST",
      dataType: "json",
      data: {
        email: email
      },
      success: function (response) {
        $("#OTPField").removeClass("d-none");
        $("#OTPBtn").addClass("d-none");
        $("#signupBtn").removeClass("d-none");
        $(".google-sign-in").addClass("d-none");
      }
    });
  }
};