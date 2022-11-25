$(document).ready(function(){

	$('.chat_head').click(function(){
		$('.chat_body').slideToggle('slow');
	});
	$('.msg_head').click(function(){
		$('.msg_wrap').slideToggle('slow');
	});

	$('.close').click(function(){
		$('.msg_box').hide();
	});

	$('.user').click(function(){

		$('.msg_wrap').show();
		$('.msg_box').show();
	});


    $('#submitt').click(
    function(){
    var msg = $('.msg_input').val();
			$('msg_input').val('');
			var x=$('.hiii').val();

			if(msg!=''){}
			//$('<div class="msg_b">'+msg+'</div>').insertBefore('.msg_push');
			//$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);

         //   $('<div class="msg_a">'+{{message}}+'</div>').insertBefore('.msg_push');
           // $('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
    }
    );


$('.msg_input').keypress(
    function(e){
        if (e.keyCode == 13) {
            e.preventDefault();
            var msg = $(this).val();
			$(this).val('');
			var x=$('.hiii').val();
			//$('#submitt').val()==true;
			if(msg!=''){}
			//$('<div class="msg_b">'+msg+'</div>').insertBefore('.msg_push');
			//$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);

          //  $('<div class="msg_a">'+x+'</div>').insertBefore('.msg_push');
            //$('.msg_body').scrollTop($('.msg_body')[0].scrollHeight);
        }
    });
      });
