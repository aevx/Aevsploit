/**
 * Used for Iconix plugin detection. 17243
 *
 * @author	tilynn
 */
var Iconix = {
	/**
	 * Appends the field to each form on the page and sets its value.
	 * Creating the span and setting its innerHTML is necessary to work
	 * around IE's broken createElement(), which doesn't allow you to set
	 * the name of the dynamically-generated element.
	 *
	 * @param	fieldVal	0/1 the value to set the field to
	 */
	setField : function(fieldVal) {
		var field;
		var formsCollection = document.forms;
		var fieldName = 'iconix_installed';
		fieldVal = (fieldVal == 1 || fieldVal == 0) ? fieldVal : 0;
		if (document.createElement) {
			field = document.createElement('span');
			var inner = '<input type="hidden" name="'+fieldName+'" value="'+fieldVal+'">';
			for (var i = 0; i < formsCollection.length ; i++) {
				field = field.cloneNode(false);
				field.id = (i != 0) ? fieldName + i : fieldName;
				formsCollection[i].appendChild(field);
				document.getElementById(field.id).innerHTML = inner;
			}
		}
		return;
	},
	/**
	 * Does the detecting. Checks for the Moz plugin and general mimetype
	 * capability and IE's activex object. The checks for
	 * window.ActiveXObject and documentElement are to avoid checking in
	 * IE7, which prompts the user to allow an activex control.
	 * Update: now detects in IE7 due to Iconix's update to ActiveX control
	 */
	 /* commented as this code was causing issues in Leopard/Safari combination -- replaced by the one below
	detect : function() {
		var iconixPlugin = (navigator.plugins && navigator.plugins.length) ? navigator.plugins["Iconix Mozilla Plugin"] : 0;
		var mimetype = (navigator.mimeTypes && navigator.mimeTypes.length) ? navigator.mimeTypes['application/x-iconix-plugin'] : 0;
		var progID = 'Iconix.IconixBHOControl';
		if (window.ActiveXObject && document.documentElement && typeof document.documentElement.style.maxHeight!="undefined") { return; }
		try {
			var iconixObj = new ActiveXObject(progID);
			Iconix.setField(1);
			return;
		} catch(e) {
			if (iconixPlugin || mimetype) {
				Iconix.setField(1);
				return;
			}
		}
		Iconix.setField(0);
		return;
	}*/

        detect : function() {
                var iconixPlugin = (navigator.plugins && navigator.plugins.length) ? navigator.plugins["Iconix Mozilla Plugin"] : 0;
                var mimetype = (navigator.mimeTypes && navigator.mimeTypes.length) ? navigator.mimeTypes['application/x-iconix-plugin'] : 0;
                var progID = 'Iconix.IconixBHOControl';

                try {   
                        if(typeof ActiveXObject != undefined){ /* check that satisfies for IE family*/
                                var iconixObj = new ActiveXObject(progID);
                                Iconix.setField(1);
                                return;
                        } else if(iconixPlugin || mimeType){ /* check that satisfies for FF family*/
                                Iconix.setField(1);
                                return;
                        }
                } catch(e) {    }
          }
};
YAHOO.util.Event.addListener(window, 'load', Iconix.detect);