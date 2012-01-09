jQuery(function($) {
    /* 
     * Cycle through row immediately on load and change the value of the input  
     * Match all ordering field inputs (with regex to be sure)
     * add a small bit of html before to show a cursor image with some 
     * hover text, and also change the css cursor of the entire td element  
	 */
     var that = this;       
	 var ordering_inputs = $('tbody tr td input','table#result_list').filter(function(){ return this.id.match(/id_form-[\d+]-ordering/)})
     ordering_inputs
    .css('display', 'none')
    .before("<div class='draggable'><div class='move-cursor'>&nbsp;</div></div>")
    .parent('td')
    .css('cursor', 'move !important')
            
    $('table#result_list').sortable({
        opacity: 0.8,
        axis: 'y', 
        items : 'tr',
        tolerance : 'pointer', 
        handle: 'div.draggable',
        containment: 'table#result_list tbody',
        update : function(event, ui){
            $(this).find('tr').each(function(i) {
                /* Recalculate the background colors for each row*/
                if(i%2==0){
                    $(this).css('background-color', '#EDF3FE');
                }else{
                    $(this).css('background-color', 'white');
                }
                /* Update the values of the hidden inputs */
                $(this).find('td .draggable').next('input').val(i);
				console.log($(this).find('td .draggable').next('input'));
            });
            /* Do a highlight on the dropped row */
            var orig_bg = $(ui.item).css('background-color')
            $(ui.item).css('background-color', '#ffff99').animate({'backgroundColor' : orig_bg}, 1500);
        },
    });
});