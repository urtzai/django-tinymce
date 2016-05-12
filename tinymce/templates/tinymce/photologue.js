function djangoPhotologue(callback, value, meta){
    if (meta.filetype == 'image') {
	    tinymce.activeEditor.windowManager.open({
		    file: '/tinymce/photologue/panel/',
		    title: '{{title}}',
		    width: 900,  
		    height: 450,
		    resizable: 'yes',	
		}, {
			'button': "{{button}}",
		    setUrl: function (url) {
		      callback(url);
		    }
		});
	}
  	return false;
}
