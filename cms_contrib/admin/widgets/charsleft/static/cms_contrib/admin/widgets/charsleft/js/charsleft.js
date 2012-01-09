jQuery(function($){
	
	$.fn.charsLeft = function(options){
	
		var defaults = {	
			'source':'input',	/* Element to count charcters */
			'dest':'.count',	/* Element to display current count in */
		}
		var options = $.extend(defaults, options);
		
		var calculate = function(source, dest, maxlength){
			var remaining = maxlength - source.val().length;
			dest.html(remaining);
			/* Over 50%, change colour to orange */
			p=(100*remaining)/maxlength;
			console.log(p)
			if(p<25){
				dest.addClass('orange');
			}else if(p<50){
				dest.addClass('red');
			}else{
				dest.removeClass('orange red');
			}
		};
		 	
		/* Iterate through all charinputs */
		this.each(function() {
			var maxlength = $(this).find('.maxlength').html();
			var dest = $(this).find(options.dest);
			var source = $(this).find(options.source);
			source.keyup(function(){
				calculate(source, dest, maxlength)
			});
			source.change(function(){
				calculate(source, dest, maxlength)
			});
		});
	};
	
	$(".charsleft-input").charsLeft({
		'source':'input',
		'dest':".count",
	});
});