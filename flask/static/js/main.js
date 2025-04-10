////===========================================================//
//File Name:			main.js
//Author:			Pedro Cumino
//Email:			pedro.cumino@gmail.com
//Creation Date:		Sat 22 Feb 12:36:59 2025
//Last Modified:		Mon  3 Mar 19:26:17 2025
//Description:
//Args:
//Usage:
//===========================================================//
function ask(question)
{
	alert(question);
	response = 'response';
	return response;
}

function scrollToBottom() {
	$("html, body").animate({ scrollTop: $(document).height() }, 1);
}


// $('#response').removeAttr("hidden");
// $('#response').show();
// console.log("```python\noi\n```");

// $('#response').html(marked.parse("```python\noi\n```"));

var answer = "";


$(document).ready(function(e){
	let agent = '';
	
	$("form#ask").on("click", "input[type=submit]", function(e) {
		agent = $(this).attr("id");
	});
	
	$("form#ask").on("submit", function(e){
		e.preventDefault();

		if ($("textarea#prompt").val().length <= 1) {
			return;
		}

		var data = $(this).serialize()+`&agent=${agent}`;
		
		// $('#response').html($('#response').html() + "<br><br>" + `Agent [${parseInt(agent)+1}]: `);
		$("input.agent").attr({'disabled':true});
		scrollToBottom();
		
		$.ajax({
			type: 'POST',
			url: $(this).attr('action'),
			data: data,
			xhr: function(){
				var xhr = new window.XMLHttpRequest();
				var lastResponseLength = 0;
				xhr.onprogress = function() {
					var currentResponse = xhr.responseText.substring(lastResponseLength);
					
					if (lastResponseLength == 0) {
						$('#response').removeAttr("hidden");
						$('#response').show();
						var line = $('#response').html() + `<span class="agent-name">${agent.toLocaleUpperCase()}</span> `;
						$('#response').html(line);
					}
					lastResponseLength = xhr.responseText.length;
					
					answer += currentResponse;
					
					$('#response').html(`<span class="agent-name">${agent.toLocaleUpperCase()}</span> <br>` + marked.parse(answer) + '<br>');
					scrollToBottom();
					
				};
				return xhr;	
			},
			success: function() {
				$("input.agent").removeAttr('disabled');
				
				var line = $('#response').html();
				$('#response').html(line + '<br>');

				answer += "\n\n";
			},
			error: function() {
				// console.log('Error');
			}
		});
	});


	$('input[type="submit"]').on("contextmenu", function(e) {
		$("span.agent-description").hide();
		clearTimeout();

		// Prevent default context menu behavior
		e.preventDefault();
		
		// Get the clicked element and its corresponding span element
		var this_tag_id = $(this).attr("id");
		var span_tag = $("span[for='" + this_tag_id + "']");

		
		// // Position the span element relative to the mouse pointer
		// span_tag.css({top: e.pageY, left: e.pageX, margin: 5});
		// span_tag.css({top: e.pageY-(span_tag.height()/1.8), left: e.pageX});
		// span_tag.css({margin: 5});

		
		// Show the span element
		span_tag.removeAttr("hidden");
		span_tag.show();
		setTimeout(() => {
			span_tag.hide();
		}, 3000);
		// span_tag.attr("hidden",true);
		
		
	});



});
