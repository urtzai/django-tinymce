function djangoPhotologue(callback, value, meta){
    if (meta.filetype == 'image') {
	    tinymce.activeEditor.windowManager.open({
		    file: '/static/photologue/index.html',// use an absolute path!
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
