$('#submitModal').on('show', function() {
   alert("here...");
    var link = $(this).data('link'),
        confirmBtn = $(this).find('.confirm');
})

$('#btnYes').click(function() {
  
    alert("submitting...");
    // handle form processing here
    $('form').submit();
});

